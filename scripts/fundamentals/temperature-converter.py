# PROGRAM: Temperature Conversion
# PURPOSE: Convert temperature from Celsius to Fahrenheit
# INPUT: Temperature in Celsius
# PROCESS: Apply the formula to convert Celsius to Fahrenheit
# OUTPUT: Temperature in Fahrenheit
# HONOR CODE: On my honor, as an Aggie, I have neither given nor received unauthorized aid on this academic work.

def CelsiusToFahrenheit(celsius):
    """
    Convert temperature from Celsius to Fahrenheit.
    
    :param celsius: Temperature in Celsius
    :return: Temperature in Fahrenheit
    """
    return (celsius * 9 / 5) + 32

def Main():
    """
    Main function to execute temperature conversion.
    """
    try:
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = CelsiusToFahrenheit(celsius)
        print(f"{celsius} Celsius is equal to {fahrenheit} Fahrenheit.")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    Main()
