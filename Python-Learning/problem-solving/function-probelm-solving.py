# ==========================================
# 1.Square Number
# ==========================================

#
# Create a function called square() that:

# Takes one number.
# Calculates its square.
# Returns the result.
# Print the result outside the function.

# Example:
# Input: 6
# Expected output: 36

# Here is the Solution ----->

# def square(number):
#     result  = number**2
#     return result

# num = int(input("Enter your number: "))

# res= square(num)

# print(res)


# ==========================================
# 2. Calculate Average
# ==========================================


# Write a function called calculate_average() that:

# Takes 3 numbers as arguments.
# Calculates their average.
# Returns the average.
# Print the result outside the function.

# Example:

# Enter first number: 10
# Enter second number: 20
# Enter third number: 30

# Average: 20.0


# Here is the Solution ----->


# a = float(input("Enter You first Number : "))
# b = float(input("Enter You second Number : ")) 
# c = float(input("Enter You third Number : "))

# def calculate_average(a,b,c):
#    total = a+b+c
#    average =total/3
#    return average

# result =calculate_average(a,b,c)

# print(result)



# ==========================================
# 3. Expense Calculator
# ==========================================


# Create a function called calculate_balance() that:

# Takes balance, amount, and transaction_type as arguments.
# If transaction_type is "income", add the amount to the balance.
# If transaction_type is "expense", subtract the amount from the balance.
# Return the new balance.
# If the transaction type is invalid, return "Invalid transaction".

# Example 1:

# Balance: 1000
# Amount: 250
# Type: expense

# New balance: 750

# Here is the Solution ----->


def calculate_balance(balance, amount, transaction_type):

    if transaction_type == "income":
        balance = balance + amount
        return balance

    elif transaction_type == "expense":
        balance = balance - amount
        return balance

    else:
        return "Invalid transaction"


balance = 1000


transaction_type = input("Enter income or expense: ")

amount = float(input("Enter amount: "))

result = calculate_balance(balance, amount, transaction_type)

print("Result:", result)