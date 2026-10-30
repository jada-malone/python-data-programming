# PROGRAM: Vowel Count Problem
# PURPOSE: Count occurrences of each vowel in a user-provided string and the total number of vowels.
# INPUT: A string from the user.
# PROCESS: Count the occurrences of each vowel and the total number of vowels in the string.
# OUTPUT: The number of each vowel and the total number of vowels.
# HONOR CODE: On my honor, as an Aggie, I have neither given nor received unauthorized aid on this academic work.

def count_vowels(input_string: str) -> dict:
    """Count occurrences of each vowel in the given string and the total number of vowels."""
    vowels = 'aeiou'
    count = {vowel: input_string.lower().count(vowel) for vowel in vowels}
    count['total'] = sum(count.values())
    return count

def main():
    """Main function to handle user input and display the results."""
    user_input = input("Enter a string: ")
    vowel_counts = count_vowels(user_input)
    for vowel, number in vowel_counts.items():
        if vowel == 'total':
            print(f"Total number of vowels: {number}")
        else:
            print(f"Number of '{vowel}': {number}")

if __name__ == "__main__":
    main()
