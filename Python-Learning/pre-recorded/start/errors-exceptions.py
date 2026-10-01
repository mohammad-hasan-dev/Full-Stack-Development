try:
    with open("rahim.txt", 'r') as f:
        print(f.read())
except FileNotFoundError:
    print("file not found")