email = "swapy123@gmail.com"

# swapy@123gmail.com

# split email by user name and domain

index_of_at_rate = email.find("@")
print(index_of_at_rate)

username = email[:index_of_at_rate:]
domain = email[index_of_at_rate:]

print(username)
print(domain)