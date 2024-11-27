# check ele in tuple or not


def check_ele(ele, tup):
    return ele in tup 

tup = (10, 20, 30)

number = int(input("enter element : "))

ele = int(number)

# res = check_ele(ele)

if check_ele(ele, tup):
    print("ele is in tuple")
else:
    print("ele is not in tuple")