#1
'''
def gh(x,y,z):
    a=[]
    if x not in a:
        a.append(x)
    elif y not in a:
        a.append(y)
    elif z not in a:
        a.append(z)
    return a
print(gh({1:3,33:5,12:4,2:5,6:7},{1:4,33:5,12:4,5:5,6:7},{1:3,3:5,12:4,2:5,9:7}))
'''
#2
'''
class Shop:
    def __init__(self,name,description,len,price):
        self.name=name
        self.disc=description
        self.len=len
        self.price=price
    def summa(self):
        a=int(self.len*self.price)
        return f'{a} сум'
    def name_(self):
        return f'название {self.name},{self.disc},{self.len},{self.price}'
    
if __name__=='__main__':
    d=Shop('Macbook','777\9',10,1000)
    print(d.summa())
    print(d.name_())
'''
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
    