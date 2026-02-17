price=2.99
quantity=3
tax_rate=7.5

# calculate subtotal
subtotal=price*quantity
# calculate tax
tax=subtotal*(tax_rate/100)
# Calculate total
total=subtotal+tax

print(f"Price of item: ${price}")
print(f"Quantity: {quantity}")
print(f"Tax rate: {tax_rate}%\n")

print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Total: ${total:.2f}")