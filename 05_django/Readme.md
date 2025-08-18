# 일종의 기획서를 작성한다. (aka. 알고리즘 수도코드)
"이미 정해져 있는 한 가지"
1. 기술스택 - django, djangorestframework 쓸거임.

- 흥미가 없음. (웹 개발 부분은 내가 나중에 만들내 데이터를 서비스할 수 있는 방법 중에 하나)
1. 목표를 정해야 한다.

- 대단한 이야기를 했지만, 지금은 공부하는 중... 이므로 그냥 기본적인 게시글
  (why article 인가요?)

- 무슨 서비스를 만들 것인가?
  1. 회원가입이 가능해야 하며, 회원만 접근 할 수 있는 기능이 있어야 한다.
  2. 게시글을 작성할 수 있어야 하고, 각 게시글들마다 댓글을 달 수 있어야 한다.
  3. 게시글은 유저만 작성할 수 있고, 
  4. 유저는 다른 유저가 작성한 게시글을 찜하거나 추천 할 수 있어야 한다.
  5. extra. 유저 활동 기반 추천 알고리즘을 만든다. (하이라키컬, 가우시안 믹스쳐)
    - 이 부분이 여러분들의 몫

- 모델을 정의한다.
  1. User Model
    - django가 기본 제공하는 User Model을 사용할 예정이다.
    - 필요에 따라서, User Model을 커스터마이징 해야 할 수도 있다.
      - 회원가입 시점에 해당 정보를 수집할 수도 있어야 한다.

      | User | 유저 정보를 저장 |
      |---|
      | id | 고유값 | PK | ....
      | django 기본 제공 필드 |
      | age | 나이 | INT |
      | phone | 핸드폰 번호 | TEXT |

  2. Article Model
    - User Model과 어떤 관계인가?
      1. 1:N 관계 (게시글 작성자 정보를 저장 해야함)
      2. M:N 관계 (여러명의 유저가 여러개의 게시글을 `좋아요` 할 수 있어야 함)
    | Article | 게시글 정보 저장 |
    | title | 제목 | CHAR(100) |
    | content | 내용 | TEXT |
    | created_at | 작성일 | DATE? DATETIME? |
    | user_id | 작성자 | FK |

  3. Comment Model
  4. User-Artice M:N 관계 테이블
    - 누가? 무엇과? 관계를 맺는가?
    - 1번 유저가 1번 게시글과 관계를 맺는다.
    - 1번 유저가 2번 게시글과 관계를 맺는다.
    - 2번 유저가 1번 게시글과도 관계를 맺을 수 있다.
    | like | 좋아요 정보를 저장 |
    | user_id | 좋아요를 누른 유저 | FK |
    | article_id | 위의 user가 좋아요를 누른 게시글 | FK |
    | created_at | 좋아요를 누른 시간 | DATATIME |
  
- 기능 정리
  1. 회원가입 요청 방법 -> 응답 방식
  2. 로그인 요청 방법 -> 응답 방식
  3. 프로필 요청 방법 -> 응답 방식
  4. 게시글 작성 요청 방법 -> 응답 방식
  5. 게시글 전체 조회 요청 방법 -> 응답 방식
  6. 게시글 수정, 삭제, 상세 조회 요청 방법 -> 응답 방식
  7. 댓글 어쩌구 -> 저쩌구
  8 ... 
  9 ...
  10 ....

  # 요청과 응답
  - django에서는 (일반적인 웹 서비스에서는) 어떤 순으로 처리하는가?
  1. 식별 (Client가 요청을 보낼 위치)
  2. 행위
  3. 표현
  - base domain - `http://127.0.0.1:8000/`
  - 기획단계에서는 노션 등으로 작성해서 공유하고,
    - 실제 백엔드 개발 담당자는 SWAGGER 등을 사용해서 docs화해서 제공
  | 기능 설명 | 행위 | 식별 | 표현 | 응답 방식 |
  | 회원 가입 | POST | accounts/signup/ | dj-rest-auth | Token |

  1. accounts 관련 기능 모음
    1. 회원 가입
      - 요청 방식 `POST accounts/signup/`
      - 응답 데이터
        ```JSON
        {
          "token": "dj-rest-auth가 반환한 토큰값"
        }
        ```
      - 구현 방식: `dj-rest-auth[with-social]` 활용한 registration
  2. articles 관련 기능 모음
    1. 게시글 작성
      - 요청 방식 `POST articles/`
      - 응답 방식
      ```JSON
        {
          "title": "문자열",
          "content": "문자열",
          "created_at": "날짜, 시간",
          "createdAt": "날짜, 시간",
        }
      ```
    2. 게시글 상세 조회
      - 요청 방식 `GET articles/{article_id}/`
      - 응답 방식 
      ```JSON
        {
          # 게시글이 가진 모든 필드?
          # 댓글에 대한 추가 정보도 보내줄 것이냐?
          "title"
          "content"
          "created_at"
          "comments": [
            {
              "id",
              "user_name",
              "content",
            }
          ]
        }
      ```