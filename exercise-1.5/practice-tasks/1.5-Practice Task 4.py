class Animal(object):
    # Every animal has an age, but a name may not be necessary
    def __init__(self, age):
        self.age = age
        self.name = None

    # Getter methods for age and name       
    def get_age(self):
        return self.age

    def get_name(self):
        return self.name

    # Setter methods for age and name 
    def set_age(self, age):
        self.age = age

    def set_name(self, name):
        self.name = name

    # Display string
    def __str__(self):
        output = "\nClass: Animal\nName: " + str(self.name) + \
            "\nAge: " + str(self.age)
        return output
    
a = Animal(5)
print(a)

class Cat(Animal):
    # New method for speak
    def speak(self):
        print("Meow")

    # Display string
    def __str__(self):
        output = "\nClass: Cat\nName: " + str(self.name) + \
            "\nAge: " + str(self.age)
        return output
    
class Dog(Animal):
    # Implementing another speak() method for dogs
    def speak(self):
        print("Woof!")

    # String representation for dogs
    def __str__(self):
        output = "\nClass: Dog\nName: " + str(self.name) + \
            "\nAge: " + str(self.age)
        return output
    
# Objects created from classes
cat = Cat(3)
dog = Dog(6)

# Set pet names
cat.set_name("Pepper")
dog.set_name("Margo")

print(cat)
cat.speak()
print(dog)
dog.speak()

class Human(Animal):
    # Unique initialization method
    def __init__(self, name, age):
        # Call the parent class' init method to initialize other attributes like 'name' and 'age'
        Animal.__init__(self, age)

        # Inherited method to set a name
        self.set_name(name)

        # New attribute for humans, 'friends'
        self.friends = []

    # New method to add friends
    def add_friend(self, friend_name):
        self.friends.append(friend_name)

    # New method to display friends
    def show_friends(self):
        for friend in self.friends:
            print(friend)

    # Inherited method to speak
    def speak(self):
        print("Hello, my name's " + self.name + "!")

    # Display string, includes friends
    def __str__(self):
        output = "\nClass: Human\nName: " + str(self.name) + \
            "\nAge: " + str(self.age) + "\nFriends list: \n"
        for friend in self.friends:
            output += friend + "\n"
        return output

# New human object
human = Human("Toby", 33)

# Add friends to human object
human.add_friend("Robert")
human.add_friend("Élise")
human.add_friend("Abdullah")
human.add_friend("Asha")
human.add_friend("Lupita")
human.add_friend("Saito")

human.speak()
print(human)

class ClassVariable(object):
    common_string = "Hello, I can be accessed from anywhere!"

    def __init__(self, a, b):
        self.a = a
        self.b = b

alpha = ClassVariable(1, 2)
beta = ClassVariable(3, 4)

# Test that both objects have access to common_string within the class definition
print(alpha.common_string)
print(beta.common_string)

# Can change the string for all objects what share the variable by changing the class definition
ClassVariable.common_string = "Changed string!"

print(alpha.common_string)
print(beta.common_string)