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

    # Simplified method to check for leap year
    def is_leap_year(self):
        return self.year % 4 == 0
    
    def is_valid_date(self):
        # Check if values are all integers
        if not (type(self.day) == int and type(self.month) == int and type(self.year) == int):
            return False
        # Check that year isn't negative
        if self.year < 0:
            return False
        # Check if month is between 1-12
        if self.month < 1 or self.month > 12:
            return False
        # Check if days are valid for any given month
        # Last dates for each month in a dictionary
        # Key = month, Value = # of days that month
        last_dates = {
            1: 31,
            # Change leap year # of days to 29
            2: 29 if self.is_leap_year() else 28,
            3: 31,
            4: 30,
            5: 31,
            6: 30,
            7: 31,
            8: 31,
            9: 30,
            10: 31,
            11: 30,
            12: 31
        }
        # Check if the day is valid for the given month
        if self.day < 1 or self.day > last_dates.get(self.month):
            return False
        # If none of the above statements are triggered
        return True

# Create an instance of Date as an object
first_moon_landing = Date(20, 7, 1969)

# Print the date with a getter function
print(first_moon_landing.get_date())

# Change the date with setter function
first_moon_landing.set_date()

# Print modified date
print(first_moon_landing.get_date())