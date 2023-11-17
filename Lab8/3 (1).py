def is_palindrome(input_string):
    cleaned_string = ''.join(input_string.split()).lower()

    return cleaned_string == cleaned_string[::-1]

user_input = input("Enter a string: ")
if is_palindrome(user_input):
    print("The entered string is a palindrome.")
else:
    print("The entered string is not a palindrome.")
