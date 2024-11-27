



def remove_element(tup, ele):
    return tuple(x for x in tup if x != ele)

tup = (1, 2, 3, 4, 5)

print(f"original tuple {tup}")

element = int(input("enter ele to remove"))

new_tup = remove_element(tup, element)



print(f"new tuple is {new_tup}")