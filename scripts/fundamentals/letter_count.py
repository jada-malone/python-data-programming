# PROGRAM: Letter Count Problem
# PURPOSE: Count occurrences of the letter 'e' or 'E' in a user-provided string.
# INPUT: A string from the user.
# PROCESS: Count the occurrences of 'e' and 'E' in the string.
# OUTPUT: The number of times 'e' or 'E' occurs.
# HONOR CODE: On my honor, as an Aggie, I have neither given nor received unauthorized aid on this academic work.

def count_e(input_string: str) -> int:
    """Count occurrences of the letter 'e' or 'E' in the given string."""
    return input_string.lower().count('e')

def main():
    """Main function to handle user input and display the result."""
    user_input = input("Enter a string: ")
    count = count_e(user_input)
    print(f"The letter 'e' or 'E' occurs {count} times.")

if __name__ == "__main__":
    main()
