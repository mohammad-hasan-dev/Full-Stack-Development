a= [1,23,4, 'hello', 'world', 5, 6, 7, 8, 9]

# list mutable

a [0] = 100

print(a)
print (a[-2])
print(len(a))

s = "hello, world"

print(list(s))

a.append([10, 11, 12])
print(a)

print(a.index(23)) #for identify index  number

# tuple immutable

t = (1,2,3,4,5,6,7,8,9)
tr= tuple (reversed(t))
print(t)
print(tr)


