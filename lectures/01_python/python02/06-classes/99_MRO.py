# 99_MRO.py
O = object
class D(O) : pass
class E(O) : pass
class F(O) : pass
class B(D, E) : pass
class C(F, D) : pass
class A(B, C) : pass

# A 클래스의 상속 탐색 순서를 출력
print(A.__mro__)