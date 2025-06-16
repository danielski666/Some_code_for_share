#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Names/invited_names.txt") as name_file:
    names = name_file.readlines()
    for name in names:
        with open("Input/Letters/starting_letter.txt") as letter:
            lines = letter.readlines()
        with open(f"Output/ReadyToSend/letter_for_{name.strip()}.txt", "a") as ready_letter:
            for line in lines:
                ready_letter.write(line.replace("[name]", name.strip()) if "[name]" in line else line)

