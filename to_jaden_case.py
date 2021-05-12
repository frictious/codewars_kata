def to_jaden_case(string):
    # Creating a set of variables to hold space, counter, and the new word
    space = " " #Holds a space value which will later be used to check if we are currently on a letter that comes after a space
    count = 0 # Keeps count of the current string index that we are on
    word = "" # This will be the new sentence that will be returned
    
    #A for loop to go through all the characters in the string
    for character in string:
        # Checking if the previous character was an empty space
        if string[count - 1] == space and character != space:
            word += character.upper() #Converting the current character to an uppercase and adding it to the word variable
        else:
            word += character #If the new word is is not a space, we add the lowercased characrter to the word variable
        count += 1 # Incrementing count by 1
        
    return word # Returning the newly formed word/sentence