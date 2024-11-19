def rail_fence_encrypt(text, key):
    rail = [['\n' for _ in range(len(text))] for _ in range(key)]
    direction_down = False
    row, col = 0, 0
    for char in text:
        rail[row][col] = char
        col += 1
        if row == 0 or row == key - 1:
            direction_down = not direction_down
        row += 1 if direction_down else -1
    return ''.join(''.join(rail[i][j] for j in range(len(text)) if rail[i][j] != '\n') for i in range(key))

def rail_fence_decrypt(cipher, key):
    rail = [['\n' for _ in range(len(cipher))] for _ in range(key)]
    direction_down = None
    row, col = 0, 0
    for _ in cipher:
        rail[row][col] = '*'
        col += 1
        if row == 0 or row == key - 1:
            direction_down = not direction_down
        row += 1 if direction_down else -1
    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if rail[i][j] == '*' and index < len(cipher):
                rail[i][j] = cipher[index]
                index += 1
    result = []
    row, col = 0, 0
    for _ in range(len(cipher)):
        result.append(rail[row][col])
        col += 1
        if row == 0 or row == key - 1:
            direction_down = not direction_down
        row += 1 if direction_down else -1
    return ''.join(result)

# Example Usage
text = "HELLO WORLD"
key = 3
encrypted = rail_fence_encrypt(text, key)
decrypted = rail_fence_decrypt(encrypted, key)
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
