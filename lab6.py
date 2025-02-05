price=2.99
quantity=3
tax_rate=7.5
subtotal=price*quantity
tax=round(subtotal*0.075,2)
total=round(subtotal+tax,2)
print("price of the item ${}".format(price))
print("quantity {}" .format(quantity))
print("tax rate {}%".format(tax_rate))
print("subtotal ${} ".format(subtotal))
print("tax ${}".format(tax))
print("$total {}".format(total))
print("${} for the total cost".format(total))