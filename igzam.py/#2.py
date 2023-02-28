#3
class Square:
    def __init__(self,a):
        self.a=a

    def PS(self):
        return 'Square',(self.a)*4,(self.a**2)
class Rect(Square):
    def __init__(self,a,b):
        super().__init__(a)
        self.b=b

    def PS2(self):
        return 'Rectangle', ((self.a+self.b)*2),(self.a*self.b)
class Triengle(Rect):
    def __init__(self,a,b,c):
        super().__init__(a,b)
        self.c=c
    def PS3(self):
        return 'triengle',(self.a+self.b+self.c),(self.a*self.b/2)
    
    @staticmethod
    def check(a,b,c):
        if a==b:
            return 'a и b равны'
        else:
            return 'a и b не равны'
main=Square(4)
print(main.PS())
main_2=Rect(4,3)
print(main_2.PS2())
main_3=Triengle(4,3,5)
print(main_3.PS3())
print(main_3.check(4,3,5))
    