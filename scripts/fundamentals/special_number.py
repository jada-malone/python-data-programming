# PROGRAM: Special Number Finder
# PURPOSE: Find a four-digit number that, when multiplied by 4, 
#          has its digits reversed.
# INPUT: None
# PROCESS: Iterate through four-digit numbers, check if multiplying by 4 
#          results in a reversed number.
# OUTPUT: The four-digit number meeting the criteria or a message if not found.
# HONOR CODE: On my honor, as an Aggie, I have neither given nor 
#             received unauthorized aid on this academic work.

def find_special_number():
    """
    Finds a four-digit number where multiplying the number by 4 
    results in its digits reversed.
    """
    for num in range(1000, 10000):
        reversed_num = int(str(num)[::-1])

        if num * 4 == reversed_num:
            return num
    return None

if __name__ == "__main__":
    result = find_special_number()
    if result:
        print("The four-digit number is {result}.")
    else:
        print("No such number found.")
