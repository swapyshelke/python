# weight converter in python

weight = float(input("enter weight :"))
unit = input("enter unit in Kilogram or Pounds:")

if unit == "K":
    weight = weight * 2.205
    unit = "Lbs."
elif unit == "L":
    weight = weight / 2.205
    unit = "Kgs."
else:
    print(f"{unit} was not valid")
    
print(f"your weight is: {weight} {unit}")