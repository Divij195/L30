class class1:
    __x=50
    def __method(self):
        print("private method")

    def fun1(self):
        print("private variable:", class1.__x)


obj1=class1()
obj1.fun1()
obj1.__method()         
