# file = open('name.txt', 'r')


# content =file.read()
# print(content)


# file.close()


with open('name.txt', 'r') as f:
    content= f.read()
    print(content)


