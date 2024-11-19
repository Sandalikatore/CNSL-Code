# Helper Functions
def prepare_key(key):
    key = ''.join(sorted(set(key), key=lambda x: key.index(x)))
    key = key.replace('J', 'I')
    return key + ''.join(chr(i) for i in range(65, 91) if chr(i) not in key and chr(i) != 'J')

def find_position(char, matrix):
    for i, row in enumerate(matrix):
        for j, val in enumerate(row):
            if char == val:
                return i, j
    return None

def playfair_cipher(text, key, mode='encrypt'):
    key = prepare_key(key.upper())
    matrix = [key[i:i + 5] for i in range(0, 25, 5)]
    text = text.upper().replace("J", "I").replace(" ", "")
    if len(text) % 2 != 0:
        text += "X"
    result = ""
    for i in range(0, len(text), 2):
        a, b = text[i], text[i + 1]
        row1, col1 = find_position(a, matrix)
        row2, col2 = find_position(b, matrix)
        if row1 == row2:
            if mode == 'encrypt':
                result += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
            else:
                result += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            if mode == 'encrypt':
                result += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
            else:
                result += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
        else:
            result += matrix[row1][col2] + matrix[row2][col1]
    return result

# Example Usage
text = "HELLO WORLD"
key = "LDRP"
encrypted = playfair_cipher(text, key)
decrypted = playfair_cipher(encrypted, key, mode='decrypt')
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
