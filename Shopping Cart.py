# User class
class login():

	# Create new user with username and password
    def __init__(self, id, pas):
        self.id = id
        self.pas = pas

	# Login as user
    def check(self, id, pas, loggedIn):
        if self.id == id and self.pas == pas:
            loggedIn = True
            return loggedIn
        else: return False

# Item class
class Item(object):

	# Create new item with an ID number, a name, a price, a category, a description, and a quantity
	# Of these attributes, only the price and quantity can be modified after initialization
    def __init__(self, unq_id, name, price, category, description, qty):
        self.unq_id = unq_id
        self.product_name = name
        self.price = price
        self.category = category
        self.description = description
        self.qty = qty

    def updatePrice(self, price):
        self.price = price

    def updateQuantity(self, quantity):
        self.qty = quantity

# Cart class
class Cart(object):

	# Create a cart for the user and initialize a dictionary to store items held in the cart
    def __init__(self):
        self.content = dict()

	# Add a new item to the cart
	# Can add in bulk, but cannot exceed current quantity for the selected item
    def addToCart(self, item, quantity):
        if item.unq_id not in self.content:
            self.content.update({item.unq_id: item})
            return
        for k, v in self.content.get(item.unq_id).items():
            if k == 'unq_id':
                continue
            elif k == 'qty':
                total_qty = v.qty + item.qty
                if total_qty:
                    v.qty = total_qty
                    continue
                self.remove_item(k)
            else:
                print (quantity)
                v[k] = item[k]

	# Calculate the total cost of all items in the cart by going through the list and getting the sum
    def get_total(self):
        return sum([v.price * v.qty for _, v in self.content.items()])

	# Return the total number of items in the cart
    def get_num_items(self):
        return sum([v.qty for _, v in self.content.items()])

	# Remove an item from the cart
    def remove_item(self, key, quantity):
        print(key)
        self.content.pop(key)

# User login
if __name__ == '__main__':
    loggedIn = False
    log = login("admin", "admin")
    while (loggedIn != True):
        loggedIn = log.check(input("Enter Login ID:"),
              input("Enter password: "), loggedIn)

	# Product information
    item1 = Item(1, "Chair", 5.76, "household items", "A wooden chair", 15)
    item2 = Item(2, "Desk", 8.24, "household items", "A wooden desk", 10)
    item3 = Item(3, "Great Expectations", 3.52, "books", "Book by Charles Dickens", 53)
    item4 = Item(4, "Fahrenheit 451", 5.29, "books", "Book by Raay  Bradbury", 45)
    item5 = Item(5, "Lego Set", 10.63, "toys", "Lego death star set", 32)
    item6 = Item(6, "Pikachu Plush", 6.35, "toys", "Plush of Pikachu", 24)
    item7 = Item(7, "RC car", 7.23, "small electronics", "remote controlled car", 9)
    item8 = Item(8, "LED lights", 12.15, "small electronics", "Strip of LED lights", 42)

	# Initialize objects/variables
    itemList = ["Chair", "Desk", "Great Expectations", "Fahrenheit 451", "Lego Set", "Pikachu Plush", "RC car", "LED lights"]
    itemList2 = [item1, item2, item3, item4, item5, item6, item7, item8]
    cart = Cart()

    if (loggedIn == False):
        print("Please log in")
    else:

		# Display UI
        print("""
    What would you like to do?
          1) View Inventory
          2) Add item to cart
          3) Remove item from cart
          4) View cart
          5) Purchase items
          6) View account
          7) Log out""")

        answer = input("> ")

		# Perform action based on user response
        while (answer != "7"):
            if (answer == "1"):
                print(item1.product_name, item1.price, item1.description, item1.category, item1.qty)
                print(item2.product_name, item2.price, item2.description, item2.category, item2.qty)
                print(item3.product_name, item3.price, item3.description, item3.category, item3.qty)
                print(item4.product_name, item4.price, item4.description, item4.category, item4.qty)
                print(item5.product_name, item5.price, item5.description, item5.category, item5.qty)
                print(item6.product_name, item6.price, item6.description, item6.category, item6.qty)
                print(item7.product_name, item7.price, item7.description, item7.category, item7.qty)
                print(item8.product_name, item8.price, item8.description, item8.category, item8.qty)

            elif (answer == "2"):
                add_item = input("which item would you like to add?")
                if add_item in itemList:
                    quantity = input("how many?")
                    cart.addToCart(itemList2[itemList.index(add_item)], quantity)
                else: print("Please type item name")

            elif (answer == "3"):
                remove_item = input("Which item would you like to remove?")
                if add_item in itemList:
                    quantity = input("how many?")
                    cart.remove_item(itemList.index(add_item)+1, quantity)

            elif (answer == "4"):
                print("You have %i items in your cart for a total of $%.02f" % (cart.get_num_items(), cart.get_total()))

            elif (answer == "5"):
                creditCard = input("add credit card for purchase")
                confirm = input("Are you sure you want to purchase (y/n)")
                if confirm == "y":
                    print("than you for your purchase")

            elif (answer == "6"):
                print("""What would you like to do?
            1) Enter Credit Card
            2) Enter Address""")
                accountAnswer = input("> ")
                if (accountAnswer == "1"):
                    creditCard = input("Input Credit Card Numbers: ")

                elif (accountAnswer == "2"):
                    address = input("Input Address: ")

                else:
                    print("Please type a correct option")
                    accountAnswer = input("> ")

            elif (answer == "7"):
                loggedin = False
                break

            else:
                print("Please type a correct option")
                answer = input("> ")
            print("""
    What would you like to do?
          1) View Inventory
          2) Add item to cart
          3) Remove item from cart
          4) View cart
          5) Purchase items
          6) View account
          7) Log out""")
            answer = input("> ")

    #cart.update(item1)
    #cart.update(item2)
    #cart.update(item3)
    #print("You have %i items in your cart for a total of $%.02f" % (cart.get_num_items(), cart.get_total()))
    #cart.remove_item(1)
    #print ("You have %i items in your cart for a total of $%.02f" % (cart.get_num_items(), cart.get_total()))


