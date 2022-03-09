class time:
    def __init__(self,h,m,s):
        self._h1=h
        self._m1=m
        self._s1=s
        def sum(self,A1):
            sum1=(self._h1)+(A1._h1)
            sum2=(self._m1)+(A1._m1)
            sum3=(self._s1)+(A1._s1)
            if (sum3>60):
                sum3=sum3-60
                sum2=sum2+1
            if (sum2>60):
                sum2=sum2-60
                sum1=sum1+1
            print("sum1","sum2","sum3")

print("time 1")
h=int(input("enter the hour"))
m=int(input("enter the minute"))
s=int(input("enter the second"))
obj1=time(h,m,s)
print("time 2")
h=int(input("enter the hour"))
m=int(input("enter the minute"))
s=int(input("enter the second"))
obj2 =time(h,m,s)
print("sum of two times")
obj1+obj2







