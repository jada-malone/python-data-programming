import string 
 # PROGRAM: Palindrome Checker
 # PURPOSE: Check if a user-entered string is a palindrome 
 #          after removing punctuation, special characters, and spaces.
 # INPUT: User input string
 # PROCESS: Clean the string by removing unwanted characters and 
 #          check if it reads the same forwards and backwards.
 # OUTPUT: Message indicating whether the string is a palindrome or not.
# HONOR CODE: On my honor, as an Aggie, I have neither given nor 
#             received unauthorized aid on this academic work.

def is_palindrome(s):
    """
    Checks if the cleaned version of the string is a palindrome.
    """
    # Remove punctuation, special characters, and spaces, then convert to lowercase
    cleaned_string = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned_string == cleaned_string[::-1]

if __name__ == "__main__":
    user_input = input("Enter a string to check if it's a palindrome: ")
    if is_palindrome(user_input):
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")
