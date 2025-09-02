def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount = price * (1 - discount_percent / 100)
        final_price = price - discount
        return final_price
    else:
        return price
    
print(calculate_discount(
    price=float(input("Enter the price: ")), 
    discount_percent=float(input("Enter the discount percent: "))
))