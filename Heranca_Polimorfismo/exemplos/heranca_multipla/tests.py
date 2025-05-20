class A:
    def falar(self):
        print("A fala")

class B:
    def gritar(self):
        print("B grita")

class C(A, B):
    pass

c = C() 
c.falar()  # A fala
c.gritar()  # B grita
