# Define a function to convert feet and inches to meters
def convert_to_meters(feet, inches):
    """
    This function converts feet and inches to meters.

    Parameters:
    feet (float): The length in feet.
    inches (float): The length in inches.

    Returns:
    float: The length in meters.

    Example:
    >>> convert_to_meters(5, 3)
    1.6002

    """

    # Constants for conversion
    # Here we define a local constant that represents the number of meters in a foot
    FEET_TO_METERS = 0.3048

    # Here we define a local constant that represents the number of meters in an inch
    INCHES_TO_METERS = 0.0254

    # Convert feet to meters
    # We multiply the number of feet by the number of meters in a foot
    feet_in_meters = feet * FEET_TO_METERS

    # Convert inches to meters
    # We multiply the number of inches by the number of meters in an inch
    inches_in_meters = inches * INCHES_TO_METERS

    # Total length in meters
    # We add the number of meters from the feet and the inches together
    total_meters = feet_in_meters + inches_in_meters

    # We return the total number of meters
    return total_meters

# Test the function
# We define a global variable for the number of feet
feet = 5

# We define a global variable for the number of inches
inches = 3

# We call our function with the number of feet and inches
# and store the result in a variable called meters
meters = convert_to_meters(feet, inches)

# We print out the result in a formatted string
print(f"{feet} feet {inches} inches is equal to {meters} meters.")