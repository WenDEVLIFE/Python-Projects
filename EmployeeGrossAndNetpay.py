Employee_Name: str = input("Enter Your Name")
Rate: float = int(input("Enter Your Rate/Hour"))
Total_Hour = int(input("Enter Your Total Hour"))
Total_Overtime = int(input("Enter Your Total Overtime Hour"))

Gross: float = (Total_Hour * Rate) + ((Rate * 20) * Total_Overtime)
if Gross >= 10000:
    Net1: float = (Gross * 12) / 100
    Net2: float = Gross - Net1
    print("Your Employee Name is:" + Employee_Name)
    print("Your Rate is:", Rate)
    print("Your Total Hour is:", Total_Hour)
    print("Your Total Overtime is:", Total_Overtime)
    print("Your Gross payment is:", Gross)
    print("Your Net pay is:", Net2)
else:
    print("Your Employee Name is:" + Employee_Name)
    print("Your Rate is:", Rate)
    print("Your Total Hour is:", Total_Hour)
    print("Your Total Overtime is:", Total_Overtime)
    print("Your Gross payment is:", Gross)
