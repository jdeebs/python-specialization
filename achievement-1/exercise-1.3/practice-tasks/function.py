def apple(color="red", weight=0):
    print("Your apple color is: " + color)

    if color == "green":
        print("Green apple confirmed!")
    else:
        print("Your apple is not green")
    if weight > 80:
        print("Your apple weighs a ton!")
    else:
        print("Your apple is small.")
        


color = str(input("Enter your apples color: "))
weight = int(input("Enter your apples weight (in grams): "))

apple(color, weight)