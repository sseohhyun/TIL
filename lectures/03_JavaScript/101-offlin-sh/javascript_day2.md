# 1. 객체

object : 키로 구분된 데이터 집합을 저장하는 자료

## 1) 구조 및 속성

### (1) 객체 구조

- `{}` 를 이용해 작성
- 중괄호 안에는 `key: value` 쌍으로 구성된 속성을 여러 개 작성 가능
- key는 문자형만 허용, 불변형
- value는 모든 자료형 허용
    
    ```jsx
    const user = {
    	name: "Alice",
    	"key with space": Ture //key 값에 공백이 있는 경우 ""로 사용
    	greeting: function() {
    		return "hello"
    	}
    }	
    ```
    

### (2) 속성 참조

- `점(.)` 또는 `대괄호[]`로 객체 요소 접근
- key 이름에 띄어쓰기 같은 구분자가 있으면 대괄호 접근만 가능
    
    ```jsx
    // 수정
    user.name = 'Bella'
    console.log(user.name) // Bella
    
    // 삭제
    delete user.name
    console.log(user) // {key with space: true, address: 'korea', greeting: ƒ}
    ```
    
- in 연산자 : 속성이 객체에 존재하는지 여부를 확
    
    ```jsx
    console.log('greeting' in user) // true
    console.log('country' in user) // false
    ```
    

---

## 2) 객체와 함수

### (1) Method

- 객체 속성에 정의된 함수 → `this 키워드`를 사용해 객체에 대한 특정한 작업을 수행할 수 있음
- object.method() 방식으로 호출

```jsx
console.log(user.greetion()) // hello
```

---

## 3) this

### (1) this 키워드

- **함수나 메서드를 호출한 객체를 가리키는 키워드**
    
    → 함수 내에서 객체의 속성 및 메서드에 접근하기 위해 사용
    
    ```jsx
    const person = {
          name: 'Alice',
          greeting: function () {
            return `Hello my name is ${this.name}`
          },
        }
    
    console.log(person.greeting()) // Hello my name is Alice
    // person이라는 객체가 greeting이라는 메서드를 호출했기 때문에 this는 person 객체를 가리
    ```
    
- this는 함수를 `호출하는 방법` 에 따라 가리키는 대상이 다
- 단순 호출 → 전역 객체(ex. window)
    
    ```jsx
    const myFunc = function () {
          return this
        }
    console.log(myFunc()) // window
    ```
    
- 가리키는 대상 → 메서드를 호출한 객체
    
    ```jsx
    const myObj = {
          data: 1,
          myFunc: function () {
            return this
          }
        }
    console.log(myObj.myFunc()) // myObj
    ```
    
- 헷갈리는 부분 주의 → **나를 호출한 객체를 보여주는게 this다!**
    
    ```jsx
    const obj = {
    	greeting: function() {
    		console.log(this)
    	}
    }
    
    const gr = obbj.greeting
    
    gr() // window, 단순 호출이었으니까!
    obj.greeting() // obj
    ```
    

### (2) 중첩된 함수에서의 this 문제점과 해결책

- forEach의 인자로 작성된 함수는 단순 호출이기 때문에 this가 전역 객체를 가리킴
    
    (콜백함수는 단순호출임)
    

```jsx
const myObj2 = {
  numbers: [1, 2, 3],
  myFunc: function () {
    this.numbers.forEach(function (number) {
      console.log(this) // window
    })
  }
}
console.log(myObj2.myFunc())
```

- 화살표 함수는 **자신만의 this를 가지지 않기** 때문에 외부 함수에서의 this 값을 가져옴
- 화살표 함수는 나를 호출했을 때 본인이 속해있는 그 곳의 this를 따라가도록 되어있음

```jsx
// 2.2 화살표 함수
const myObj3 = {
  numbers: [1, 2, 3],
  myFunc: function () {
    this.numbers.forEach((number) => {
      console.log(this) // myObj3
    })
  }
}
console.log(myObj3.myFunc())
```

### (3) this 정리

