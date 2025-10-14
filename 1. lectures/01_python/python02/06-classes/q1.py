# 단어를 드래그하거나 포커싱을 한다음 `ctrl+D`를 하면 동일한 글자 모두 다중 포커싱 된


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
        super().__init__() # ParentA 클래스의 init 메서드 호출
        self.value_c = 'Child'
    def show_value(self):
        super().show_value() # ParentA 클래스의 show_value 메서드 호출
        print(f'Value from Child: {self.value_c}')

child = Child()
child.show_value() 

# 만약 생성자의 순서를 바꾸면 덮어씌운게 돼서 'ParentA'로만 출력됨
'''
class Child(ParentA, ParentB):
    def __init__(self):
        self.value_a = 'Child'
        super().__init__() # ParentA 클래스의 init 메서드 호출
        
    def show_value(self):
        super().show_value() # ParentA 클래스의 show_value 메서드 호출
        print(f'Value from Child: {self.value_a}')
'''