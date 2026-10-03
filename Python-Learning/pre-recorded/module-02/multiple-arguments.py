def  addition( *args):
    return sum(args)


a= addition(int(input("Enter first Number: ")))
b= addition(int(input("Enter second Number: ")))
c= addition(int(input("Enter third Number: ")))
d= addition(int(input("Enter fourth Number: ")))


res = a+b+c
print(res)
