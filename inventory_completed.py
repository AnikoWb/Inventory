# ======== The beginning of the class ========== #
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
   
    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity
       
        
    def __str__(self):
        output = f""" 👟 ------------------------- ⌘ ------------------------- 👟\n
    Country: {self.country} 
    Code: {self.code} 
    Product: {self.product}
    Cost: {self.cost} 
    Quantity: {self.quantity}\n"""
        return output
 

# ============= Shoe list =========== #

# The list will be used to store a list of objects of shoes.
shoe_list = []

# ========== Functions outside the class =========== #

# Reading data from the file and adding the shoes to the list as objects
def read_shoes_data():
    try:
        shoes_data_file = open("inventory.txt", "r")
        shoes_data = shoes_data_file.readlines()[1:]
        shoes_data_file.close()
        
        for line in shoes_data:
            line = line.strip("\n")
            split_line = line.split(",")
            shoe_list.append(Shoe(split_line[0], split_line[1], split_line[2], split_line[3], split_line[4]))
        

    except FileNotFoundError:
        print("\nThere's no data in the system, please upload the latest inventory file (inventory.txt).")
        

# Add a new item
def capture_shoes():
    country = input("Country: ")
    code = input("Code: ")
    product = input("Product: ")
    while True:
        try:
            cost = float(input("Cost: "))
            break 
        except ValueError:
            print("Please enter a number.")

    while True:        
        try:
            quantity = int((input("Quantity: "))) 
            break
        except ValueError:
            print("Please enter a whole number.")

    shoe_list.append(Shoe(country, code, product, cost, quantity))

    shoes_data_file = open("inventory.txt", "w+")
    shoes_data_file.write("Country,Code,Product,Cost,Quantity\n")
    for shoe in shoe_list:
        shoes_data_file.write(shoe.country + "," + shoe.code + "," + shoe.product + "," + str(shoe.cost) + "," + str(shoe.quantity) + "\n")
    shoes_data_file.close()

    print("\n\nThank you, this item has been added to the inventory. ✔\n\n")

# Print all the items in the inventory with all details
def view_all():
    for shoe in shoe_list:
        print(shoe)

# Find the item with the lowest quantity and option to restock
def re_stock():
    quantity_list = []

    for shoe in shoe_list:
        quantity_list.append(int(shoe.quantity))

    min_qty = min(quantity_list)

    for shoe in shoe_list:
        if min_qty == int(shoe.quantity):
            print("\n\nThe item with the lowest quantity is: \n")
            print(shoe)

    while True:
        choice = input("""
1, Re-stock the item 
2, Exit to the Main Menu\n\n""")
        if choice == "1":
            order_qty = input("Please enter the new order amount: ")
            for shoe in shoe_list:
                if min_qty == int(shoe.quantity):
                    shoe.quantity = str(int(shoe.quantity)+int(order_qty))

            shoes_data_file = open("inventory.txt", "w+")
            shoes_data_file.write("Country,Code,Product,Cost,Quantity\n")
            for shoe in shoe_list:
                shoes_data_file.write(shoe.country + "," + shoe.code + "," + shoe.product + "," + shoe.cost + "," + shoe.quantity + "\n")
            shoes_data_file.close()

            print("\n\nThank you, your order has been submitted. The inventory has been updated with this order. ✔\n\n")
            break

        elif choice == "2": 
            break

        else: 
            print("\nInvalid option. Please try again.\n")

# Search an item by product code
def search_shoe():
    while True:
        code = input("Shoe code: ")
        shoe_not_found = True
        for shoe in shoe_list:
            if code == shoe.code:
                print("\n")
                print(shoe)
                shoe_not_found = False

        if shoe_not_found == True:
            print("\nThere is no item with this product code. Please try again.\n")
        
    
# Calculate the value for each item
def value_per_item():
    for shoe in shoe_list:
        value = float(shoe.cost) * int(shoe.quantity)
        print(shoe)
        print(f"""
    Value: {value}""")    

# Find the item with highest quantity which is on sale
def highest_qty():
    quantity_list = []

    for shoe in shoe_list:
        quantity_list.append(int(shoe.quantity))

    max_qty = max(quantity_list)

    for shoe in shoe_list:
        if max_qty == int(shoe.quantity):
            print("\n\n ✔ SALE - the below product is on sale as we have the highest quantity of this item. ✔ \n\n")
            print(shoe)
   
# ======================== Main Menu ================================= #

read_shoes_data()

while True:
    user_message = """
Welcome to the Shoe Inventory. Please select from the options below:\n
✔ 1 See total inventory
✔ 2 Add items to the inventory
✔ 3 Re-stock an item
✔ 4 Search for an item
✔ 5 See the total value of each product
✔ 6 Show product with the highest quantity 
✔ 7 Exit \n\n
"""

    option = input(user_message)

    if option == "1": 
        view_all()

    elif option == "2": 
        capture_shoes()

    elif option == "3":
        re_stock()

    elif option == "4":
        search_shoe()

    elif option == "5":
        value_per_item()

    elif option == "6":
        highest_qty()

    elif option == "7":
        print ("\nGoodbye!\n ✔ just DO it. ")
        break
    else: 
        print("Invalid option. Please try again.")    
