try:
    with open("rahim.txt", 'r') as f:
        print(f.read())
    print(10/10)
except ZeroDivisionError:
    print("Error: Division by zero is not possible")

except FileNotFoundError:
    print("file not found")
else:
    print("Code Executed Succesfully")

finally:
    print(" finally always printable")

#Custom error
def check_file(filename):
    if not filename.endswith('.txt'):
        raise ValueError(" only .txt files are allowed")
    print("Valid File")


#Custom Error Handling
try:
    check_file('data.csv')
except Exception as er:
    print(er)