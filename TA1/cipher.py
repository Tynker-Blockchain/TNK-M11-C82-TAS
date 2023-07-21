capitalLetters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowerLetters='abcdefghijklmnopqrstuvwxyz'
numbers='0123456789'

# Define the function cipher() that takes two parameter i.e 'plaintext' and a key 'n'
def cipher(plaintext, n):
    # Access globals: capitalLetters, lowerLetters, numbers
    global  capitalLetters, lowerLetters, numbers
    # Create empty string variable cipherText
    cipherText = ''

    # Loop throught each 'char' in the 'plaintext'
    for char in plaintext:
        # Check if 'char' is present in 'numnbers' list
        if char in numbers:
            # Get the current position of the 'char' in 'numbers' list
            currentPosition = numbers.find(char)
            # Calculate the character using formula : numbers[(currentPosition + n ) % 10] and add it to cipherText
            cipherText += numbers[(currentPosition + n ) % 10]
        # Else add the 'char' to 'cipherText'
        else:
            cipherText += char
    
    # Return 'cipherText'
    return cipherText
        
