# fibonachi 
# 0 1 1 2 3 5 8 


num = int(input("enter num : "))
n1, n2 = 0, 1
print("fibonachi series : ", n1, n2, end=" ")

for i in range(2, num):
    n3 = n1 + n2 
    n1 = n2
    n2 = n3
    print(n3, end=" ")