def diffie_hellman(p, g, private_key_a, private_key_b):
    public_key_a = (g ** private_key_a) % p
    public_key_b = (g ** private_key_b) % p
    shared_key_a = (public_key_b ** private_key_a) % p
    shared_key_b = (public_key_a ** private_key_b) % p
    return shared_key_a, shared_key_b

# Example Usage
p = 23  # Prime number
g = 5   # Primitive root
private_key_a = 6
private_key_b = 15
shared_key_a, shared_key_b = diffie_hellman(p, g, private_key_a, private_key_b)
print("Shared Key A:", shared_key_a)
print("Shared Key B:", shared_key_b)
