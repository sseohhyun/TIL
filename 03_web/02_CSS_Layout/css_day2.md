# 1. CSS Box Model

- `Outer display type`, `inner display type`

## 1) 박스 구성 요소

- margin - border - padding - content
    
    ```html
    .box1 {
          width: 300px; # content 영역에 해당함
          border-width: 3px; 
          border-style: solid;
          border-color: black;
          padding-bottom: 25xpx;
          padding-left: 25px;
        }
    
    .box2 {
    			width: 300px;
          border: 1px dashed black;
          margin: 25px auto;
          padding: 25px 50px;
        }
    ```
    

### (1) shorthand 속성

- border
    - border-width, border-style 등을 한 번에 설정하기 위한 속성
    - **작성 순서는 영향을 주지 않음**
- margin & padding
    - 4방향의 속성을 각각 지저하지 않고 한번에 지정할 수 있는 속성
    - 4개 : 상우하좌 / 3개 : 상(좌우)하 / 2개 : (상하)(좌우) / 1개 : 공

## 2) box - sizing 속성

- `box-sizing: border-box;` 로 설정해서 작업해야 함
    - border까지 포함해서 width로 치는 것을 의미함

```html
  <style>
    .box {
      width: 100px;
      border: 2px solid black;
      padding: 10px;
      margin: 20px;
      background-color: yellow;
    }

    .content-box {
      /* box-sizing은 기본값이 content-box */
    }

    .border-box {
      /* border까지 포함해서 100px임 */
      box-sizing: border-box;
    }
  </style>
```

## 3) 기타 display 속성

- `inline-block`, `none`

### (1) inline- block

- **새로운 행으로 넘어가지 않음, `span`**
- inline과 block 요소 사이의 중간 지점을 제공하는 display 값
- width, height 속성 사용 가능
- padding, margin, border로 인해 다른 요소가 상자에서 밀려남

```html
span {
  margin: 20px;
  padding: 20px;
  width: 80px;
  height: 50px;
  background-color: lightblue;
  border: 2px solid blue;
  /* display: inline-block; */
}
  
---

<p>Lorem ipsum dolor sit amet <span>consectetur</span> adipisicing elit. Animi iusto enim officia exercitationem
    dolorque, quasi velit, dolores, tempora illum odio necessitatibus. Fugit,
    cumque eligendi!</p>  
```

### (2) none

- 요소를 화면에 표시하지 않고, 공간조차 부여되지 않음
- 랜더링에는 필요한 경우가 있을 수 있으므로 그때 사용함

```html
.none {
	display: none;
}
```

# 2. CSS Position

요소를 normal flow에서 제거하여 다른 위치로 배치하는 것 

다른 요소 위에 올리기, 화면의 특정 위치에 고정시키기 등

## 1) Position 유형

이동 방향 : 3차원으로 있음

- static(정적)
    - 디폴트 값임
- relative(상대)
    - 왼쪽 상단 꼭짓점이 기준임
    - 본인 공간을 유지한 상태로 요소만 이동함
- absolute(절대)
    - 내 화면의 왼쪽 상단 꼭짓점이 기준임(부모 중 포시션이 relative가 없다면 화면 기준)
    - 본인 공간을 없앰
    - `position: relative;` 만약에 부모 박스가 포지션이 상대라면, 그 부모를 기준으로 왼쪽 상단 꼭짓점이 기준점이 됨
- fixed(고정)
    - 화면을 스크롤 해도 고정되어 있음
- sticky(끈적끈적?)
    - 본인 부모의 border까지 해당됨

```html
.container {
  position: relative;
  margin: 30px;
  height: 300px;
  width: 300px;
  border: 1px solid black;
}

.box {
  height: 100px;
  width: 100px;
  border: 1px solid black;
}

.static {
  /* position: static; */
  background-color: lightcoral;
}

.absolute {
  position: absolute;
  background-color: lightgreen;
  top: 100px;
  left: 100px;
}

.relative {
	/* 왼쪽 꼭짓점을 기준으로 아래로 100, 오른쪽으로 100 이동함을 의미함 */
  position: relative;
  background-color: lightblue;
  top: 100px;
  left: 100px;
}

.fixed {
  position: fixed;
  background-color: gray;
  top: 0;
  right: 0;
}
</style>
```

## 2) z-index 특징

