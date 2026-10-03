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


def check_file(filename):
    if not filename.endswith('.txt'):
        raise ValueError(" only .txt files are allowed")
    print("Valid File")


check_file('data.csv')
