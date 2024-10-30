class Date(object):
    # init automatically called when a new instance (object) of the class Date is created
    # self parameter is a reference to the new instance, allowing access to set the attributes
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def get_date(self):
        output = str(self.day) + "/" + str(self.month) + "/" + str(self.year)
        return output
    
    def set_date(self):
        self.day = int(input("Enter the day of the month: "))
        self.month = int(input("Enter the month: "))
        self.year = int(input("Enter the year: "))


# Create an instance of Date as an object
first_moon_landing = Date(20, 7, 1969)

# Print the date with a getter function
print(first_moon_landing.get_date())

# Change the date with setter function
first_moon_landing.set_date()

# Print modified date
print(first_moon_landing.get_date())