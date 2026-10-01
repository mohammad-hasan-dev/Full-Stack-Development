try:
    with open("rahim.txt", 'r') as f:
        print(f.read())
    print(10/0)
except ZeroDivisionError:
    print("Error: Division by zero is not possible")

except FileNotFoundError:
    print("file not found")

