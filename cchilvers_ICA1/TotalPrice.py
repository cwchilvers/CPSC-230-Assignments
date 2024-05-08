# Chandler Chilvers
# 2311765
# cchilvers@chapman.edu
# 230-06
# Total Price

item = input("Please enter item price: x.xx")
tax = input("Please enter sales tax: x.xx")

# cast vars so we can do math w them

item = float(item)
tax = float(tax)

total_price =  item + (item * tax)

print("Total price is:",total_price)
