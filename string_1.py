# name = input("Enter any string: ")
# phone_no = input("enter phone number: ")



# 1. count - count length of str
# 2. replace - replace anything with other thing
# 3. isdigit - check i fnumber present or not
# 4. isalpha() - check if only contains alphabets or not
# 5. 

# result = phone_no.replace(" ", "")
# print(result)

# print(len(name))
# print(name)

# print(name.find(" "))

# print(name)
# print(name.find(" "))

# print(help(str))

# exercise

# take username
# 1. no spaces
# 2. no digits
# 3. not more than 12 letters

username = input("enter username : ")

if not username.isdigit():
    print("no digits are allowed")
elif not username.find(" ") == -1:
    print("no spaces allowed")
elif len(username) > 12:
    print("uname should be less than 12 letters")
else:
    print("username is registered")
