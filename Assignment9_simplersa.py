def rsa_encrypt_decrypt(p, q, e, plaintext):
    n = p * q
    phi = (p - 1) * (q - 1)
    d = pow(e, -1, phi)
    ciphertext = [pow(ord(char), e, n) for char in plaintext]
    decrypted_text = ''.join(chr(pow(c, d, n)) for c in ciphertext)
    return ciphertext, decrypted_text

# Example Usage
p, q, e = 61, 53, 17  # p and q are primes; e is the public key exponent
plaintext = "HELLO"
ciphertext, decrypted = rsa_encrypt_decrypt(p, q, e, plaintext)
print("Ciphertext:", ciphertext)
print("Decrypted Text:", decrypted)
