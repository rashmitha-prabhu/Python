n = int(input("Make a guess : "))
    if n>num:
        print("Too HIGH")
    elif n<num:
        print("Too LOW")
    else:
        print("You guessed it! Congratulations!")
        exit()