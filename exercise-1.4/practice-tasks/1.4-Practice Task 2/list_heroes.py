def display(file):
    heroes = []
    # Iterate over each line in the file
    for line in file:
        # Remove newline character
        line = line.rstrip("\n")

        # Split the hero name and year separately at the ",".
        # Take the first element of the split
        hero_name = line.split(", ")[0]
        # Take the second element of the split
        first_appearance = line.split(", ")[1]

        # Append both elements into a sublist together and then append the sublist to the heroes list
        heroes.append([hero_name, first_appearance])

        # Sort heroes by first appearance
        # Lambda is an anonymous function that takes one parameter "hero" and returns "hero[1]"
        # hero[1] is the second item in the sublist
        # e.g. the year of the first_appearance
        # It then returns the earliest first_appearance to the sort() as default sort is ascending 1 -> 1000 etc
        heroes.sort(key = lambda hero: hero[1])

        for hero in heroes:
            print("Superhero: " + hero[0])
            print("First year of appearance: " + hero[1])

# Prompt user to enter the filename where superhero data is stored
filename = input("Enter the filename where you've stored your superheroes: ")
try:
    file = open(filename, 'r')
    display(file)
except FileNotFoundError:
    print("File doesn't exist - exiting.")
except:
    print("An unexpected error occurred.")
else:
    file.close()
finally:
    print("Goodbye!")