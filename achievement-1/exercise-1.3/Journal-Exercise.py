available_destinations = ["London", "Japan", "Mexico"]

print("\nEnter your desired destination below\n")

destination = str(input("Destination: "))

if destination in available_destinations:
    print(f"Enjoy your stay in {destination}!")
else:
    print("Oops, that destination is not currently available.")