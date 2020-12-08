import art
from game_data import data
import random
import subprocess as sp

score =0
chosen = []

def choose():
    n = random.randint(0,len(data)-1)
    if n not in chosen:
        chosen.append(n)
        return n
    while n in chosen:
        n = random.randint(0,len(data)-1)
    chosen.append(n)
    return n

def describe(n):
    return (f"{data[n]['name']}, a {data[n]['description']} from {data[n]['country']}")

def compare(ch1,ch2):
    if data[ch1]['follower_count'] > data[ch2]['follower_count']:
        return "a"
    return "b"

ch1 = choose()
print(ch1)
ch2 = choose()
print(ch2)

game = True

while game:
    tmp = sp.call('clear', shell=True)
    print(art.logo)
    print(f"\nCurrent Score : {score}")
    print(f"\n\nCompare A: {describe(ch1)}")
    print(art.vs)
    print(f"\nAgainst B : {describe(ch2)}")

    choice = input("Who has more Instagram followers (A/B) : ")

    if choice.lower() == compare(ch1,ch2):
        score+=1
        ch1=ch2
        ch2=choose()
    
    else:
        tmp = sp.call('clear', shell=True)
        print(art.logo)
        print("\nSorry, Thats wrong")
        print(f"\nFinal Score : {score}")
        game = False
