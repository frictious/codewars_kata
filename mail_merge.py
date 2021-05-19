arr = [] # List to hold all the names of the inviteed

with open("./Inputs/Names/invited_names.txt", "r") as invitees: # Opening the invitees text file in read mode
    for names in invitees:
        arr.append(names.strip()) # Adding / Appending the invitees names to the list and stripping \n in the process

with open("./Inputs/Letters/starting_letter.txt", "r") as files: # Going through the letter in read mode
    letter = files.read() # Passing the full letter in the file to the letter variable
    for name in arr:
        lets = letter.replace("[name],", f"{name},") # Passing the new letter with replaced [name] for invitees name to the variable lets
        with open(f"./Output/Ready to send/letter_for_{name}.txt", "w") as letters:
            letters.write(lets) # Passing the lets as an argument to the invitation letters being written
