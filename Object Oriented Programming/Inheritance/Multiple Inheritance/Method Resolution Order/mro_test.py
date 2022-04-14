

class A(object):
    def method(self):
        print("Class A's method!")
        super().method()

class B(object):
    def method(self):
        print("Class B's method!")
        super().method()

class C(object):
    def method(self):
        print("Class C's method!")

class X(A, B):
    def method(self):
        print("Class X's method!")
        super().method()

class Y(B, C):
    def method(self):
        print("Class Y's method!")
        super().method()

class P(X, Y, C):
    def method(self):
        print("Class P's method!")
        super().method()


p = P()
p.method()
print(P.mro())
# P
# X
# A
# Y
# B
# C

