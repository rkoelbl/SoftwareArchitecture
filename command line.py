loggedin = True

if (loggedin == False):
    print("Please log in")
else:
    
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

    while (answer != "7"):
        if (answer == "1"):
            print("show inventory here")
            
        elif (answer == "2"):
            print("Add to cart function")
            
        elif (answer == "3"):
            print("Remove from cart function")
            
        elif (answer == "4"):
            print("View cart")
            
        elif (answer == "5"):
            print("Purchase")
            
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
    
