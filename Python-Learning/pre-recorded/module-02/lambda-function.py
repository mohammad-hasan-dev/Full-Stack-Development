# importing functools for understand ruducing function.
import functools


# Lembda Function is Anonymous Function.


# Normal Function
# def square(x):
#     return x*x
# print(square(5))


#lembda function


# add = lambda x: x*x


# print(add(8))


# student= [('Rahim',60), ('karim',38), ('jhon',98)]
# sorted_stedents = sorted(student, key= lambda x:x[1])


# print(sorted_stedents)






# most usefull function: map (), filter() and ruduce().


# Map
nums =[1,2,3,5,6]
sq_nums =list(map(lambda x: x*x,nums))
print(sq_nums)


#filter


even= list(filter(lambda x: x%2 ==0, nums))
print(even)


# Reduce


sum =functools.reduce(lambda x,y: x+y, nums)
print(sum)

