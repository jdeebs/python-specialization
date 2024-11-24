class Height(object):
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    # Return human-readable output from the Height class
    def __str__(self):
        output = str(self.feet) + " feet, " + str(self.inches) + " inches"
        return output
    
    def __add__(self, other):
        # Convert both objects height into inches
        height1_inches = self.feet * 12 + self.inches
        height2_inches = other.feet * 12 + other.inches

        # Add them together
        total_height_inches = height1_inches + height2_inches

        # Get output in feet and inches
        output_feet = total_height_inches // 12
        output_inches = total_height_inches - (output_feet * 12)

        # Return feet and inches output in new Height object
        return Height(output_feet, output_inches)

person1_height = Height(5, 10)
person2_height = Height(4, 10)
height_sum = person1_height + person2_height

print("Total height: ", height_sum)