# a =[1,2,3,5,6,7,8]
# res= 0
# i = 0
# n =len(a)
# while i<n:
#     res =res +a [i]
#     i+=1

# print(res)

a = [-10, 2,9, 4,-5,-8]

i=0
while i<len(a):
    if a[i]<0:
        a[i]=0
    i+=1

print(a)