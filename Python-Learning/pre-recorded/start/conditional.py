#if else
name = input("please enter your name: ")
product_name1 = input("Please enter 1st product name: ")
product_price1 = int(input("Please enter 1st product price: "))
product_name2 = input("Please enter 2nd product name: ")
product_price2 = int(input("Please enter 2nd product price: "))
product_name3 = input("Please enter 3rd product name: ")
product_price3 = int(input("Please enter 3rd product price: "))
subtotal = product_price1 + product_price2 + product_price3



if subtotal >= 5000:
    discount = 0.20
elif subtotal >= 3000:
    discount = 0.10
elif subtotal >= 1000:
    discount = 0.05
else:
    discount = 0

discount_amount = subtotal * discount
final_total = subtotal - discount_amount


print("Customer Name:", name.title(), "Product 1:", product_name1.title(), "Price:", product_price1, "Product 2:", product_name2.title(), "Price:", product_price2, "Product 3:", product_name3.title(), "Price:", product_price3, "Subtotal:", subtotal, "Discount:", discount_amount, "Final Total:", final_total)

