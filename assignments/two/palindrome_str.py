# palindrome or not


def isPalindrome(string):
	if (string == string[::-1]):
		return print("The string is palindrome")
	else:
		return print("string is not palindrome")

string = input("Enter string: ")

print(isPalindrome(string))


