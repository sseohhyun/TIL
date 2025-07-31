'''
    super의 역할은 단순히 `나의 부모 클래스`를 호출하는 것이 아닙니다.
    MRO순서상, 다음에 실행되어야 할 클래스를 호출하는 것이 됩니다.
    따라서 아래의 방법 1의 경우, C를 기준으로는 MRO상 C -> A -> B가 되므로,
    C에서 호출한 super는 A를, A에서 호출한 super는 B를 가르키게 됩니다.
    그러나... 이러한 표기 방식은, A를 기준으로 보았을 떄는, super가 가르키는 대상이 모호해 지므로,
    방법 2를 사용할 수 있겠습니다.
        그냥, 내가 쓰고 싶은 클래스의 생성자 함수를 직접 호출하면 되는 것이죠.
'''

class ParentA:
    def __init__(self):
        self.home = 'Busan'
        # 방법 1-2.
        # super().__init__()    # 다시 super를 사용하여 다음 호출 순서의 클래스의 생성자 함수를 호출한다.

class ParentB:
    def __init__(self):
        self.home = 'Daejeon'

class Child(ParentA, ParentB):
    def __init__(self):
        '''
            이러한 경우에, super().__init__() 을 하게 되면
            ParentA의 생성자 함수를 불러와 사용하게 됩니다.
            하지만, 저는 ParentB의 생성자 함수를 사용하여 Child의 생성자 함수를 정의하고 싶습니다.
            이런 경우, 반드시 상속의 순서를 바꿔야만 하나요...?
        '''
        # 방법 1-1.
        # super().__init__()    # ParentA의 생성자를 호출하고,

        # 방법 2. ParentB 클래스의 생성자를 호출하시면 되겠죠?
        ParentB.__init__()