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
