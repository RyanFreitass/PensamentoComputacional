class A:
    def __init__(self):
        print("Construtor A")

class B:
    def __init__(self):
        print("Construtor B")

class C(A, B):
    def __init__(self):
        super().__init__()
        B.__init__(self)
        print("Construtor C")


c = C() 