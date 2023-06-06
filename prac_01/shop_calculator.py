"""
Shop Calculator
The program allows the user to enter the number of items and the price of each different item.
Then the program computes and displays the total price of those items.
if the total price is over $100, then a 10% discount is applied to that total
"""
ItemList: list[float] = []
price_output: float = 0
total = 0
item_num = int(input("Number of items:"))
for i in range(item_num):
    price = float(input("Price of items:"))
    ItemList.append(price)
total = sum(ItemList)

if total < 0:
    print("wrong price input")
elif total > 100:
    price_output = total * 0.9
else:
    price_output = total

print(f"Total price for 3 items is ${price_output:.2f}")
# print(ItemList)
# print(price_output)
# print(total)
