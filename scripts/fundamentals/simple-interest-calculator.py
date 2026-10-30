# PROGRAM: Simple Interest Calculator
# PURPOSE: Calculate simple interest based on principal, rate, and time
# INPUT: Principal amount, rate of interest, and time period in years
# PROCESS: Apply the formula to compute simple interest
# OUTPUT: Simple interest
# HONOR CODE: On my honor, as an Aggie, I have neither given nor received unauthorized aid on this academic work.

def CalculateSimpleInterest(principal, rate, time):
    """
    Calculate simple interest.
    
    :param principal: Principal amount
    :param rate: Rate of interest
    :param time: Time period in years
    :return: Calculated simple interest
    """
    return (principal * rate * time) / 100

def Main():
    """
    Main function to execute simple interest calculation.
    """
    try:
        principal = float(input("Enter the principal amount: "))
        rate = float(input("Enter the rate of interest: "))
        time = float(input("Enter the time period in years: "))
        
        interest = CalculateSimpleInterest(principal, rate, time)
        print(f"The simple interest is: {interest}")
    except ValueError:
        print("Please enter valid numbers.")

if __name__ == "__main__":
    Main()