- javascript의 this는 함수가 호출되기 전까지 값이 할당되지 않고 호출 시에 결정
    
    따라서 this가 미리 정해지지 않고 호출 방식에 의해 결정되는 것은 
    (호출하는 시점의 왜 해당하는 객체를 정하는가?)
    
    - 장점 : 함수를 하나만 만들어 여러 객체에서 재사용할 수 있다는 것
    - 단점 : 이런 유연함이 실수로 일어질 수 있다는 것

---

## 4) 추가 객체 문법

### (1) 단축 속성

- 키 이름과 값으로 쓰이는 변수의 이름이 같은 경우 단축 구문을 사용할 수 있음

```jsx
// 1. 단축 속성 적용 전
const name = 'Alice'
const age = 30

const user = {
  name: name,
  age: age
}
```

```jsx
// 2. 단축 속성 적용 후
const name = 'Alice'
const age = 30

const user = {
  name:,
  age:
}
```

### (2) 단축 메서드

- 메서드 선언 시 fuction 키워드 생략 가능

```jsx
// 1. 단축 메서드 적용 전
const myObj1 = {
  myFunc: function () {
    return 'Hello'
  }
}
```

```jsx
// 2. 단축 메서드 적용 후
const myObj2 = {
  myFunc() {
    return 'Hello'
  }
}
```

### (3) 계산된 속성

- 키가 대괄호로 둘러싸여 있는 속성 → 고정된 값이 아닌 변수 값을 사용할 수 있음

```jsx
const product = prompt('물건 이름을 입력해주세요')
const prefix = 'my'
const suffix = 'property'

const bag = {
  [product]: 5,
  [prefix + suffix]: 'value'
}

console.log(bag) // {연필: 5, myproperty: 'value'}
```

### (4) 구조 분해 할당

- 배열 또는 객체를 분해하여 객체 속성을 변수에 쉽게 할당할 수 있는 문법
- 객체가 가지고 있는 속성명과 정의하려는 변수명과 같으면 userInfo.firstName에서 .firstName을 생략 가능

```
const userInfo = {
  firstName: 'Alice',
  userId: 'alice123',
  email: 'alice123@gmail.com'
}

// const firstName = userInfo.firstName
// const userId = userInfo.userId
// const email = userInfo.email

// const { firstName } = userInfo  
// const { firstName, userId } = userInfo
const { firstName, userId, email } = userInfo

// Alice alice123 alice123@gmail.com
console.log(firstName, userId, email)
```

- `함수의 매개변수` 로 객체 구조 분해 할당 활용 가능함

```jsx
const person = {
  name: 'Bob',
  age: 35,
  city: 'London',
}

function printInfo({ name, age, city }) { // 매개변수로 넣을 때는 const 안붙여도 
  console.log(`이름: ${name}, 나이: ${age}, 도시: ${city}`)
}

// 함수 호출 시 객체를 구조 분해하여 함수의 매개변수로 전달
printInfo(person) // '이름: Bob, 나이: 35, 도시: London'
```

### (5) 전개 구문

- 객체 복사
    - 객체 내부에서 객체 전개
- 얕은 복사에 활용 가능

```jsx
const newObj = { a: 1, ...obj, e: 5 }
console.log(newObj) // {a: 1, b: 2, c: 3, d: 4, e: 5}
```

### (6) 유용한 객체 메서드

- object.keys(객체명) / object.values(객체)

### (7) Optional chainng(’?.’)

- 속성이 없는 중첩 객체를 에러 없이 접근할 수 있는 방법
    
    해당 속성에 값이 있거나, 키가 있는지 매번 if문으로 확인하기에는 번거로울 수 있으니까!
    
- 만약 참조 대상이 null 또는 undefined라면 에러가 발생하는 것 대신 평가를 멈추고 undefined를 반환
- 주의사항 : 남용 금지

