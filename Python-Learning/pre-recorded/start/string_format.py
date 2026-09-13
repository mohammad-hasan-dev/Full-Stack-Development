age = 25
f_name = "John"
l_name = "Doe"

txt= "My name is {1} {0} and I am {2} years old.".format(l_name, f_name, age) #long format method with index numbers

txt2= f"My name is {f_name} {l_name} and I am {age} years old." #f-string method (short format method)
print(txt) 
print(txt2)