class Complex:
    def __init__(self, rel=0, imaginary=0):
        self.rel = rel
        self.imaginary = imaginary
    
    def __str__(self):
        if self.rel == 0:
            return f"{self.imaginary}i"
        return f"{self.rel} + {self.imaginary}i" if self.imaginary>=0 else f"{self.rel} - {-self.imaginary}i"

    #  Getter and Setter Starts
    
    @property
    def rel(self):
        return self._rel
    @rel.setter
    def rel(self, rel):
        if type(rel) not in [int, float]:
            raise ValueError("Invalid entry.")
        self._rel = rel
    
    @property
    def imaginary(self):
        return self._imaginary
    @imaginary.setter
    def imaginary(self, imaginary):
        if type(imaginary) not in [int, float]:
            raise ValueError("Invalid entry.")
        self._imaginary = imaginary

    #    Getter and Setter ends


    def conjugate(self):
        return Complex(self.rel, -self.imaginary)

    def modulus(self):
        return (self.rel**2 + self.imaginary**2)**0.5
    
    def multiplicativeInverse(self):
        if self.modulus()==0:
            raise ZeroDivisionError("Can't find Multiplicative Inverse of {}.".format(self.__str__()))
        return Complex(self.rel/(self.rel**2 + self.imaginary**2), -self.imaginary/(self.rel**2 + self.imaginary**2))

    def add(self, *others):
        for i in others:
            try:
                self.rel+=i.rel
                self.imaginary+=i.imaginary
            except AttributeError:
                pass

    def subtract(self, *others):
        for i in others:
            try:
                self.rel-=i.rel
                self.imaginary-=i.imaginary
            except AttributeError: 
                pass 

    def multiply(self, *others):
        for i in others:
            try:
                self.rel, self.imaginary = (self.rel*i.rel - self.imaginary*i.imaginary), (self.rel*i.imaginary + self.imaginary*i.rel)
            except AttributeError:
                pass
 
    def divide(self, *others):
        for i in others:
            try:
                try:
                    i = i.multiplicativeInverse()
                except ZeroDivisionError:
                    raise ZeroDivisionError("Can't divide {} with zero.".format(self.__str__()))
                else:
                    self.multiply(i)
            except AttributeError:
                pass

    def isequal(self, other):
        try:
            return ((self.rel == other.rel) and (self.imaginary==other.imaginary))
        except AttributeError:
            raise ValueError(f"{other} is not a complex instance.")

    def __eq__(self, other):
        return self.isequal(other)

    def __nq__(self, other):
        return not self.isequal(other)

    @classmethod
    def Re(cls, _complex_):
        if isinstance(_complex_, Complex):
            return _complex_.rel
        else:
            return None
    @classmethod
    def Im(cls, _complex_):
        if isinstance(_complex_, Complex):
            return _complex_.imaginary
        else:
            return None
    @classmethod
    def get_add(cls, *others):
        x = y = 0
        for i in others:
            try:
                x+=i.rel
                y+=i.imaginary  
            except AttributeError:
                pass
        return Complex(x, y)  
    
    def __add__(self, other):
        if not isinstance(other, Complex):
            raise ValueError(f"{other} is not complex instance.")
        return Complex.get_add(self, other)

    @classmethod
    def get_subtract(cls, *others):
        x = y =0
        flag = 0
        for i in others:
            if flag==0 and isinstance(i,Complex):
                x, y = i.rel, i.imaginary
                flag = 1
                continue
            try:
                x-=i.rel
                y-=i.imaginary  
            except AttributeError:
                pass
        return Complex(x, y)

    def __sub__(self, other):
        if not isinstance(other, Complex):
            raise ValueError(f"{other} is not complex instance.")
        return Complex.get_subtract(self, other)

    @classmethod
    def get_multiply(cls, *others):
        x, y = 1, 0
        for i in others:
            try:
                x, y = (x*i.rel - y*i.imaginary), (x*i.imaginary + y*i.rel)
            except AttributeError:
                pass
        return Complex(x, y)
    
    def __mul__(self, other):
        if not isinstance(other, Complex):
            raise ValueError(f"{other} is not complex instance.")
        return Complex.get_multiply(self, other)
        
    @classmethod
    def get_divide(cls, *others):
        x, y = 1, 0
        flag = 0
        for i in others:
            if flag==0 and isinstance(i,Complex):
                x, y = i.rel, i.imaginary
                flag = 1
                continue
            try:
                try:
                    i = i.multiplicativeInverse()
                except ZeroDivisionError:
                    raise ZeroDivisionError("Can't divide with 0.")
                else:
                    x, y = (x*i.rel - y*i.imaginary), (x*i.imaginary + y*i.rel)
            except AttributeError:
                pass
        return Complex(x, y)

    def __truediv__(self, other):
        if not isinstance(other, Complex):
            raise ValueError(f"{other} is not complex instance.")
        return Complex.get_divide(self, other)