```jsx
const user = {
  name: 'Alice',
  greeting: function () {
    return 'hello'
  }
}

// console.log(user.address.street) // Uncaught TypeError: Cannot read properties of undefined (reading 'street')
// user라는 객체에 address라는 속성이 있어? 있으면 street에 들어있는 값을 불러와줘 없으면 undefined
console.log(user.address?.street) // undefined

// console.log(user.nonMethod()) // Uncaught TypeError: user.nonMethod is not a function
console.log(user.nonMethod?.()) // undefined

// optional chaining을 사용하지 않는다면 && 연산자를 사용해야 
console.log(user.address && user.address.street) // undefined

console.log(myObj?.address) // Uncaught ReferenceError: myObj is not defined

// 위 예시 코드 논리상 user는 반드시 있어야 하지만 address는 필수 값이 아님
// user에 값을 할당하지 않은 문제가 있을 때 바로 알아낼 수 있어야 하기 때문

// Bad
user?.address?.street

// Good
user.address?.street
```

---

## 5) 참고 (시험x)

### (1)  JSON

- JavaScript Object Notation
- Key - Value 형태로 이루어진 자료 표기법
- JSON은 형식이 있는 문자열, JavaScript에서 JSON을 사용하기 위해서는 Object 자료형으로 변경해야

# 2. 배열

## 1) 배열 정의 및 구조

- 배열 = **object**, 키로 구분된 데이터 집합을 저장하는 자료형()
- length 속성을 사용해 배열에 담긴 요소가 몇 개인지 알 수 있
    
    ```jsx
    const arr = [1,2,3]
    arr.legth = 1
    arr = 1로 출력됨
    ```
    
- for in으로 배열을 순회할 시 순서 보장x → for of로 순회해야 함

---

## 2) 배열 메서드

![image.png](attachment:196bbe06-ccff-4dff-9cf3-0ad23ef53396:image.png)

---

## 3) Array helper method

배열 조작을 보다 쉽게 수행할 수 있는 특별한 메서드 모음

### (1) forEach (반복만을 위)

- 배열 내의 모든 요소 각각에 대해 함수(콜백함수)를 호출, **반환 값 없음**
- 사용 권장, 간결하고 가독성이 높음

![image.png](attachment:8832c632-412f-4c87-87b8-09f73c4e52b1:image.png)

```jsx
		/* 구조 소개
		arr.forEach(function (item, index, array) {
			//do something
		})
		*/
		
		const names = ["Alice", "Bella", "Cathy"]
		
		// 일반 함수 표시
		names.forEach(function (name) {
			console.log(name)
		})
		
		// 화살표 함수 표기
		names.forEach((name) => {
			console.log(name)
		})
```

### (2) map()

- 배열의 모든 요소에 대해 함수를 호출하고, 반환 된 호출 값을 모아 **새로운 배열을 반환**
- map 메서드에 callbackfunc 함수를 인자로 넘겨 numbers 배열의 각 요소를 callbackfunc 함수의 인자로 사용하였음

![image.png](attachment:c9339e0e-e269-4ab7-95e1-73ebc9d3282e:image.png)

```jsx
/* 구조 소개
const newArr = array.map(function (item, index, array) {
	// do something
})
*/

// 2. 화살표 함수 표기
const names = ['Alice', 'Bella', 'Cathy']

const result3 = names.map(function (name) {
  return name.length
})

const result4 = names.map((name) => {
  return name.length
})

console.log(result3) // [5, 5, 5]
console.log(result4) // [5, 5, 5]
```

### (3) filter

- 콜백 함수의 반환 값이 참인 요소들만 모아서 새로운 배열을 반환
- 참인 요소들을 모두 반환

### (4) find

- 콜백 함수의 반환 값이 참이면 해당 요소를 반환
- 찾아나가다가 한 개를 찾으면 그 한 개를 반환하고 끝임

# 3. 비동기

## 1) 동기

- 프로그램의 실행 흐름이 순차적으로 진행 → 하나의 작업이 완료된 후에 다음 작업이 실행되는 방식

## 2) 비동기

