def advanced_columnar_encrypt(text, key):
    key_order = sorted((val, i) for i, val in enumerate(key))
    columns = [''] * len(key)
    for i, char in enumerate(text):
        columns[i % len(key)] += char
    return ''.join(columns[i] for _, i in key_order)

def advanced_columnar_decrypt(cipher, key):
    key_order = sorted((val, i) for i, val in enumerate(key))
    column_lengths = [len(cipher) // len(key)] * len(key)
    for i in range(len(cipher) % len(key)):
        column_lengths[key_order[i][1]] += 1
    columns = []
    idx = 0
    for length in column_lengths:
        columns.append(cipher[idx:idx + length])
        idx += length
    result = ''
    for i in range(max(column_lengths)):
        for _, col in key_order:
            if i < len(columns[col]):
                result += columns[col][i]
    return result

# Example Usage
text = "HELLO WORLD"
key = "4312"
encrypted = advanced_columnar_encrypt(text, key)
decrypted = advanced_columnar_decrypt(encrypted, key)
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
