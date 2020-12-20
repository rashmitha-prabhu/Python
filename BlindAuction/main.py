import art
import subprocess as sp

print(art.logo)
print("WELCOME TO SECRET AUCTION PROGRAM")

bidders = {}
proceed = True

while proceed:
    name = input("\nEnter your name : \t")
    bid = int(input("Enter your bid: \t$"))

    bidders[name] = bid

    flag = input("Any other bidders? (Y/N)\t: ")
    if flag.lower() == "n":
        proceed = False
    tmp = sp.call('clear', shell=True)

maximum = 0
name = ""

for key in bidders:
    if bidders[key] > maximum:
        maximum = bidders[key]
        name = key

print(f"\n{name} won the bid at ${maximum}\n")