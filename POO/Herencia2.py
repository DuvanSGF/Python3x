"""
La herencia puede ser tambien indirecta. Una
clase hereda de otra, y esa clase puede a su vez
heredar de una tercera clase.
"""

class A:
    def method(self):
        print("A method")

class B(A):
    def another_method(self):
        print("B method")

class C(B):
    def third_method(self):
        print("C method ")

c = C()
c.method()
c.another_method()
c.third_method()

# No es posible la herencia circular

