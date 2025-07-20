# branch
## 장점 
1) 독립된 개발 환경을 형성하기 때문에 원본에 대해 안전
2) 하나의 작업은 하나의 브랜치로 나누어 진행되므로 체계적으로 협업과 개발이 가능
3) 손쉽게 브랜치를 생성하고 브랜치 사이를 이동할 수 있음

init -> 작업 -> add -> commit -> push -> pull(집) (해당 파일에서 git으로 실행해서 git pull 입력하기)

다른 폴더의 커밋을 옮기는 것은 불가능

전체를 관리하는 깃과 그 하위 폴더를 또 깃으로 관리를 할 수 있긴 함 = 서브모듈

문제발생 시 폴더를 다른 쪽을 옮기기 → add,

```markdown
1. git config 초기화
  - `$ git config --global 설정` 삭제
  - `$ code ~/.gitconfig` 를 실행
  - 해당 설정에 작성된 username과 email 모두 지우기

2. 자격 증명 초기화
  - `win+자격증명` 검색 > 자격 증명 관리자
  - windows 자격 증명 > 깃허브, 깃랩 계정 정보 삭제
```

파일은 study 에 복붙해 넣기

- git init = 폴더를 완전 처음 만들었을 때 사용함 (깃에게 이제부터 관리해달라고 명령)

→ 이미 깃으로 관리를 하고 있는 상황에서 다시 입력하면 문제 발생, 따라서 add, commit 을 하기

- add 전에 status 하기
    
    만약 새로운 파일이 만들어졌다면, status 확인해서 add 하고 다시 status 확인하기 그러고 commit하기 
    
- git commit -m “이번 버전의 메시지”
- vim에 들어왔다면 → :q (나가)
- push가 안되는 경우, 원격저장소와 내가 저장하려는데가 다를 때
    - git pull 먼저 진행 → vim 창이 나올것임  :q 로 빠져나오기 →

branch

: 나뭇가지처럼 뻗어나오는 형태로 작업을 해나가는 것

```bash
$ git branch -c viktor/login
```

create viktor 가 login 작업을 하도록 작업공간 생성

```bash
$ git switch viktor/login
```

마스터에서 빅터 확경으로 변경

```bash
git log # 제작한 사람 확인 가능
```

헤리로 스위치하면 빅터 작업환경에서 만들었던 파일이 보이지 않음 → 개인이 만든 파일은 개인의 작업환경에서만 보임 → 하나의 공간에 있도록 어떻게 합칠 수 있는가?

```bash
git merge viktor/login # 마스터에서 빅터거를 병합함
```

마스터로 switch 후 merge 하기 : `Fast-forward`

- 처음에 빅터를 할때는 vim이 안켜지는데 herry를 후에 치면 vim이 켜짐

```bash
$ git log --oneline --gragh
```


fast forward인 이유 :  이해 못했음..ㅜㅠ

`three way merge`  도 있음
```bash
git push origin katie
```
origin은 저장소 별명, katie 작업자

``` bash
git branch -c katie
git branch # 브랜치 확인

git switch katie

# 파일 만들기
touch katie.md
git add katie.md
git commit -m " katie  작업 완료"

git push origin katie

git switch master
git pull

git branch -d katie
```

같은 파일의 같은 줄을 다른 사람이 수정한걸 머지 하려고 하면 충돌이 발생함(컴플릭트)
-> 처음, 나중, 둘다 중에 선택 가능 또는 코드를 직접 수정할 수도 있음

merge 오류 해결 
resolve locaaly

로컬에는 마스터와 katie가 존재
원격저장소에는 오리진, 마스터가 있음

1, katie가 push가 되어서 원격저장소에 들어가고 그게 마스터와 마지하려다가 충돌이 나는 상황
2. 로컬에서 마스터로 바꿔서 쓰더라도 다른 저장소의 마스터 내용과는 다른 상황
3. 따라서 로컬에서 마스터로 쓸 때 최신화를 하고 나서 마지하도록 해야

``` bash
git pull origin master
git add .
git commit -m "충돌해결"
git push

git pull # 마스터를 머지 후 최신걸로 다운 받는 과정
```

# 2. Git workflow
- 원격 저장소를 활용해 다른 사람과 협업하는 

1) master 브랜치는 아무도 수정하지 않는다.
2) master 브랜치는 최초 설정 (모든 팀원이 함게 쓸 내용 생성시만 사용)
  - git add, git commit, push 까지 모두 진행
3) 팀장이 develop(혹은 dev) 브랜치를 생성한다.

(dev 1차 완성 -> relese 라는 브랜치를 생성해서 중간 완성 단계를 저장함 -> master가 최종 완성)

