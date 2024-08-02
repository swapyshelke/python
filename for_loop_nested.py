rows = int(input("enter no. of rows : "))
columns = int(input("enter no. of columns : "))
symbol = input("enter symbol : ")


for x in range(rows):
    for y in range(columns):
        print(symbol, end="")
    print()