def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    if mode == 'decrypt':
        shift = -shift
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

# Example Usage
text = "HELLO WORLD"
shift = 3
encrypted = caesar_cipher(text, shift)
decrypted = caesar_cipher(encrypted, shift, mode='decrypt')
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
