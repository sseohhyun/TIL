# 1. html

- 웹 페이지 구성요소 : `HTML(구조)`, `CSS(스타일링`), `javascript(동작)`

## 1) HTML 정의

- 웹 페이지의 의미와 구조를 정의하는 언어입니다.

### (1) Hypertext

- 웹 페이지를 다른 페이지로 연결하는 링크, 참조를 토앻 사용자가 한 문서에서 다른 문서로 즉시 접근할 수 있는 텍스
- 비선형성, 상호 연결성, 사용자 주도적 탐

### (2) Markup Language

- 태그 등을 이용하여 문서나 데이터의 구조를 명시하는 언어 (예: HTML, 마크다운)
- 어디에서 시작하고 어디에서 끝날지 알려줌
    

## 2) HTML 구조

```html
<!DOCTYPE html> # 해당 문서가 html로 만들어진 문서라는 것을 나타냄
<html lang="en"> # 웹 사이트의 언어를 설정함

<head> # html 문서에 관련된 설명, 설정 등 컴퓨터가 식별하는 메타데이터를 작성, 사용자에게 보이지 않음 
  <meta charset="UTF-8"> 
  <title>My page</title>
</head>

<body> # html 문서의 내용을 나타냄
  <p>This is my page</p>
  <a href="https://www.google.co.kr/">Google로 이동</a>
  <img src="images/sample.png" alt="sample-img"> # 상대경로로 로컬에 있는 파일을 명시
  <img src="https://random.imagecdn.app/500/150/" alt="sample-img"> # 주소 명
</body>

</html>
```

### (1) HTML Element(요소)

- 하나의 요소는 여는 태그와 닫는 태그 그리고 그 안의 내용으로 구성됨
- 닫는 태그는 태그 이름 앞에 슬래시가 포함됨 (닫는 태그가 없는 태그도 존재)
    

### (2) HTML Attribute(속성)

- 사용자가 원하는 기준에 맞게 요소를 설정하거나 다양한 방식으로 요소의 동작을 조절하기 위한 값
    
- 속성 작성 규칙
    - 소문자로 작성
    - 꼬치 -ㅁ-ㅁ-ㅁ- `kebab case` 모양으로 명명
    - 속성은 요소 이름과 속성 사이에 공백이 있어야 함
    - 하나 이상의 속성들이 있는 경우엔 속성 사이에 공백으로 구분함
    - 속성 값은 열고 닫는 따옴표로 감싸야

### (3) HTML 실습

- `!+탭:` 기본 구조 자동 생성
- `alt + b`: 브라우저에서 HTML 파일을 쉽게 실행합니다.

## 3) HTML Text structure

HTML의 주요 목적 중 하나는 `텍스트 구조와 의미를` 제공하는 것입니다.

### (1) Heading & Paragraphs

- <h1> </h1> : 단순히 테스트를 크게 만드는 것이 아니라 현재 문서의 최상위 제목이라는 의미를 부여하기 위한 것
- h1~6, p

### (2) Lists

- ol, ul, li

### (3) Emphasis & Importance

- em, strong

# 2. 웹 스타일링, CSS

cascading(계단식) style sheet, 웹 페이지의 디자인과 레이아웃을 구성하는 언어

