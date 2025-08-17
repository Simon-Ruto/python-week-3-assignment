def calculate_discount(price, discount_percent):
    discount=discount_percent/100
    if discount >= 0.2:
        return price*(1-discount)
    else:
        return price


original_price=float(input ("Enter original price: "))
discount_percentage=float(input("Enter Discount Percentage: "))
print("Final price :",calculate_discount(price=original_price, discount_percent=discount_percentage))



