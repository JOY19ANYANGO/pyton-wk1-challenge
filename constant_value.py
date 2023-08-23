'''pseudocode
  Define a function consonant_value that takes input_string as parameter.
  Create a variable consonants which is a string  containing all consonants.
  Create a variable highest_value and  current_value and assign them initial value of 0.These varaibles keep track of consonant value.
  Loop through letters in input_string.If the letter is a consonant add consonant value  to current value.IF it is a vowel set consonant value to 0.
  Return the highest_value'''
  
def consonant_value(input_string):
    # contains all consonants
    consonants = 'bcdfghjklmnpqrstvwxyz'
    # keep track of highest consonant value
    highest_value = 0
    current_value = 0
    
    # loops through letters
    for letter in input_string:
        # check if letter is a consonant
        if letter in consonants:
            # calculate the value of consonant according to position and add to the current_value
            current_value += ord(letter) - ord('a') + 1
            # compares highest_value and current_value and updates highest_value to be the max value
            highest_value = max(highest_value, current_value)
        # sets current_value to 0 if the letter is a vowel    
        else:
            current_value = 0
    
    return highest_value

# Example usage
result = consonant_value("abcd")
print(result)  
result1 = consonant_value( "strength")
print(result1)  
result2 = consonant_value("zodiacs" )
print(result2)  
