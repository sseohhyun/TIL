# movies/management/commands/import_movies.py
import csv
import json
from pathlib import Path
from datetime import datetime
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from django.conf import settings

from movies.models import Movie, Genre, Cast, Review


def parse_date(s: str):
    if not s:
        return None
    for fmt in ("%Y-%m-%d", "%Y/%m/%d", "%Y.%m.%d"):
        try:
            return datetime.strptime(s, fmt).date()
        except ValueError:
            continue
    return None


def to_int(x):
    """'123' 또는 '123.0' 등을 안전하게 int로 변환"""
    if x in (None, ""):
        return None
    try:
        return int(float(x))
    except (ValueError, TypeError):
        return None


def to_float(x):
    if x in (None, ""):
        return None
    try:
        return float(x)
    except (ValueError, TypeError):
        return None


def parse_genre_names(raw):
    """
    'Action|Drama' / 'Action,Drama' / '["Action","Drama"]' / 'Action' 모두 지원
    """
    if not raw:
        return []
    s = str(raw).strip()
    if s.startswith('['):  # JSON 배열
        try:
            data = json.loads(s)
            return [str(x).strip() for x in data if str(x).strip()]
        except json.JSONDecodeError:
            pass
    for sep in ('|', ',', ';', '/'):
        if sep in s:
            return [p.strip() for p in s.split(sep) if p.strip()]
    return [s]  # 단일 값