- 프로그램의 실행 흐름이 순차적이지 않으며, 작업이 완료되기를 기다리지 않고 다음 작업이 실행되는 방식 → **작업의 완료 여부를 신경 쓰지 않고 동시에 다른 작업들을 수행**할 수 있음
- 예시
    
    ```jsx
    const slowRequest = function (callBack) {
        console.log('1. 오래 걸리는 작업 시작 ...')
        setTimeout(function () {
          callBack()
        }, 3000)
      }
    
    const myCallBack = function () {
        console.log('2. 콜백함수 실행됨')
      }
    
    slowRequest(myCallBack)
    
    console.log('3. 다른 작업 실행')
    
    // 출력결과
    // 1. 오래 걸리는 작업 시작 ...
    // 3. 다른 작업 실행
    // 2. 콜백함수 실행됨
    ```
    
- 병렬적 수행
- 당장 처리를 완료할 수 없고 시간이 필요한 작업들은 별도로 요청을 보낸 뒤 응답이 빨리 오는 작업부터 처리

## 3) JavaScript와 비동기

- Thread란? 작업을 처리할 때 실제로 작업을 수행하는 주체로 multi-thread라면 업무를 수행할 수 있는 주체가 여러 개라는 의미
- JavaScript는 한 번에 하나의 일만 수행할 수 있는 single thread 언어로 동시에 여러 작업을 처리할 수 없음 → 하나의 작업을 요청한 순서대로 처리할 수 밖에 없음
- call stack → web api(작업위치) → task queue → event loop
    
    ![image.png](attachment:6fa71a53-8059-46bf-8570-f6e100521a16:image.png)
    
    - 요청이 들어오면 작업위치로 보내고 작업이 끝나는 대로 task로 넘김 이때 call이 비어있다면 event가 call로 들여보내
    - 비동기로 movie, actor, ganre 를 보냈다면 뭐가 먼저 나올 지 알 수 없음 → 그냥 먼저 끝나는게 빠져나와서 task 들어가고 call에 다시 가서 출력을 하니

# 4. AJAX

## 1) AJAX 의 정의 및 목적

### (1) AJAX 정의

- 복잡하고 동적인 웹 페이지를 구성하는 프로그래밍 방식
- 브라우저와 서버 간의 데이터를 비동기적으로 교환하는 기

### (2) AJAX 목적

- 전체 페이지가 다시 로드되지 않고 HTML 페이지 일부 DOM만 업데이트
    
    → 웹 페이지 일부가 다시 로드되는 동안에도 코드가 계속 실행되어, 비동기식으로 작업할 수 있음
    

### (3) XMLHttpRequest 객체

- 서버와 상호작용할 때 사용하는 객체
- 브라우저와 서버 간의 네트워크 요청을 전송할 수 있음
- 이름에 xml이라는 데이터 타입이 들어가긴 하지만 xml 뿐만 아니라 모든 종류의 데이터를 가져올 수 있음

## 1) XHR

### (1) XHR 구조

- HTTP 요청을 생성하고 전송하는 기능을 제공
- AJAX 요청을 통해 서버에서 데이터를 가져와 웹 페이지에 동적으로 표시
    
    ```jsx
    const xhr = new XMLHttpRequest() // XHR 객체 인스턴스 생성
    xhr.open('GET', 'https://jsonplaceholder.typicode.com/posts')
    xhr.send() // 요청 전송
    
    xhr.onload = function () {  // 요청이 완료되었을 때 호출
      // 응답 상태 코드가 200이라면
      if (xhr.status == 200) {
        console.log(xhr.responseText)  // 응답 받은 결과 출력
      } else {
        console.error('Request failed')  // 200 이외 상태에 대한 예외 처리
      }
    }
    ```
    

### (2) 기존 기술과의 차이 - AJAX

- 클라이언트에서 form을 채우고 이를 서버로 제출(submit) → 서버는 요청 내용에 따라 데이터 처리 ㅎ ㅜ새로운 웹페이지를 작성하여 응답으로 전달
- XHR 객체 생성 및 요청
- 서버는 새로운 페이지를 응답으로 만들지 않고 필요한 부분에 대한 데이터만 처리 후 응답
    - 필요한 부분의 데이터만 받아 기존 페이지의 일부를 수정 (새로고침 X)
    - 서버에서 모두 처리되던 데이터 처리의 일부분이 이제는 클라이언트 쪽에서 처리되므로 교환되는 데이터량과 처리량이 줄어듦

