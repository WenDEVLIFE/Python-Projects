# This is A Simple Pizza Ordering System With Login And DATABASE
# Made by: Frouen M. Medina Jr.
# Version v1.0
# ----------------------------------------------------------------
# Login Interface
# In order To buy is to Log in your credentials to Proceed
# ----------------------------------------------------------------
print("--------------------------------------")
print("----Pizza-Ordering-System-Login-------")
print("--------------------------------------")
Username = input("Enter Your Username:")
print("--------------------------------------")
Password = input("Enter Your Password:")
print("--------------------------------------")
# ----------------------------------------------------------------
# User1
# ----------------------------------------------------------------
if Username == "User8904" and Password == "username4232":
    print("Welcome User User8904")
    print("Welcome To Pizza Ordering System")
    # Select an Menu
    print("[0] Logout")
    print("Select To Order\n" + "[0] Exit\n" + "[1] Pizza Peperoni with Pineapple\n" + "Price 200")
    print("[2] Pizza With Bacon and bell pepper with cheese\n" + "price 290")
    print("[3] Pizza With beef and bell pepper with cheese\n" + "price 350")
    print("[4] Pizza With Bacon and bell pepper with cheese\n" + "price 390")
    print("[5] Hawaiian Pizza\n" + "price 400")
    print("[6] Buddy Pizza Bundle\n" + "price 600")
    print("[7] Chicago Pizza Style\n" + "price 650")
    print("[8] Crust Pizza with all of toppings like cheese, pineapple and etc\n" + "price 700")
    print("[9] Italian Pizza Style\n" + "price800")
    print("[10] Unlimited Pizza Bundle with drinks\n" + "price 1000 per 5 person")
    selection = int(input("Select From 0-10"))
    # ----------------------------------------------------------------
    # Menu 1
    # ----------------------------------------------------------------
    if selection == 1:
        print("--------------------------------------")
        print("----------You-Selected----------------")
        print("--------------------------------------")
        print("[1] Pizza Peperoni with Pineapple\n" + "Price 200")
        Option = input("Are you sure you want to buy this? Yes or No")
        if Option == "Yes" or Option == "yes":
            print("--------------------------------------")
            print("-------------Add-Ons------------------")
            print("--------------------------------------")
            print("[0] No Add-Ons")
            print("[1] Coke\n" + "price 70")
            print("[2] Sprite\n" + "price 70")
            print("[3] Burger\n" + "price 80")
            print("[4] Fries small \n" + "price 40")
            print("[5] Fries medium \n" + "price 75")
            print("[6] Fries large \n" + "price 100")
            print("[7] Bottle of Water big bottle\n" + "price 80")
            Selected = int(input("Select From 0-7"))
            if Selected == 0:
                money = int(input("Enter Your Money Balance"))
                order = money - 200
                print("You Successfully Order Your Pizza")
                print("Your Balance is now", + order)
            elif Selected == 1:
                money = int(input("Enter Your Money Balance"))
                order = 200 + 70 - money
                print("You Successfully Order Your Pizza")
                print("Your Balance is now", + order)
            elif Selected == 2:
                money = int(input("Enter Your Money Balance"))
                order = 200 + 70 - money
                print("You Successfully Order Your Pizza")
                print("Your Balance is now", + order)
            elif Selected == 3:
                money = int(input("Enter Your Money Balance"))
                order = 200 + 80 - money
                print("You Successfully Order Your Pizza")
                print("Your Balance is now", + order)
            elif Selected == 4:
                money = int(input("Enter Your Money Balance"))
                order = 200 + 40 - money
                print("You Successfully Order Your Pizza")
                print("Your Balance is now", + order)
            elif Selected == 5:
                money = int(input("Enter Your Money Balance"))
                order = 200 + 75 - money
                print("You Successfully Order Your Pizza")
                print("Your Balance is now", + order)
            elif Selected == 6:
                money = int(input("Enter Your Money Balance"))
                order = 200 + 100 - money
                print("You Successfully Order Your Pizza")
                print("Your Balance is now", + order)
            elif Selected == 7:
                money = int(input("Enter Your Money Balance"))
                order = 200 + 80 - money
                print("You Successfully Order Your Pizza")
                print("Your Balance is now", + order)
            else:
                print("Type From 0-7")
        elif Option == "No" or Option == "no":
            print("Take Your Time")
        else:
            print("Type Yes or No")
    # ----------------------------------------------------------------
    # Menu 2
    # ----------------------------------------------------------------
    elif selection == 2:
        print("--------------------------------------")
        print("----------You-Selected----------------")
        print("--------------------------------------")
        print("[2] Pizza With Bacon and bell pepper with cheese\n" + "price 290")
        Option = input("Are you sure you want to buy this? Yes or No")
        if Option == "Yes" or Option == "yes":
            print("--------------------------------------")
            print("-------------Add-Ons------------------")
            print("--------------------------------------")
            print("[0] No Add-Ons")
            print("[1] Coke\n" + "price 70")
            print("[2] Sprite\n" + "price 70")
            print("[3] Burger\n" + "price 80")
            print("[4] Fries small \n" + "price 40")
            print("[5] Fries medium \n" + "price 75")
            print("[6] Fries large \n" + "price 100")
            print("[7] Bottle of Water big bottle\n" + "price 80")
            Selected = int(input("Select From 0-7"))
            if Selected == 0:
                money = int(input("Enter Your Money Balance"))
                order = money - 290
                print("You Successfully Order Your Pizza")
                print("Your Balance is now", + order)
            elif Selected == 1:
                money = int(input("Enter Your Money Balance"))
                order = 290 + 70 - money
                print("You Successfully Order Your Pizza")
                print("Your Balance is now", + order)
            elif Selected == 2:
                money = int(input("Enter Your Money Balance"))
                order = 290 + 70 - money
                print("You Successfully Order Your Pizza")
                print("Your Balance is now", + order)
            elif Selected == 3:
                money = int(input("Enter Your Money Balance"))
                order = 290 + 80 - money
                print("You Successfully Order Your Pizza")
                print("Your Balance is now", + order)
            elif Selected == 4:
                money = int(input("Enter Your Money Balance"))
                order = 290 + 40 - money
                print("You Successfully Order Your Pizza")
                print("Your Balance is now", + order)
            elif Selected == 5:
                money = int(input("Enter Your Money Balance"))
                order = 290 + 75 - money
                print("You Successfully Order Your Pizza")
                print("Your Balance is now", + order)
            elif Selected == 6:
                money = int(input("Enter Your Money Balance"))
                order = 290 + 100 - money
                print("You Successfully Order Your Pizza")
                print("Your Balance is now", + order)
            elif Selected == 7:
                money = int(input("Enter Your Money Balance"))
                order = 290 + 80 - money
                print("You Successfully Order Your Pizza")
                print("Your Balance is now", + order)
            else:
                print("Type From 0-7")
        elif Option == "No" or Option == "no":
            print("Take Your Time")
        else:
            print("Type Yes or No")
    # ----------------------------------------------------------------
    # Menu 3
    # ----------------------------------------------------------------
    elif selection == 3:
        print("--------------------------------------")
        print("----------You-Selected----------------")
        print("--------------------------------------")
        print("[3] Pizza With beef and bell pepper with cheese\n" + "price 350")
        Option = input("Are you sure you want to buy this? Yes or No")
        if Option == "Yes" or Option == "yes":
            print("--------------------------------------")
            print("-------------Add-Ons------------------")
            print("--------------------------------------")
            print("[0] No Add-Ons")
            print("[1] Coke\n" + "price 70")
            print("[2] Sprite\n" + "price 70")
            print("[3] Burger\n" + "price 80")
            print("[4] Fries small \n" + "price 40")
            print("[5] Fries medium \n" + "price 75")
            print("[6] Fries large \n" + "price 100")
            print("[7] Bottle of Water big bottle\n" + "price 80")
            Selected = int(input("Select From 0-7"))
            if Selected == 0:
                money = int(input("Enter Your Money Balance"))
                order = money - 350
                print("You Successfully Order Your Pizza")
                print("Your Balance is now", + order)
            elif Selected == 1:
                money = int(input("Enter Your Money Balance"))
                order = 350 + 70 - money
                print("You Successfully Order Your Pizza")
                print("Your Balance is now", + order)
            elif Selected == 2:
                money = int(input("Enter Your Money Balance"))
                order = 350 + 70 - money
                print("You Successfully Order Your Pizza")
                print("Your Balance is now", + order)
            elif Selected == 3:
                money = int(input("Enter Your Money Balance"))
                order = 350 + 80 - money
                print("You Successfully Order Your Pizza")
                print("Your Balance is now", + order)
            elif Selected == 4:
                money = int(input("Enter Your Money Balance"))
                order = 350 + 40 - money
                print("You Successfully Order Your Pizza")
                print("Your Balance is now", + order)
            elif Selected == 5:
                money = int(input("Enter Your Money Balance"))
                order = 350 + 75 - money
                print("You Successfully Order Your Pizza")
                print("Your Balance is now", + order)
            elif Selected == 6:
                money = int(input("Enter Your Money Balance"))
                order = 350 + 100 - money
                print("You Successfully Order Your Pizza")
                print("Your Balance is now", + order)
            elif Selected == 7:
                money = int(input("Enter Your Money Balance"))
                order = 350 + 80 - money
                print("You Successfully Order Your Pizza")
                print("Your Balance is now", + order)
            else:
                print("Type From 0-7")
        elif Option == "No" or Option == "no":
            print("Take Your Time")
        else:
            print("Type Yes or No")
    # ----------------------------------------------------------------
    # Menu 4
    # ----------------------------------------------------------------
    elif selection == 4:
        print("--------------------------------------")
        print("----------You-Selected----------------")
        print("--------------------------------------")
        print("[4] Pizza With Bacon and bell pepper with cheese\n" + "price 390")
        Option = input("Are you sure you want to buy this? Yes or No")
        if Option == "Yes" or Option == "yes":
            print("--------------------------------------")
            print("-------------Add-Ons------------------")
            print("--------------------------------------")
            print("[0] No Add-Ons")
            print("[1] Coke\n" + "price 70")
            print("[2] Sprite\n" + "price 70")
            print("[3] Burger\n" + "price 80")
            print("[4] Fries small \n" + "price 40")
            print("[5] Fries medium \n" + "price 75")
            print("[6] Fries large \n" + "price 100")
            print("[7] Bottle of Water big bottle\n" + "price 80")
            Selected = int(input("Select From 0-7"))
            if Selected == 0:
                money = int(input("Enter Your Money Balance"))
                order = money - 390
                print("You Successfully Order Your Pizza")
                print("Your Balance is now", + order)
            elif Selected == 1:
                money = int(input("Enter Your Money Balance"))
                order = 390 + 70 - money
                print("You Successfully Order Your Pizza")
                print("Your Balance is now", + order)
            elif Selected == 2:
                money = int(input("Enter Your Money Balance"))
                order = 390 + 70 - money
                print("You Successfully Order Your Pizza")
                print("Your Balance is now", + order)
            elif Selected == 3:
                money = int(input("Enter Your Money Balance"))
                order = 390 + 80 - money
                print("You Successfully Order Your Pizza")
                print("Your Balance is now", + order)
            elif Selected == 4:
                money = int(input("Enter Your Money Balance"))
                order = 390 + 40 - money
                print("You Successfully Order Your Pizza")
                print("Your Balance is now", + order)
            elif Selected == 5:
                money = int(input("Enter Your Money Balance"))
                order = 390 + 75 - money
                print("You Successfully Order Your Pizza")
                print("Your Balance is now", + order)
            elif Selected == 6:
                money = int(input("Enter Your Money Balance"))
                order = 390 + 100 - money
                print("You Successfully Order Your Pizza")
                print("Your Balance is now", + order)
            elif Selected == 7:
                money = int(input("Enter Your Money Balance"))
                order = 390 + 80 - money
                print("You Successfully Order Your Pizza")
                print("Your Balance is now", + order)
            else:
                print("Type From 0-7")
        elif Option == "No" or Option == "no":
            print("Take Your Time")
        else:
            print("Type Yes or No")
    # ----------------------------------------------------------------
    # Menu 5
    # ----------------------------------------------------------------
    elif selection == 5:
        print("--------------------------------------")
        print("----------You-Selected----------------")
        print("--------------------------------------")
        print("[5] Hawaiian Pizza\n" + "price 500")
        Option = input("Are you sure you want to buy this? Yes or No")
        if Option == "Yes" or Option == "yes":
            print("--------------------------------------")
            print("-------------Add-Ons------------------")
            print("--------------------------------------")
            print("[0] No Add-Ons")
            print("[1] Coke\n" + "price 70")
            print("[2] Sprite\n" + "price 70")
            print("[3] Burger\n" + "price 80")
            print("[4] Fries small \n" + "price 40")
            print("[5] Fries medium \n" + "price 75")
            print("[6] Fries large \n" + "price 100")
            print("[7] Bottle of Water big bottle\n" + "price 80")
            Selected = int(input("Select From 0-7"))
            if Selected == 0:
                money = int(input("Enter Your Money Balance"))
                order = money - 500
                print("You Successfully Order Your Pizza")
                print("Your Balance is now", + order)
            elif Selected == 1:
                money = int(input("Enter Your Money Balance"))
                order = 500 + 70 - money
                print("You Successfully Order Your Pizza")
                print("Your Balance is now", + order)
            elif Selected == 2:
                money = int(input("Enter Your Money Balance"))
                order = 500 + 70 - money
                print("You Successfully Order Your Pizza")
                print("Your Balance is now", + order)
            elif Selected == 3:
                money = int(input("Enter Your Money Balance"))
                order = 500 + 80 - money
                print("You Successfully Order Your Pizza")
                print("Your Balance is now", + order)
            elif Selected == 4:
                money = int(input("Enter Your Money Balance"))
                order = 500 + 40 - money
                print("You Successfully Order Your Pizza")
                print("Your Balance is now", + order)
            elif Selected == 5:
                money = int(input("Enter Your Money Balance"))
                order = 500 + 75 - money
                print("You Successfully Order Your Pizza")
                print("Your Balance is now", + order)
            elif Selected == 6:
                money = int(input("Enter Your Money Balance"))
                order = 500 + 100 - money
                print("You Successfully Order Your Pizza")
                print("Your Balance is now", + order)
            elif Selected == 7:
                money = int(input("Enter Your Money Balance"))
                order = 500 + 80 - money
                print("You Successfully Order Your Pizza")
                print("Your Balance is now", + order)
            else:
                print("Type From 0-7")
        elif Option == "No" or Option == "no":
            print("Take Your Time")
        else:
            print("Type Yes or No")
    # ----------------------------------------------------------------
    # Menu 6
    # ----------------------------------------------------------------
    elif selection == 6:
        print("--------------------------------------")
        print("----------You-Selected----------------")
        print("--------------------------------------")
        print("[6] Buddy Pizza Bundle\n" + "price 600")
        Option = input("Are you sure you want to buy this? Yes or No")
        if Option == "Yes" or Option == "yes":
            print("--------------------------------------")
            print("-------------Add-Ons------------------")
            print("--------------------------------------")
            print("[0] No Add-Ons")
            print("[1] Coke\n" + "price 70")
            print("[2] Sprite\n" + "price 70")
            print("[3] Burger\n" + "price 80")
            print("[4] Fries small \n" + "price 40")
            print("[5] Fries medium \n" + "price 75")
            print("[6] Fries large \n" + "price 100")
            print("[7] Bottle of Water big bottle\n" + "price 80")
            Selected = int(input("Select From 0-7"))
            if Selected == 0:
                money = int(input("Enter Your Money Balance"))
                order = money - 500
                print("You Successfully Order Your Pizza")
                print("Your Balance is now", + order)
            elif Selected == 1:
                money = int(input("Enter Your Money Balance"))
                order = 600 + 70 - money
                print("You Successfully Order Your Pizza")
                print("Your Balance is now", + order)
            elif Selected == 2:
                money = int(input("Enter Your Money Balance"))
                order = 600 + 70 - money
                print("You Successfully Order Your Pizza")
                print("Your Balance is now", + order)
            elif Selected == 3:
                money = int(input("Enter Your Money Balance"))
                order = 600 + 80 - money
                print("You Successfully Order Your Pizza")
                print("Your Balance is now", + order)
            elif Selected == 4:
                money = int(input("Enter Your Money Balance"))
                order = 600 + 40 - money
                print("You Successfully Order Your Pizza")
                print("Your Balance is now", + order)
            elif Selected == 5:
                money = int(input("Enter Your Money Balance"))
                order = 600 + 75 - money
                print("You Successfully Order Your Pizza")
                print("Your Balance is now", + order)
            elif Selected == 6:
                money = int(input("Enter Your Money Balance"))
                order = 600 + 100 - money
                print("You Successfully Order Your Pizza")
                print("Your Balance is now", + order)
            elif Selected == 7:
                money = int(input("Enter Your Money Balance"))
                order = 600 + 80 - money
                print("You Successfully Order Your Pizza")
                print("Your Balance is now", + order)
            else:
                print("Type From 0-7")
        elif Option == "No" or Option == "no":
            print("Take Your Time")
        else:
            print("Type Yes or No")
    # ----------------------------------------------------------------
    # Menu 7
    # ----------------------------------------------------------------
    elif selection == 7:
        print("--------------------------------------")
        print("----------You-Selected----------------")
        print("--------------------------------------")
        print("[7] Chicago Pizza Style\n" + "price 650")
        Option = input("Are you sure you want to buy this? Yes or No")
        if Option == "Yes" or Option == "yes":
            print("--------------------------------------")
            print("-------------Add-Ons------------------")
            print("--------------------------------------")
            print("[0] No Add-Ons")
            print("[1] Coke\n" + "price 70")
            print("[2] Sprite\n" + "price 70")
            print("[3] Burger\n" + "price 80")
            print("[4] Fries small \n" + "price 40")
            print("[5] Fries medium \n" + "price 75")
            print("[6] Fries large \n" + "price 100")
            print("[7] Bottle of Water big bottle\n" + "price 80")
            Selected = int(input("Select From 0-7"))
            if Selected == 0:
                money = int(input("Enter Your Money Balance"))
                order = money - 650
                print("You Successfully Order Your Pizza")
                print("Your Balance is now", + order)
            elif Selected == 1:
                money = int(input("Enter Your Money Balance"))
                order = 650 + 70 - money
                print("You Successfully Order Your Pizza")
                print("Your Balance is now", + order)
            elif Selected == 2:
                money = int(input("Enter Your Money Balance"))
                order = 650 + 70 - money
                print("You Successfully Order Your Pizza")
                print("Your Balance is now", + order)
            elif Selected == 3:
                money = int(input("Enter Your Money Balance"))
                order = 650 + 80 - money
                print("You Successfully Order Your Pizza")
                print("Your Balance is now", + order)
            elif Selected == 4:
                money = int(input("Enter Your Money Balance"))
                order = 650 + 40 - money
                print("You Successfully Order Your Pizza")
                print("Your Balance is now", + order)
            elif Selected == 5:
                money = int(input("Enter Your Money Balance"))
                order = 650 + 75 - money
                print("You Successfully Order Your Pizza")
                print("Your Balance is now", + order)
            elif Selected == 6:
                money = int(input("Enter Your Money Balance"))
                order = 650 + 100 - money
                print("You Successfully Order Your Pizza")
                print("Your Balance is now", + order)
            elif Selected == 7:
                money = int(input("Enter Your Money Balance"))
                order = 650 + 80 - money
                print("You Successfully Order Your Pizza")
                print("Your Balance is now", + order)
            else:
                print("Type From 0-7")
        elif Option == "No" or Option == "no":
            print("Take Your Time")
        else:
            print("Type Yes or No")
    # ----------------------------------------------------------------
    # Menu 8
    # ----------------------------------------------------------------
    elif selection == 8:
        print("--------------------------------------")
        print("----------You-Selected----------------")
        print("--------------------------------------")
        print("[8] Crust Pizza with all of toppings like cheese, pineapple and etc\n" + "price 700")
        Option = input("Are you sure you want to buy this? Yes or No")
        if Option == "Yes" or Option == "yes":
            print("--------------------------------------")
            print("-------------Add-Ons------------------")
            print("--------------------------------------")
            print("[0] No Add-Ons")
            print("[1] Coke\n" + "price 70")
            print("[2] Sprite\n" + "price 70")
            print("[3] Burger\n" + "price 80")
            print("[4] Fries small \n" + "price 40")
            print("[5] Fries medium \n" + "price 75")
            print("[6] Fries large \n" + "price 100")
            print("[7] Bottle of Water big bottle\n" + "price 80")
            Selected = int(input("Select From 0-7"))
            if Selected == 0:
                money = int(input("Enter Your Money Balance"))
                order = money - 700
                print("You Successfully Order Your Pizza")
                print("Your Balance is now", + order)
            elif Selected == 1:
                money = int(input("Enter Your Money Balance"))
                order = 700 + 70 - money
                print("You Successfully Order Your Pizza")
                print("Your Balance is now", + order)
            elif Selected == 2:
                money = int(input("Enter Your Money Balance"))
                order = 700 + 70 - money
                print("You Successfully Order Your Pizza")
                print("Your Balance is now", + order)
            elif Selected == 3:
                money = int(input("Enter Your Money Balance"))
                order = 700 + 80 - money
                print("You Successfully Order Your Pizza")
                print("Your Balance is now", + order)
            elif Selected == 4:
                money = int(input("Enter Your Money Balance"))
                order = 700 + 40 - money
                print("You Successfully Order Your Pizza")
                print("Your Balance is now", + order)
            elif Selected == 5:
                money = int(input("Enter Your Money Balance"))
                order = 700 + 75 - money
                print("You Successfully Order Your Pizza")
                print("Your Balance is now", + order)
            elif Selected == 6:
                money = int(input("Enter Your Money Balance"))
                order = 700 + 100 - money
                print("You Successfully Order Your Pizza")
                print("Your Balance is now", + order)
            elif Selected == 7:
                money = int(input("Enter Your Money Balance"))
                order = 700 + 80 - money
                print("You Successfully Order Your Pizza")
                print("Your Balance is now", + order)
            else:
                print("Type From 0-7")
        elif Option == "No" or Option == "no":
            print("Take Your Time")
        else:
            print("Type Yes or No")
    # ----------------------------------------------------------------
    # Menu 9
    # ----------------------------------------------------------------
    elif selection == 9:
        print("--------------------------------------")
        print("----------You-Selected----------------")
        print("--------------------------------------")
        print("[9] Italian Pizza Style\n" + "price 800")
        Option = input("Are you sure you want to buy this? Yes or No")
        if Option == "Yes" or Option == "yes":
            print("--------------------------------------")
            print("-------------Add-Ons------------------")
            print("--------------------------------------")
            print("[0] No Add-Ons")
            print("[1] Coke\n" + "price 70")
            print("[2] Sprite\n" + "price 70")
            print("[3] Burger\n" + "price 80")
            print("[4] Fries small \n" + "price 40")
            print("[5] Fries medium \n" + "price 75")
            print("[6] Fries large \n" + "price 100")
            print("[7] Bottle of Water big bottle\n" + "price 80")
            Selected = int(input("Select From 0-7"))
            if Selected == 0:
                money = int(input("Enter Your Money Balance"))
                order = money - 800
                print("You Successfully Order Your Pizza")
                print("Your Balance is now", + order)
            elif Selected == 1:
                money = int(input("Enter Your Money Balance"))
                order = 800 + 70 - money
                print("You Successfully Order Your Pizza")
                print("Your Balance is now", + order)
            elif Selected == 2:
                money = int(input("Enter Your Money Balance"))
                order = 800 + 70 - money
                print("You Successfully Order Your Pizza")
                print("Your Balance is now", + order)
            elif Selected == 3:
                money = int(input("Enter Your Money Balance"))
                order = 800 + 80 - money
                print("You Successfully Order Your Pizza")
                print("Your Balance is now", + order)
            elif Selected == 4:
                money = int(input("Enter Your Money Balance"))
                order = 800 + 40 - money
                print("You Successfully Order Your Pizza")
                print("Your Balance is now", + order)
            elif Selected == 5:
                money = int(input("Enter Your Money Balance"))
                order = 800 + 75 - money
                print("You Successfully Order Your Pizza")
                print("Your Balance is now", + order)
            elif Selected == 6:
                money = int(input("Enter Your Money Balance"))
                order = 800 + 100 - money
                print("You Successfully Order Your Pizza")
                print("Your Balance is now", + order)
            elif Selected == 7:
                money = int(input("Enter Your Money Balance"))
                order = 800 + 80 - money
                print("You Successfully Order Your Pizza")
                print("Your Balance is now", + order)
            else:
                print("Type From 0-7")
        elif Option == "No" or Option == "no":
            print("Take Your Time")
        else:
            print("Type Yes or No")
    # ----------------------------------------------------------------
    # Menu 10
    # ----------------------------------------------------------------
    elif selection == 10:
        print("--------------------------------------")
        print("----------You-Selected----------------")
        print("--------------------------------------")
        print("[10] Unlimited Pizza Bundle with drinks\n" + "price 1000 per 5 person")
        Option = input("Are you sure you want to buy this? Yes or No")
        if Option == "Yes" or Option == "yes":
            print("--------------------------------------")
            print("-------------Add-Ons------------------")
            print("--------------------------------------")
            print("[0] No Add-Ons")
            print("[1] Coke\n" + "price 70")
            print("[2] Sprite\n" + "price 70")
            print("[3] Burger\n" + "price 80")
            print("[4] Fries small \n" + "price 40")
            print("[5] Fries medium \n" + "price 75")
            print("[6] Fries large \n" + "price 100")
            print("[7] Bottle of Water big bottle\n" + "price 80")
            Selected = int(input("Select From 0-7"))
            if Selected == 0:
                money = int(input("Enter Your Money Balance"))
                order = money - 1000
                print("You Successfully Order Your Pizza")
                print("Your Balance is now", + order)
            elif Selected == 1:
                money = int(input("Enter Your Money Balance"))
                order = 1000 + 70 - money
                print("You Successfully Order Your Pizza")
                print("Your Balance is now", + order)
            elif Selected == 2:
                money = int(input("Enter Your Money Balance"))
                order = 1000 + 70 - money
                print("You Successfully Order Your Pizza")
                print("Your Balance is now", + order)
            elif Selected == 3:
                money = int(input("Enter Your Money Balance"))
                order = 1000 + 80 - money
                print("You Successfully Order Your Pizza")
                print("Your Balance is now", + order)
            elif Selected == 4:
                money = int(input("Enter Your Money Balance"))
                order = 1000 + 40 - money
                print("You Successfully Order Your Pizza")
                print("Your Balance is now", + order)
            elif Selected == 5:
                money = int(input("Enter Your Money Balance"))
                order = 1000 + 75 - money
                print("You Successfully Order Your Pizza")
                print("Your Balance is now", + order)
            elif Selected == 6:
                money = int(input("Enter Your Money Balance"))
                order = 1000 + 100 - money
                print("You Successfully Order Your Pizza")
                print("Your Balance is now", + order)
            elif Selected == 7:
                money = int(input("Enter Your Money Balance"))
                order = 1000 + 80 - money
                print("You Successfully Order Your Pizza")
                print("Your Balance is now", + order)
            else:
                print("Type From 0-7")
        elif Option == "No" or Option == "no":
            print("Take Your Time")
        else:
            print("Type Yes or No")
    # ----------------------------------------------------------------
    # Logout
    # ----------------------------------------------------------------
    elif selection == 0:
        Option = input("Are You Sure You Want to Logout? Yes or no")
        if Option == "Yes" or Option == "yes":
            print("You Successfully Logged Out")
        else:
            print("Welcome User User8904")
            print("Welcome To Pizza Ordering System")
            print("[0] Logout")
            print("Select To Order\n" + "[0] Exit\n" + "[1] Pizza Peperoni with Pineapple\n" + "Price 200")
            print("[2] Pizza With Bacon and bell pepper with cheese\n" + "price 290")
            print("[3] Pizza With beef and bell pepper with cheese\n" + "price 350")
            print("[4] Pizza With Bacon and bell pepper with cheese\n" + "price 390")
            print("[5] Hawaiian Pizza\n" + "price 400")
            print("[6] Buddy Pizza Bundle\n" + "price 600")
            print("[7] Chicago Pizza Style\n" + "price 650")
            print("[8] Crust Pizza with all of toppings like cheese, pineapple and etc\n" + "price 700")
            print("[9] Italian Pizza Style\n" + "price800")
            print("[10] Unlimited Pizza Bundle with drinks\n" + "price 1000 per 5 person")

    else:
        print("Select From 0-10")
# ----------------------------------------------------------------
# Username and Password Incorrect
# ----------------------------------------------------------------
elif Username != "User8904" and Password != "username4232":
    print("Username or Password is Incorrect")
# ----------------------------------------------------------------
# No Account Stored in the DATABASE
# ----------------------------------------------------------------
else:
    print("No Account Found")
