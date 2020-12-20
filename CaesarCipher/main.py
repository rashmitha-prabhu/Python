import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def caesar(direction, text, shift):
    msg = ""
    for letter in text:
        if letter not in alphabet:
            msg += letter
            continue
        pos = alphabet.index(letter)
        n = len(alphabet)
        if direction.lower() == "encode":
            msg += alphabet[(pos+shift) % n]
        elif direction.lower() == "decode":
            msg += alphabet[abs(pos+n-shift) % n]
    print(f"The {direction.lower()}d text is {msg}")


print(art.logo)


def inputs():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(direction, text, shift)


def check(restart):
    if restart.lower() == "yes":
        inputs()
        check(input("\n\nType 'yes' to go again, else type 'no':\n"))
    else:
        print("\n\nGood bye\n")


check("yes")
