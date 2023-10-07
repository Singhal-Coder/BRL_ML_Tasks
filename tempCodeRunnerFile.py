class A:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class B(A):
    def __init__(self, name, age, profession):
        self.profession = profession
        super().__init__(name, age)
    

class C(B):
    def __init__(self):
        pass

class D(B):
    def __init__(self, name):
        self.name = name
    def call(self):
        print(f"{self.name}")

class E(C,D):
    pass

x = E()
x.call()
    
