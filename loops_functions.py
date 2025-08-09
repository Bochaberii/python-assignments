def calculate_discount(price, discount_percent):
    if discount_percent  >= 0.2:
        return price * (1- discount_percent)
    else:
        return price



original_price = float(input("Enter original price: "))
 
discount_percentage = float(input("Enter the discount percentage: "))
print("Discounted price: ", calculate_discount(original_price, discount_percentage / 100))
