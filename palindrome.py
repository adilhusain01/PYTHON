def is_palindrome(s):
    s = s.replace(" ", "").lower()
    
    return s == s[::-1]

input_string = input("Enter a string: ")

result = is_palindrome(input_string)
if result:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
