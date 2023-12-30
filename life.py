life = input("Are You Ok?")
if life == "Yes" or life == "yes":
    print("Keep up your dreams")
    print("Dont Give Up")
    print("Keep Fighting ok?")
    print("Life must go on and ")
    print("Anything gonna be alright")
    num1 = int(input("Select from 1 or 2"))
    if num1 == 1:
        list1 = ["fight", "survive", "follow your dreams", "live on"]
        a = list1
        print("Here are the list to follow")
        print(a)
        print("Just Keep Dreaming and Dreaming until you achieve your goal")
        print("No Matter What Problem you are facing right know")
        print("Just Go onn with the things you love to do")
    elif num1 == 2:
        print("No Matter what your weakness and strength")
        print("Just Keep Fighting")
        print("Don't Compare Yourself To Others")
        print("Because Other people has own talents and skills")
        print("Just show yourself and don't be shy for who you are!")
    else:
        print("Select From 1 - 2")
elif life == "No" or life == "no":
    print("Life must go on and live for it")
    print("Without Sacrafice and hardship will would be easy")
    print("Keep fighting and follow your dreams")
    print("Thats all, Thank You and Take Care of Yourself!")
else:
    print("Select Yes/No or lowercase of yes and no")