- 선택 : 적용 위치
- `인라인 스타일` : 사용x
- `내부 스타일 시트`: head 태그 안에 style 태그에 작
- `외부 스타일 시트`: 별도의 CSS 파일을 생성하여 html link 태그를 사용하여 로드합니다.
    
    ```html
    <link rel="stylesheet" href ="style.css"> # shyle.css 파일 불러오기
    ```
    
    ## 1) CSS 선택자
    
    html 요소를 선택하여 스타일을 적용할 수 있도록 하는 선택
    
    - 기본 선택자
        - `전체(*) 선택자` : 모든 HTML 요소 선택
        - `요소(tag) 선택자` : 지정된 모든 태그를 선택
        - `클래스(class) 선택자`: **(’.’)** 주어진 클래스 속성을 가진 모든 요소를 선택
        - `아이디(ID) 선택자` : 주어진 아이디 속성을 가진 요소 선택, 문서에는 주어진 아이디를 가진 요소가 **하나**만 있어야 함
        - `속성(attr) 선택자` 등
    - 결합자
        - `자손 결합자 (" "(space))`
            - .green li : green 클래스를 가진 li 태그들
            - 모든 자식을 의미
        - `자식 결합자 (">")`
            - .green > li : green 클래스를 가진 자식 li 태그들
            - 자식은 모두 **직계 자식**만을 의미함

    
    ```html
      <style>
        /* 전체선택자 */
        * {
          color: red;
        }
    
        /* 타입 선택자 */
        h2 {
          color: orange;
        }
    
        h3, h4 {
          color: blue;
        }
    
        /* 클래스 선택자 */
        .green {
          color: green;
        }
    
        /* id 선택자 */
        #purple {
          color: purple;
        }
    
        /* 자손 결합자, 띄어쓰기 */
        .green li {
          color: brown;
        }
    
        /* 자식 결합자, > */
        .green > li {
          font-size: 30px;
        }
    
      </style>
    ```
    
    - 결합자 사용 예시
        
        ```html
        div.box>ul.todo-list#lsit>li*3 # 라고 입력하면
        # div의 클래스=box 이고, 자식인 ul의 클래스=todo-list, id=list 이고, 자식인 li를 3개 만들어줘
        
          <div class="box">
            <ul class="todo-list" id="lsit">
              <li></li>
              <li></li>
              <li></li>
            </ul>
          </div>
        ```
        
    
    ## 2) 명시도
    
    결과적으로 요소에 적용할 CSS 선언을 결정하기 위한 알고리즘
    
    ### (1) Cascade 예시
    
    ### (2) 명시도가 높은 순
    
    - inportance (`!important`) : 극단적이므로 평소에 잘 사용x, 디버깅 할 때 사용
    - inline 스타일 : 오류가 날 수 있으므로 사용 추천 x
    - 선택자 (id > class > 요소)
    - 소스 코드 선언 순서
    - 상속
        
    
    ### (3) 명시도 연습
    
    - 3,4, 7,8 부분 확인해보기
        
        ```html
        <!DOCTYPE html>
        <html lang="en">
        
        <head>
          <meta charset="UTF-8">
          <meta name="viewport" content="width=device-width, initial-scale=1.0">
          <title>Document</title>
          <style>
            h2 {
              color: darkviolet !important;
            }
        
            p {
              color: blue;
            }
        
            .orange {
              color: orange;
            }
        
            .green {
              color: green;
            }
        
            #red {
              color: red;
            }
          </style>
        </head>
        
        <body>
          <p>1</p>
          <p class="orange">2</p>
          <p class="green orange">3</p>
          <p class="orange green">4</p>
          <p id="red" class="orange">5</p>
          <h2 id="red" class="orange">6</h2>
          <p id="red" class="orange" style="color: brown;">7</p>
          <h2 id="red" class="orange" style="color: brown;">8</h2>
        </body>
        
        </html>
        ```
        
    - 3, 4 이유 정리
        
        **✅ 왜 둘 다 초록색(`green`)으로 보일까?**
        
        HTML에서는 `class="green orange"`와 `class="orange green"`의 순서가 **스타일 적용 우선순위에 영향을 주지 않아**.
        
        즉, 클래스가 두 개 있으면 **CSS에서 나중에 선언된 규칙이 우선함**.
        
        ```css
        .orange { color: orange; }   /* 먼저 선언됨 */
        .green  { color: green; }    /* 나중에 선언됨 → 이게 이김! */
        ```
        
        그래서 `.green`이 `.orange`보다 나중에 정의되었기 때문에 **`.green`이 우선 적용**돼서 초록색이 된 거야.
        
    
    ## 3) 상속
    
    부모 요소의 속성을 자식에게 상속해 재사용성을 높임

    

# 3. CSS Box MODL

웹 페이지의 모든 HTML 요소를 감싸는 사각형 상자 모델

## 1) 박스타입

박스 타입에 따라 페이지에서의 배치 흐름 및 다른 박스와 관련하여 박스가 동작하는 방식이 달라짐

### (1) Outer display type (block & inline)

박스가 문서 흐름에 어떻게 동작할 지를 결정함

- **`block 특징`**
    - `h1~6, p, div 태그`는 일반적으로 디스플레이가 block 인 요소임
    - 항상 새로운 행으로 나뉨
    - 너비, 높이 지정 가능
    - padding, margin, border 를 설정해 다른 요소를 상자로부터 밀어낼 수 있음
    - width 속성을 지정하지 않으면 박스는 inline 방향으로 사용 가능한 공간을 모두 차지함
    (상위 컨테이너 너비 100%로 채우는 거)
- **`inline 특징`**
    - `a, img, span, strong, em` 은 대표적인 inline 타입 태그
    - 새로운 행으로 넘어가지 않음
    - padding, margin, border는 적용되나, 수평 방향으로만 다른 요소르 밀어낼 수 있음
    

**`nomal flow`**  : 일반적인 흐름 또는 레이아웃을 변경하지 않은 경우, 웹 페이지 요소가 배치되는 방식

### (2) inner display type (block & inline)

- 내일 수업 진행
- 

# 4. 참고

## 1) html 스타일 가이드

- 대소문자 구분
    - html은 대소문자를 구분하지 않지만, 소문자 사용을 강력히 권장
    - 태그명과 속성명 모두 소문자로 작성
- 속성 따옴표
    - 속성 값에는 큰 따옴표(”)를 사용하는 것이 일반적
- 코드 구조와 포맷팅
    - 일관된 들여쓰기를 사용 (tab)
- 공백 처리
    - html은 연속된 공백을 하나로 처리
    - enter키로 줄 바꿈을 해도 브라우저에서 인식하지 않음
- 에러 출력 x

## 2) css 스타일 가이드

- 코드 구조와 포맷팅(html과 유사)
    - 마지막 속성 뒤에는 세미콜론(;) 넣기
- 선택자 사용
    - class 선택자 우선적으로 사용
    - id, 요소 선택자 등은 가능한 피할 것
- 속성과 값
    - 속성과 값은 소문자로 작성
    - 0 값에는 단위를 붙이지 않음
- 명명 규칙
    - 케밥 케이스를 사용(kebab case)
- css 적용 스타일
    - 인라인 스타일 되도록이면 사용x