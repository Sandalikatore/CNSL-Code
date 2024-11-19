import numpy as np

def hill_cipher_encrypt(text, key_matrix):
    n = len(key_matrix)
    text = text.upper().replace(" ", "")
    
    # Ensure text length is a multiple of the matrix size
    while len(text) % n != 0:
        text += "X"
    
    # Split text into chunks
    chunks = [text[i:i + n] for i in range(0, len(text), n)]
    
    result = ""
    for chunk in chunks:
        # Convert chunk to numerical vector
        vector = np.array([ord(c) - 65 for c in chunk]).reshape(-1, 1)
        # Multiply with the key matrix
        transformed = np.dot(key_matrix, vector) % 26
        # Convert back to text
        result += ''.join(chr(int(x) + 65) for x in transformed.flatten())
    return result

def hill_cipher_decrypt(cipher, key_matrix):
    n = len(key_matrix)
    # Calculate the inverse of the key matrix modulo 26
    det = int(np.round(np.linalg.det(key_matrix))) % 26
    det_inv = pow(det, -1, 26)  # Modular multiplicative inverse
    adjugate = np.round(det * np.linalg.inv(key_matrix)).astype(int) % 26
    inverse_key_matrix = (det_inv * adjugate) % 26

    # Decrypt using the inverse key matrix
    return hill_cipher_encrypt(cipher, inverse_key_matrix)

# Example Usage
text = "HELLO"
key_matrix = np.array([[6, 24, 1], [13, 16, 10], [20, 17, 15]])  # 3x3 key matrix

encrypted = hill_cipher_encrypt(text, key_matrix)
decrypted = hill_cipher_decrypt(encrypted, key_matrix)

print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