- static이 아닌 요소에만 적용됨
- 기본값은 auto
- 부모 요소의 z-index 값에 영향을 받음
- 같은 부모 내에서만 z-index 값을 비교
- 부모의 z-index가 낮으면 자식의 z-index가 아무리 높아도 부모보다 위로 올라갈 수 없음
- z-index 값이 같으면 html 문서 순서대로 쌓임

# 3. CSS Flexbox

요소를 행과 열 형태로 배치하는 1차원 레이아웃 방식 → 공간 배열, 정렬

## 1) Flexbox 구성 요소

너비의 길이는 content 기준으로 설정됨, 높이는 부모 클래스의 높이 기준임

### (1) main axis (주 축)

- flex item 들이 배치되는 기본 축
- main start 에서 시작하여 main end 방향으로 배치 (기본값)

### (2) crss axis (교차 축)

- main axis에 수직인 축
- cross start에서 시작하여  cross end 방향으로 배치 (기본 값)


### (3) 실습

```html
flex-direction: row; /* flex-direction은 기본값이 row */
/* flex-direction: column; */ nomal flow처럼 보이는 형태로 바뀜(상->하가 주축으로 바뀜)
/* flex-direction: row-reverse; */
/* flex-direction: column-reverse; */

/* flex-wrap: nowrap; */
/* flex-wrap: wrap; */ 부모 요소 밖으로 튀어나가는 것을 방지하는 것

/* justify-content: flex-start; */
/* justify-content: center; */ 중앙 정렬
/* justify-content: flex-end; */

/* align-content: flex-start; */
/* align-content: center; */ 
/* align-content: flex-end; */

/* align-items: flex-start; 이전엔 부모 크기만큼 다 차지했다면, 위쪽으로 올려져서 배치됨 */
/* align-items: center; 수직 교차 축을 기준으로 중앙 정렬됨*/
/* align-items: flex-end; */
```

## 2) Flexbox 속성

- flex container 관련 속성
    - display, flex-direction, flex-wrap, justify-content, align-items, align-content
- flex item 관련 속성
    - Flex Container의 **직계 자식 요소**들
    - align-self, flex-grow, flex-basis, order
    
    ### (1) flex container
    
    1. display
        
        `display : flex`  주축의 기본값인 가로 방향으로 나열
        
    2. flex-direction
        
        `flex-direction: column` 디폴트는 row임, column으로 지정하면 nomal flow처럼 보이는 형태로 바뀜(상->하가 주축으로 바뀜)

    3. flex-wrap
        
        `flex-wrap: wrap;` 부모 요소 밖으로 튀어나가는 것을 방지하는 것
        
    4. justify-content
        
        `justify-content: center;` 주 축을 따라 flex item과 주위에 공간을 분배 = 중앙 정렬
        
        between : 끝 여백 없이 균등 분배, around : 패딩 있다고 생각하고 균등 분배, evenly : 틈은 모두 같
        
    5. align-content
        
        `align-content: center;` 교차축을 따라 flex item과 주위에 공간을 분배 = 중앙 정렬
      
    6. align-items
        
        `align-items: center;` 교차축을 따라 flex item 행을 정렬 = 중앙 정렬
        
    
    ### (2) flex item
    
    1. align-self
        
        교차 축을 따라 개별 flex item을 정렬
        
    
    ### (3) 속성 분류
    
    - 배치 :  `flex-direction` , `flex-wrap`
    - 공간 분배 : `justify-content` , `align-content`
    - 정렬 : `align-items` , `align-self`
    
    - justivy-items 및 justify-self 속성이 없는 이유 : 필요 없기 때문, margin auto로 가능
    
    ### (4) 기타
    
    - flex-grow
        
    - flex-basis
        
        flex item의 초기 크기 값을 지정, flex-basis와 width 값을 동시에 적용한 경우 flex-basis가 우선
        

# 4. 참고

## 1) 마진 상쇄

두 block 타입 요소의 margin top과 bottom이 만나 더 큰 margin으로 결합되는 현상

- 복잡한 레이아웃에서 요소 간 간격을 일관되게 유지하기 위함
- 요소 간의 간격을 더 예측 가능하고 관리하기 쉽게 만듦

## 2) 박스 타입 별 수평 정렬

- block 요소의 수평 정렬 → `margin: auto` 사용
- inline 요소의 수평 정렬 → `text-align: center` 사용