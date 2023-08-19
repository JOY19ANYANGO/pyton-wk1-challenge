def consonant_value(s):
    consonants = 'bcdfghjklmnpqrstvwxyz'
    highest_value = 0
    current_value = 0
    
    for char in s:
        if char in consonants:
            current_value += ord(char) - ord('a') + 1
            highest_value = max(highest_value, current_value)
        else:
            current_value = 0
    
    return highest_value

# Example usage
input_string = "abcd"
result = consonant_value(input_string)
print(result)  # Output: 4
