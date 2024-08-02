item = input("What item you want to buy?")
prize = float(input("What is the price?"))
quantity = int( input("how many would you like? "))

total = price * quantity
print(f"you have bought {quantity} X {item}/s")
print(f"youre total is: {total}")