print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $")),
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
split = int(input("How many people to split the bill? "))
splitBill = (bill[0] / split)
tip /= 100
roundNum = splitBill * tip
roundNum = round(roundNum, 2)
splitBill = round(splitBill, 2)
splitBill += roundNum
print("Each person should pay: ${:.2f}".format(splitBill))
