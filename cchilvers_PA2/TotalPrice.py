# Chandler Chilvers
# 2311765
# cchilvers@chapman.edu
# 230-06
# Total Price


# ask for item value

item = input("Please enter item price: x.xx")


# cast

item = float(item)



# cast item

item = float(item)


# check value of item

if item < 0:
    print("Invalid value")

else:
    # ask for tax value

    tax = input("Please enter sales tax: x.xx")

    # cast tax

    tax = float(tax)

    # check value of tax

    if tax < 0:
        print("Invalid value")
    
    else:

        # calculate
    
        total_price =  item + (item * tax)

        #print results

        print("Total price is:",total_price)
