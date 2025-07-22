# 1. 객체

클랙스에서 정의한 것을 토대로 메모리에 할당된 것 `속성` 과 `행동` 으로 구성된 모든 것

## 1) 클래스와 객체

- 어떤 클래스의 인스턴스인지 언급할 필요가 있음 (”아이유는 인스턴스다” 보단 “아이유는 가수의 인스턴스다”가 더 적합함)
- “”.upper() 가 가능함, “”는 str 객체이므로

# 2. 클래스

파이썬에서 타입을 표현하는 방법 = 객체를 생성하기 위한 설계도

## 1) 클래스의 정의

- 클래스 이름은 파스칼 케이스 방식으로 작성 (MyClass)

```python
# 클래스 정의
class Person:
    blood_color = 'red'
    def __init__(self, name):
        self.name = name
    def singing(self):
        return f'{self.name}가 노래합니다.'

# 인스턴스 생성
singer1 = Person('iu')
# 메서드 호출
print(singer1.singing())  
# 속성(변수) 접근
print(singer1.blood_color)
```

### (1) 생성자 함수

- 객체를 생성할 때 자동으로 호출되는 특별한 메서드
- __init__메서드로 정의되며, 객체 초기화를 담당
- 생성자 함수를 통해 인스턴스를 생성하고 필요한 초기값을 설정
- `self` : 생성하려고 하는 인스턴스 그 자체

### (2) 인스턴스, 클래스 변수

- `인스턴스 변수` : 인스턴스마다 별도로 유지되는 변수
    - `self.name = name`
- `클래스 변수` : 클래스 내부에 선언된 변수
    - `blood_color = 'red'`
    - 클래스에서 동일하게 사용하고 싶은 값(변수) 일 경우 사용
    - 클래스 변수를 변경하고 싶을 때
        - 클래스명.변수 = 변경하고 싶은 값
        - 인스턴스 변수 변경 → 인스턴스명.변수명 = 변경하고 싶은 값

## 2) 메서드

인스턴스 메서드, 클래스 메서드, 정적 메서드가 있음

### (1) 인스턴스 메서드

### (2) 클래스 메서드

- 클래스가 호출하는 메서드, `@Classmethod` 데코레이터를 사용하여 정의
- 호출 시, 첫 번째 인자로 해당 메서드를 호출하는 클래스가 전달됨
- 클래스 변수에 접근해서 공통값 관리 가능

```python
# 클래스 메서드
class Person:
    count = 0
    def __init__(self, name):
        self.name = name
        Person.count += 1
    @classmethod
    def number_of_population(cls):
        print(f'인구수는 {cls.count}입니다.')

person1 = Person('iu')
person2 = Person('BTS') 
print(Person.count) #2
```

### (3) 정적 메서드

- 클래스와 인스턴스와 상관없이 독립적으로 동작하는 메서드
    - 클래스가 가지고 있는 속성, 인스턴스 메서드에 접근할 필요는 없지만,
- `@staticmethod` 데코레이터를 사용해서 정의
- 호출 시 필수적으로 작성해야 할 매개변수가 없음
- 인스턴스도 안 만들고, 클래스 속성도 안 쓰고, 그냥 도구로 쓰는 함수

```python
class MathHelper:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def is_even(n):
        return n % 2 == 0
        
print(MathHelper.add(3, 5))    # 👉 8
print(MathHelper.is_even(10))  # 👉 True
```

### (4) 인스턴스와 클래스 간의 이름 공간

- 클래스를 정의하면, 클래스에 해당하는 이름 공간 생성
- 인스턴스를 만들면, 인스턴스 객체가 생성되고 독립적인 이름 공간 생성
- 인스턴스에서 특정 속성에 접근하면, 인스턴스 → 클래스 순으로 탐

# 3. 상속

- 부모 클래스의 메스드를 상속받아서 따로 정의하지 않더라도 함수를 호출해서 사용 가능함
- 자식 이기는 부모 없음

## 1) 다중 상속

- 둘 이상의 상위 클래스로부터 여러 행동이나 특징을 상속받을 수 있는 것

```python
# 다중 상속 예시
class Person:
    def __init__(self, name):
        self.name = name
    def greeting(self):
        return f'안녕, {self.name}'
class Mom(Person):
    gene = 'XX'
    def swim(self):
        return '엄마가 수영'
class Dad(Person):
    gene = 'XY'
    def walk(self):
        return '아빠가 걷기'

class FirstChild(Dad, Mom):
    def swim(self):
        return '첫째가 수영'
    def cry(self):
        return '첫째가 응애'

baby1 = FirstChild('아가')
print(baby1.cry())  # 첫째가 응애
print(baby1.swim())  # 첫째가 수영
print(baby1.walk())  # 아빠가 걷기
print(baby1.gene)  # XY Dad 먼저 상속 받았으므로 우선순위가 dad에 있

```

- print(baby1.gene)  # XY 인 이유
    - `MRO`
        - 부모 클래스로부터 상속된 속성들의 검색을 C3 선형화 규칙에 맞춰 진행


## 2) super()

- 부모 클래스의 메서드를 호출하기 위해 사용하는 내장 함수
- 부모 클래스의 생성자 함수를 가져와서 추가 혹은 수정을 하고 싶은 경우

```python
# 다중 상속
class ParentA:
    def __init__(self):
        self.value_a = 'ParentA'
    def show_value(self):
        print(f'Value from ParentA: {self.value_a}')
class ParentB:
    def __init__(self):
        self.value_b = 'ParentB'
    def show_value(self):
        print(f'Value from ParentB: {self.value_b}')

class Child(ParentA, ParentB):
    def __init__(self):
        super().__init__() # ParentA 클래스의 __init__ 메서드 호출
        self.value_c = 'Child'
    def show_value(self):
        super().show_value() # ParentA 클래스의 show_value 메서드 호출
        print(f'Value from Child: {self.value_c}')

```

# 4. 참고

## 1) 매직 메서드

- 인스턴스 메서드, 특정 상황에 자동으로 호출되는 메서드
- __lt__ = less than
- __str__

## 2) 데코레이터

- 함수 안에 함수를 정의함

## 3) 제너레이터

- 이터레이터(Iterator) : 반복 가능한 객체의 요소를 하나씩 반환하는 객체
- 제너레이터 : 이터레이터를 간단하게 만드는 함수

- 한번에 한 개의 값만 생성 / 대용량 데이터 처리 / 무한 시퀀스 처리
- `yield` 문을 사용하여 값을 반환
    
    ```python
    def generate_numbers():
        for i in range(3):
            yield i
    
    for number in generate_numbers():
        print(number)  # 0 1 2
    ```
    

- 제너레이터를 사용하는 경우
    - 파일에서 한 줄씩 읽어와 처리
    - 메모리에 전체 파일을 로드하지 않고 한 줄씩 처리하여 메모리 사용 절약
    
    ```python
    # 대용량 데이터 처리 
    def read_large_file_with_generator(file_path):
        with open(file_path, 'r') as file:
            for line in file:
                yield line.strip()
    # 예제 파일 경로
    file_path = 'large_data_file.txt'
    # 제너레이터 사용하여 파일 읽기 및 처리
    for line in read_large_file_with_generator(file_path):
        print(line)
    ```
