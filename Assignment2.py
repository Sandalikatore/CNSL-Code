def polyalphabetic_cipher(text, key, mode='encrypt'):
    key = key.upper()
    result = ""
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index]) - 65
            if mode == 'decrypt':
                shift = -shift
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
            key_index = (key_index + 1) % len(key)
        else:
            result += char
    return result

# Example Usage
text = "HELLO WORLD"
key = "KEY"
encrypted = polyalphabetic_cipher(text, key)
decrypted = polyalphabetic_cipher(encrypted, key, mode='decrypt')
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
