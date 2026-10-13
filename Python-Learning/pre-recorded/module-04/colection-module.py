import collections
# print(collections.__doc__)

fruits =['apple', 'Banana','apple','orange']
print(collections.Counter(fruits))
print(collections.Counter(fruits).most_common(2))
