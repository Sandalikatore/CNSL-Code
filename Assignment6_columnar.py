def simple_columnar_encrypt(text, key):
    columns = [''] * key
    for i, char in enumerate(text):
        columns[i % key] += char
    return ''.join(columns)

def simple_columnar_decrypt(cipher, key):
    num_rows = len(cipher) // key
    extra_chars = len(cipher) % key
    rows = [''] * num_rows
    idx = 0
    for col in range(key):
        length = num_rows + (1 if col < extra_chars else 0)
        for row in range(length):
            rows[row] += cipher[idx]
            idx += 1
    return ''.join(rows)

# Example Usage
text = "HELLO WORLD"
key = 3
encrypted = simple_columnar_encrypt(text, key)
decrypted = simple_columnar_decrypt(encrypted, key)
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
