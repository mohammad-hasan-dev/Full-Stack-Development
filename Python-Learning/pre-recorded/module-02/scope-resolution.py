# scoping
x= 10 # global veriable


def func():
    y=19 #local veriable
    print("y",y)


func()




#LEGB --> veriable scoping


#L = Local veriable
#E = Enclosing  veriable
#G = Global  veriable
#B = Built in scope --> its an defult scope


n = "global" #global veriable




def outer():
    n="" #Enclosing veriable
    def inner():
        n="" #local veriable
        print(n)
