class Height(object):
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    def __str__(self):
        output = str(self.feet) + " feet, " + str(self.inches) + " inches"
        return output
    
    def __lt__(self, other):
        height1_inches = self.feet * 12 + self.inches
        height2_inches = other.feet * 12 + other.inches
        return height1_inches < height2_inches
    
    def __le__(self, other):
        height1_inches = self.feet * 12 + self.inches
        height2_inches = other.feet * 12 + other.inches
        return height1_inches <= height2_inches
    
    def __eq__(self, other):
        height1_inches = self.feet * 12 + self.inches
        height2_inches = other.feet * 12 + other.inches
        return height1_inches == height2_inches

    def __gt__(self, other):
        height1_inches = self.feet * 12 + self.inches
        height2_inches = other.feet * 12 + other.inches
        return height1_inches > height2_inches
    
    def __ge__(self, other):
        height1_inches = self.feet * 12 + self.inches
        height2_inches = other.feet * 12 + other.inches
        return height1_inches >= height2_inches
    
    def __ne__(self, other):
        height1_inches = self.feet * 12 + self.inches
        height2_inches = other.feet * 12 + other.inches
        return height1_inches != height2_inches
    
print(Height(4, 6) > Height(4, 5)) # True
print(Height(4, 5) >= Height(4, 5)) # True
print(Height(5, 9) != Height(5, 10)) # True

# Class sorting
height_1 = Height(4, 10)
height_2 = Height(5, 6)
height_3 = Height(7, 1)
height_4 = Height(5, 5)
height_5 = Height(6, 7)
height_6 = Height(5, 6)

# Put objects into sortable list
heights = [height_1, height_2, height_3, height_4, height_5, height_6]

# Sort the list, ensure that __lt__ method is defined for this to work
heights = sorted(heights)
for height in heights:
    print(height)