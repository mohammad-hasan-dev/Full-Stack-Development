def my_func(*args, **kwargs):
    print(f"My Name is {kwargs['f_name']} {kwargs['l_name']}. I am {kwargs['age']} years old.")
    print("My other data:", args)


my_func(89, 90, "tuple", age=29, f_name="Mohammad", l_name="Hasan",)




