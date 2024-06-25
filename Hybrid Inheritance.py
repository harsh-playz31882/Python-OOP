class A:
    pass
class B:
    pass
class C:
    pass
class X(A,B,C):
    pass
class Y(B, C):
    pass
class P(X,Y):
    pass

print(P.mro())