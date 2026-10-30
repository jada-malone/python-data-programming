# PROGRAM: Leap Year Problem
# PURPOSE: Determine if a given year is a leap year based on specific rules.
# INPUT: A four-digit year from the user.
# PROCESS: Check if the year is a leap year based on leap year rules.
# OUTPUT: Whether the year is a leap year or not.
# HONOR CODE: On my honor, as an Aggie, I have neither given nor received unauthorized aid on this academic work.

def is_leap_year(year: int) -> bool:
    """Check if the given year is a leap year."""
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def main():
    """Main function to handle user input and display whether the year is a leap year."""
    year = int(input("Enter a four-digit year: "))
    if is_leap_year(year):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")

if __name__ == "__main__":
    main()
