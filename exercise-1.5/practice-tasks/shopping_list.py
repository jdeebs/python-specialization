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
            print(f"'{item}' added to the shopping list.")
    
    def remove_item(self, item):
        try:
            if item in self.shopping_list:
                self.shopping_list.remove(str(item))
            else:
                raise ValueError(f"'{item}' not found in the shopping list.")
        except:
            print(f"Error removing '{item}' from the shopping list.")
        else:
            print(f"'{item}' removed from the shopping list.")
    
    def view_list(self):
        print(self.list_name)
        print(self.shopping_list)

pet_store_list = ShoppingList("Pet Store Shopping List")

pet_store_list.add_item("dog food")
pet_store_list.add_item("frisbee")
pet_store_list.add_item("bowl")
pet_store_list.add_item("collars")
pet_store_list.add_item("flea collars")

pet_store_list.remove_item("flea collars") # Test removal
pet_store_list.add_item("frisbee") # Test no duplicate items

pet_store_list.view_list()