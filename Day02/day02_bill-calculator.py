# Bill calculator considering the tip amount and number of people
print("Welcome to the tip calculator!")

total_bill = float(input("What was the total bill? $"))
tip_percentage = int(input("How much tip would you like to give? 10%, 12%, or 15%? "))
people = int(input("How many people to split the bill? "))

tip_amount = total_bill * (tip_percentage / 100)
total_amount = total_bill + tip_amount
each_person_pay = total_amount / people
each_person_pay = "{:.2f}".format(each_person_pay) #to limit the decimal places to 2

print(f"Each person should pay: ${each_person_pay}")
