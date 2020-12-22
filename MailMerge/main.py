with open("Input/Names/invited_names.txt", "r") as names:
    guests = []
    for name in names.readlines():
        guests.append(name.strip("\n"))

with open("Input/Letters/starting_letter.docx") as letter:
    contents = letter.read()
    for guest in guests:
        with open(f"Output/ReadyToSend/{guest}.docx", "w") as invite:
            invite.write(contents.replace("[name]", guest))
