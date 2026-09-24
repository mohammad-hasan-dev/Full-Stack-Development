a= [1,3,6,4,8,10,12]


# result= []

# for i in a:
#     if i %2 == 0:
#         result.append(i)

# print(result)

#List comprehension
new_result = [i for i in a if i%2==0 ]
print(new_result)


b = [1,2,4,8,10]

b_result = [i**2 if i%2==0 else i for i in b]

print(b_result)