class Command(BaseCommand):
    help = "Load CSVs in data/ into DB (movies, genres via details, casts, reviews)."

    def add_arguments(self, parser):
        parser.add_argument(
            '--base', default=None,
            help='Base dir that contains data/ (default: BASE_DIR)'
        )
        parser.add_argument(
            '--encoding', default='utf-8',
            help='CSV encoding (utf-8 or cp949, etc.)'
        )

    def handle(self, *args, **opts):
        base_dir = Path(opts['base']) if opts['base'] else Path(settings.BASE_DIR)
        data_dir = base_dir / 'data'
        enc = opts['encoding']

        # CSV 경로
        movies_csv   = data_dir / 'movies.csv'
        details_csv  = data_dir / 'movie_details.csv'   # ← 장르/상세 정보가 여기에 있음
        casts_csv    = data_dir / 'movie_cast.csv'
        reviews_csv  = data_dir / 'movie_reviews.csv'
        # (선택) 별도 장르 마스터가 있다면 사용 가능
        genres_csv   = data_dir / 'genres.csv'

        # 필수 파일 존재 확인
        for p in [movies_csv, casts_csv, reviews_csv]:
            if not p.exists():
                raise CommandError(f'CSV not found: {p}')

        self.stdout.write(self.style.NOTICE(f'Data dir: {data_dir}'))

        with transaction.atomic():
            # (선택) 별도 장르 마스터가 있다면 미리 로드
            if genres_csv.exists():
                with genres_csv.open(encoding=enc, newline='') as f:
                    reader = csv.DictReader(f)
                    created = 0
                    for row in reader:
                        name = (row.get('name') or '').strip()
                        if not name:
                            continue
                        gid = to_int(row.get('id'))
                        if gid is not None:
                            obj, was_created = Genre.objects.update_or_create(
                                id=gid, defaults={'name': name}
                            )
                        else:
                            obj, was_created = Genre.objects.get_or_create(name=name)
                        if was_created:
                            created += 1
                    self.stdout.write(self.style.SUCCESS(
                        f'Genres upserted (from genres.csv): +{created}'
                    ))

            # 1) movies.csv → Movie upsert
            with movies_csv.open(encoding=enc, newline='') as f:
                reader = csv.DictReader(f)
                upsert = 0
                for r in reader:
                    mid = to_int(r.get('id'))
                    if mid is None:
                        continue
                    m, _ = Movie.objects.update_or_create(
                        id=mid,
                        defaults={
                            'title':       r.get('title') or '',
                            'release_date': parse_date(r.get('release_date')),
                            'popularity':   to_float(r.get('popularity')),
                            'budget':       to_int(r.get('budget')) if r.get('budget') not in (None, '', 'null') else 0,
                            'revenue':      to_int(r.get('revenue')) if r.get('revenue') not in (None, '', 'null') else 0,
                            'runtime':      to_int(r.get('runtime')) if r.get('runtime') not in (None, '', 'null') else 0,
                        }
                    )
                    upsert += 1

                    # 만약 movies.csv 자체에 genres 열이 있다면 누적 추가 (옵션)
                    raw_genres = r.get('genres')
                    if raw_genres:
                        names = parse_genre_names(raw_genres)
                        if names:
                            genre_objs = [Genre.objects.get_or_create(name=n)[0] for n in names]
                            # 누적 추가
                            m.genres.add(*genre_objs)

                self.stdout.write(self.style.SUCCESS(f'Movies upserted: {upsert}'))

            # 2) movie_details.csv → 상세 값 업데이트 + ★장르 연결★
            if details_csv.exists():
                touched = 0
                with details_csv.open(encoding=enc, newline='') as f:
                    reader = csv.DictReader(f)  # 헤더: movie_id,budget,revenue,runtime,genres
                    for r in reader:
                        mid = to_int(r.get('movie_id'))
                        if mid is None:
                            continue
                        try:
                            m = Movie.objects.get(pk=mid)
                        except Movie.DoesNotExist:
                            continue

                        # 상세 값 업데이트(비어있으면 건너뜀)
                        updates = {}
                        b = to_int(r.get('budget'))
                        if b is not None:
                            updates['budget'] = b
                        rv = to_int(r.get('revenue'))
                        if rv is not None:
                            updates['revenue'] = rv
                        rt = to_int(r.get('runtime'))
                        if rt is not None:
                            updates['runtime'] = rt
                        if updates:
                            for k, v in updates.items():
                                setattr(m, k, v)
                            m.save(update_fields=list(updates.keys()))

                        # ★ 장르 연결 (덮어쓰기: set)
                        names = parse_genre_names(r.get('genres'))
                        if names:
                            genre_objs = [Genre.objects.get_or_create(name=n)[0] for n in names]
                            m.genres.set(genre_objs)  # 기존 것을 대체 (현재 비었으니 가장 깔끔)
                        touched += 1

                self.stdout.write(self.style.SUCCESS(
                    f'Details processed (incl. genres): {touched}'
                ))
            else:
                self.stdout.write(self.style.WARNING(
                    'movie_details.csv not found; skip details/genres.'
                ))

            # 3) movie_cast.csv
            with casts_csv.open(encoding=enc, newline='') as f:
                reader = csv.DictReader(f)
                bulks = []
                for r in reader:
                    mid = to_int(r.get('movie_id'))
                    if mid is None:
                        continue
                    try:
                        movie = Movie.objects.get(pk=mid)
                    except Movie.DoesNotExist:
                        continue
                    bulks.append(Cast(
                        movie=movie,
                        name=(r.get('name') or '').strip(),
                        character=(r.get('character') or None),
                        order=to_int(r.get('order')),
                    ))
                if bulks:
                    Cast.objects.bulk_create(bulks, ignore_conflicts=True)
                self.stdout.write(self.style.SUCCESS(f'Casts inserted: {len(bulks)}'))

            # 4) movie_reviews.csv
            with reviews_csv.open(encoding=enc, newline='') as f:
                reader = csv.DictReader(f)
                bulks = []
                for r in reader:
                    mid = to_int(r.get('movie_id'))
                    if mid is None:
                        continue
                    try:
                        movie = Movie.objects.get(pk=mid)
                    except Movie.DoesNotExist:
                        continue
                    bulks.append(Review(
                        movie=movie,
                        author=(r.get('author') or '').strip(),
                        content=(r.get('content') or ''),
                        rating=to_float(r.get('rating')),
                    ))
                if bulks:
                    Review.objects.bulk_create(bulks, ignore_conflicts=True)
                self.stdout.write(self.style.SUCCESS(f'Reviews inserted: {len(bulks)}'))

        self.stdout.write(self.style.SUCCESS('CSV import completed.'))
        