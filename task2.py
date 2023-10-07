class A:
    def __init__(self, name, age, profession):
        self.name = name
        self.age = age
        self.profession = profession
    

class B(A):
    def call_name(self):
        print(self.name)

class C(B):
    def __init__(self):
        pass
    def get_age(self):
        print(self.age)

class D(B):
    def __init__(self, gender):
        self.gender = gender
    def get_gender(self):
        print(f"{self.gender}")

class E(D,C):
    def __init__(self, name, age, gender, profession, income):
        self.income = income
        super().__init__(gender)
        B.__init__(self, name, age, profession)
        

a = A("Vishal", 19, "CEO")
b = B("Vansh", 19, "Writer")
c = C()
d = D('Female')
e = E("Vaibhav", 19, "Male", "CEO", "99999999999999999999")
print("\nFor class B")
b.call_name()
print("\nFor class C")
c.name = "Akshita"
c.age = 19
c.call_name()
c.get_age()
print("\nFor class D")
d.get_gender()
print("\nFor class E")
e.call_name()
e.get_age()
e.get_gender()