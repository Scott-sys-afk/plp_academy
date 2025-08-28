def calculate_discount(price, discount_percent):
    """Calculate final price after discount if discount is 20% or higher."""
    if discount_percent >= 20:
        return price * (1 - discount_percent / 100)
    return price

# Get user input
try:
    price = float(input("Enter the original price: $"))
    discount = float(input("Enter the discount percentage: "))
    
    final_price = calculate_discount(price, discount)
    
    if discount >= 20:
        print(f"Final price after {discount}% discount: ${final_price:.2f}")
    else:
        print(f"No discount applied. Price remains: ${price:.2f}")
        
except ValueError:
    print("Please enter valid numbers!")