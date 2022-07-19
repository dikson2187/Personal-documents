'''
class Human:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

class Student(Human):
    def stad (self):
        print(f"{self.name} is studing")



class Worker(Human):
    def work (self):
        print(f"{self.surname} is studing")


class Correspondence (Student, Worker):
    pass
'''

'''
class A:
    def __init__(self):
        print("A")
        super().__init__()
class B(A):
    def __init__(self):
        print("B")
        super().__init__()

class C(A):
    def __init__(self):
        print("C")
        super().__init__()


class D(B, C):
    def __init__(self):
        print("D")
        super().__init__()

d = D()
print(D.mro())
'''

'''
class Complex:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, (int, float)):
            new_x = self.x + other
            new_y = self.y
        else:
            new_x = self.x + other.x
            new_y = self.y + other.y
        return Complex(new_x, new_y)

    def __radd__(self, other):
        return self + other

    def __str__(self) -> str:
        return f"{self.x} + {self.y}i"

c1 = Complex(1, 2)
c2 = Complex(3, 4)
print(2.5 + c2)

'''

'''
class Figure:
    pass



class Crook(Figure):
    def __init__(self, r):
        self.r = r
    def crook(self):
        return self.r  * 3,14



class Square(Figure):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def square(self):
        return self.a * self.b


c1 = Crook(2)
s1 = Square(2, 4)
print(s1.square())
print(c1.crook())
'''

'''
class Radio:
    def __init__(self, sound) -> None:
        self.sound = sound

    def play(self):
        print(self.sound)


class RadioPlayMixin:
    def __init__(self) -> None:
        self.radio = Radio(self.radio_sound)

    def radio_play(self):
        return self.radio.play()

class Clock(RadioPlayMixin):
    def __init__(self, radio_sound):
        self.radio_sound = radio_sound
        super().__init__()
'''

'''
class Pizza:
    INGRIDIENS = "tomat"



    @classmethod
    def maargarita (cls):
        print(cls)
        return cls(**cls.INGRIDIENS)
'''

class Person:
    def __init__(self, name, surname) -> None:
        self.name = name
        self.surname = surname


    @classmethod
    def with_fullname(cls, fullname: str) ->Person:


    @staticmethod
    def is_adult():
    

