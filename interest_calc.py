principle = 0
interest = 0
time = 0

while True:
    principle = float(input("Enter your principle amount : "))
    if principle <= 0:
        print('Principle cant be less than or equal to zero.')
    else:
        break



while True:
    interest = float(input("Enter your interest : "))
    if interest <= 0:
        print('Interest cant be less than or equal to zero.')
    else:
        break



while True:
    time = float(input("Enter your  time in years. : "))
    if time <= 0:
        print('Time cant be less than or equal to zero.')
    else:
        break


# print(principle)
# print(interest)
# print(time)

total = principle * pow((1 + interest / 100), time)

print(f"Balance after {time} year/s: ${total:.2f}")