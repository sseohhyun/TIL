from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Articel
from .serializers import ArticleListSerializer

# Create your views here.
@api_view("GET", 'POST')
def article_get_or_create(request):
    if request.method == "GET":
        # 전체 게시글 조회
        articles = Articel.objects.all()
        # 전체 게시글 조회라서, id, title만 보여주고 싶음
        # serializer라는 걸 정의
        serializer = ArticleSerializer(articles, many = True)
        # 직렬화를 마친 객체의 data만 사용자에게 반환
        # 그리고, 이 직렬화는 Django가 아닌 DRF로 인해 만들어진 것
        # 즉 반환도 Django 기본 기능이 아니라 drf 의 반환 방식을 쓸 것임 
        return Response(serializer.data)

    elif request.method == "POST":
        # 사용자가 보낸 데이터로 article을 생성, 그 정보가 유효한지 검증, 정상적이변 저장 & 반환
        serializer = ArticleSerializer()

