# function is typed
# 1. User defined function ---> my own custom function
# 2. built in function ---> defult function
# common built in function name:  print(), input(), sum ()
print ("Hello")
input("Enter your Name : ")




def numbers():
    a= int(input("Enter your 1st Number : "))
    b= int(input("Enter your 2nd Number : "))
    print(a+b)


numbers()


def add_numbers(a,b): #arguments
    print(a+b)


add_numbers(5,10) #perametars
