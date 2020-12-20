print("Welcome to Tip and Bill Split Calculator")

bill = float(input("What was the total bill? \t$"))

tip = int(input("What percentage tip would you like to give? 10,12, or 15? \t"))

ppl = int(input("How many people to split the bill?\t"))

amount = (bill*(1+tip/100))/ppl
print(f"Each person should pay: ${amount:.2f}")