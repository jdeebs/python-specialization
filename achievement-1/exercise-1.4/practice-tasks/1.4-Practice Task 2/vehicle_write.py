import pickle

vehicle = {
    'brand': 'BMW',
    'model': '530i',
    'year': 2015,
    'color': 'Black Sapphire'
}

# Open or create a binary file in write mode to store vehicle details
my_file = open('vehicledetail.bin', 'wb')

# Convert vehicle dictionary and write it to the binary file
pickle.dump(vehicle, my_file)

# Close file to ensure saved data and released resources
my_file.close()