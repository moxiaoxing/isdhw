class SH:                         #定义形状类
    def __init__(self,x,y):       #构造函数
        self.x=x
        self.y=y
    def area(self):               #定义空的面积方法
        pass
    
class Ellipse(SH):                #定义椭圆类，继承形状类
    def __init__(self,a,b):
        SH.__init__(self,a,b)
    def area(self):
        return 3.14*self.x*self.y

class Square(SH):                 #定义正方形类，继承形状类
    def __init__(self,a):
        SH.__init__(self,a,0)
    def area(self):
        return self.x*self.x

class Rectangle(SH):              #定义长方形类，继承形状类
    def __init__(self,a,b):
        SH.__init__(self,a,b)
    def area(self):
        return self.x*self.y
    
class Circle(SH):                 #定义圆类，继承形状类
    def __init__(self,r):
        SH.__init__(self,r,0)
    def area(self):
        return 3.14*self.x*self.x

def compute_area(x):              #定义compute_area函数，用于求面积之和
    n=len(x)
    i=len(x)-1
    s=0
    while(i>=0):
        s+=x[i].area()        
        i=i-1
    return s
    
        
        
