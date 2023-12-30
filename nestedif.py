username = input("Enter Your Username")
password = input("Enter Your Password")
verification = int(input("Enter Your Verification Code"))

if username == "Wenwen123" or password == "Putobong2x" or verification == 95032 or username == "pam2x90" and password  == "putobongs2x" and verification == 90323:
    print("Username, Password or verification code is incorrect")

    if username == "Wenwen123" and password == "Putobong2x" and 95032 == verification:
      print("Welcome User Wenwen123")

    elif username == "pam2x90" and password == "putobongs2x" and 90323 == verification:
      print("No User Found")
else:
    print("Username, Password or verification code is incorrect")