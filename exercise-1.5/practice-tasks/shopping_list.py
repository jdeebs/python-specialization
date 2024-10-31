class ShoppingList(object):
    def __init__(self, list_name):
        self.list_name = str(list_name)
        self.shopping_list = []
        
    def add_item(self, item):
        try:
            if item not in self.shopping_list:
                self.shopping_list.append(str(item))
            else:
                raise ValueError(f"'{item}' is already in the shopping list.")
        except:
            print(f"Error adding '{item}' to the shopping list. Make sure '{item}' isn't already on the list.")
        else:
            print(f"'{item}' added to the {self.list_name} shopping list.")
    
    def remove_item(self, item):
        try:
            if item in self.shopping_list:
                self.shopping_list.remove(str(item))
            else:
                raise ValueError(f"'{item}' not found in the shopping list.")
        except:
            print(f"Error removing '{item}' from the shopping list.")
        else:
            print(f"'{item}' removed from the {self.list_name} shopping list.")
    
    def view_list(self):
        print("\n" + self.list_name)
        print("------------------------------")
        # Format shopping list with a new line per item
        shopping_list_formatted = "\n - ".join(self.shopping_list)
        print(" - " + shopping_list_formatted)

    def merge_lists(self, obj):
        # Create name for new merged shopping list
        merged_lists_name = 'Merged List - ' + str(self.list_name) + " + " + str(obj.list_name)

        # Initialize new ShoppingList object with the new name that will store the merged items
        merged_lists_obj = ShoppingList(merged_lists_name)

        # Copy the items from the first list (self) into the new list
        merged_lists_obj.shopping_list = self.shopping_list.copy()

        # Iterate over each item in second list (obj) and check whether item exists in first list
        # If not present, append it to the first list, this ensures no duplicate items
        for item in obj.shopping_list:
            if not item in merged_lists_obj.shopping_list:
                merged_lists_obj.shopping_list.append(item)
        # Returns merged list
        return merged_lists_obj

pet_store_list = ShoppingList("Pet Store")
grocery_store_list = ShoppingList("Grocery Store")

# Use loop to add items to each list
for item in ['dog food', 'frisbee', 'bowl', 'collars', 'flea collars']:
    pet_store_list.add_item(item)
for item in ['fruits', 'vegetables', 'bowl', 'ice cream']:
    grocery_store_list.add_item(item)

# Merge the two lists together, since the merge_lists() method returns another ShoppingList it must be assigned to a new object (merged_list)
merged_list = ShoppingList.merge_lists(pet_store_list, grocery_store_list)

merged_list.view_list()