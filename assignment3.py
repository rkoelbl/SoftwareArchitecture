# User class
class login():

	# Create new user with username and password
    def __init__(self, id, pas):
        self.id = id
        self.pas = pas

	# Login as user
    def check(self, id, pas):
        print (self.id)
        if self.id == id and self.pas == pas:
            print ("Login success!")


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

# Cart class
class Cart(object):

	# Create a cart for the user and initialize a dictionary to store items held in the cart
    def __init__(self):
        self.content = dict()

	# Add a new item to the cart
	# Can add in bulk, but cannot exceed current quantity for the selected item
    def update(self, item):
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
                v[k] = item[k]

	# Calculate the total cost of all items in the cart by going through the list and getting the sum
    def getTotal(self):
        total = 0
        for item in self.list:
            name, price = item  # or price = item[1]
            total = total + price

	# Return the total number of items in the cart
    def get_num_items(self):
        return sum([v.qty for _, v in self.content.items()])

	# Remove an item from the cart
    def remove_item(self, key):
        self.content.pop(key)


if __name__ == '__main__':
    log = login("admin", "admin")
    log.check(input("Enter Login ID:"),
              input("Enter password: "))


    item1 = Item(1,"Chair",5.76, "household items", "A wooden chair", 15)
    item2 = Item(2, "Desk", 8.24, "household items", "A wooden desk", 10)
    item3 = Item(3, "Great Expectations", 3.52, "books", "Book by Charles Dickens", 53)
    item4 = Item(4, "Fahrenheit 451", 5.29, "books", "Book by Raay  Bradbury", 45)
    item5 = Item(5, "Lego Set", 10.63, "toys", "Lego death star set", 32)
    item6 = Item(6, "Pikachu Plush", 6.35, "toys", "Plush of Pikachu", 24)
    item7 = Item(7, "RC car", 7.23, "small electronics", "remote controlled car", 9)
    item8 = Item(8, "LED lights", 12.15, "small electronics", "Strip of LED lights", 42)

    print (item1.product_name, item1.price)
    print(item2.product_name, item2.price)
    print(item3.product_name, item3.price)
    print(item4.product_name, item4.price)
    print(item5.product_name, item5.price)
    print(item6.product_name, item6.price)
    print(item7.product_name, item7.price)
    print(item8.product_name, item8.price)


    cart = Cart()
    cart.update(item1)
    cart.update(item2)
    cart.update(item3)
    print("You have %i items in your cart for a total of $%.02f" % (cart.get_num_items(), cart.get_total()))
    cart.remove_item(1)
    print ("You have %i items in your cart for a total of $%.02f" % (cart.get_num_items(), cart.get_total()))
