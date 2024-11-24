class Height(object):
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    def __str__(self):
        output = str(self.feet) + " feet, " + str(self.inches) + " inches"
        return output
    
    def __sub__(self, other):
        # Convert feet to inches
        height1_inches = self.feet * 12 + self.inches
        height2_inches = other.feet * 12 + other.inches

        # Subtract height 1 from height 2
        if height1_inches < height2_inches:
            return print("Make sure the taller height is placed first in order to subtract.")
        total_height_inches = height1_inches - height2_inches

        # Get output in feet and inches
        output_feet = total_height_inches // 12
        output_inches = total_height_inches - (output_feet * 12)

        # Return feet and inches output in new Height object
        return Height(output_feet, output_inches)
    
person1_height = Height(5, 10)
person2_height = Height(3, 9)

height_difference = person1_height - person2_height

print("Height difference: ", height_difference)