### (3) 이벤트 핸들러와의 유사성

- 이벤트 핸들러는 비동기 프로그래밍의 한 형태임
- 이벤트가 발생할 때마다 호출되는 함수(콜백 함수)를 제공하는 것
- HTTP 요청은 응답이 올때까지의 시간이 걸릴 수 있는 작업이라 비동기임, 이벤트 핸들러는 XHR 객체에 연결해 요청의 진행 상태 및 최종 완료에 대한 응답을 받

# 5. 기타

## 1) CallbackPromise

### (1) 비동기 처리의 단점

- Web API로 들어오는 순서가 아니라 작업이 완료되는 순서에 따라 처리함
- 개발자 입장에서는 코드의 실행 순서가 불명확하다는 단점이 존재함
- 실행 결과를 예상하면서 코드를 작성할 수 없게 함 → 콜백 함수를 사용

### (2) 비동기 콜백

- 비동기적으로 처리되는 작업이 완료되었을 때 실행되는 함수
- 연쇄적으로 발생하는 비동기 작업을 **순차적으로 동작**할 수 있게 함

```jsx
const asyncTask = function (callback) {
  setTimeout(function () {
    console.log('비동기 작업 완료')
    callback() // 작업 완료 후 콜백 호출
  }, 2000) // 1초 후에 작업 완료
}
// 비동기 작업 수행 후 콜백 실행
asyncTask(function () {
  console.log('작업 완료 후 콜백 실행')
})
```

### (3) 비동기 콜백의 한계

- 콜백 지옥 발생 → 가독성을 헤치고 유지 보수가 어려워
    
    ![image.png](attachment:575e150e-d3aa-4d15-9d66-4a5467df599b:image.png)
    

### (4) Promis object

- 비동기 작업이 완료되었을 때 결과 값을 반환하거나, 실패 시 에러를 처리할 수 있는 기능을 제공
- then 메서드를 이요하여 추가한 경우에도 호출 순서를 보장하며 동작
- **성공에 대한 약속 then() / 실패에 대한 약속 cath()**
    
    ```jsx
    const fetchData = () => {
      return new Promise((resolve, reject) => {
          const xhr = new XMLHttpRequest()
          xhr.open('GET', 'https://api.thecatapi.com/v1/images/search')
          xhr.send()
      })
    }
    const promiseObj = fetchData()
    console.log(promiseObj) // Promise object
    ```
    
    ![image.png](attachment:c6c9cfe5-96e4-42fd-b6e9-b32cefed7f9e:image.png)
    
- then 메서드 chaining의 목적 : 비동기 작업의 `순차적인` 처리 가능
    - 가독성, 에러 처리, 유연성, 코드 관리 등의 용이함

## 2) Axios

- JavaScript에서 사용되는 HTTP 클라이언트 라이브러리
- XHR 객체를 생성해서

```jsx
  <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
  <script>
    // 1.
    const promiseObj = axios({
      method: 'get',
      url: 'https://api.thecatapi.com/v1/images/search'
    })

    console.log(promiseObj) // Promise object

    promiseObj.then((response) => { // 응답해준 결과물을 response 객체에 담김
      console.log(response) // Response object
      console.log(response.data)  // Response data
    })

    // 2. 1보다 2 방법을 주로 사용
    axios({
      method: 'get',
      url: 'https://api.thecatapi.com/v1/images/search'
    })
      .then((response) => {
        console.log(response)
        console.log(response.data)
      })
  </script>
```

## 3) 암묵적 형변환

```jsx
"3" + 3 // '33'
3 + "3" // '33' 문자열 + 숫자 → 문자열 결합
"2" - 1 // 1
```

## 4) negative indexing

```jsx
const = [1,2,3]
arr[-1] = 4 // [1,2,3,-1:4] : 배열은 객체이므로
```