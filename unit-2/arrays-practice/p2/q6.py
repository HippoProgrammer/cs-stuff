letters = ['H', 'E', 'L', 'L', 'O']
shift = 3
encrypted = []

for letter in letters:
    # Convert letter to ASCII code
    code = ord(letter)
    
    # Shift the code
    new_code = code + shift
    
    # Convert back to character
    new_letter = chr(new_code)
    encrypted.append(new_letter)

print("Original:", letters)
print("Encrypted:", encrypted)
