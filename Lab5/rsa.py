import random
import math

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def inverse(e, phi_n):
    """Find the modular multiplicative inverse of e modulo phi_n."""
    for d in range(3, phi_n):
        if (d * e) % phi_n == 1:
            return d
    raise ValueError("Could not generate the inverse")

def generate_prime(min_n, max_n):
    """Generate a random prime number between min_n and max_n."""
    while True:
        p = random.randint(min_n, max_n)
        if is_prime(p):
            return p

def generate_public_key(phi_n):
    """Generate a public key 'e' such that 1 < e < phi_n and gcd(e, phi_n) == 1."""
    e = random.randint(3, phi_n - 1)
    while math.gcd(e, phi_n) != 1:
        e = random.randint(3, phi_n - 1)
    return e

def generate_private_key(e, phi_n):
    """Generate the private key 'd' as the modular multiplicative inverse of 'e' modulo phi_n."""
    return inverse(e, phi_n)

if __name__ == "__main__":
    p = generate_prime(3, 500)
    q = generate_prime(3, 500)
    n = p * q
    phi_n = (p - 1) * (q - 1)

    e = generate_public_key(phi_n)
    d = generate_private_key(e, phi_n)

    original_message = "Cusnir Mihaela"
    print(f"Original Message: {original_message}")

    message_decimal = [ord(c) for c in original_message]
    print(f"Converted message to decimal: {''.join(str(c) for c in message_decimal)}")

    cipher_text = [pow(c, e, n) for c in message_decimal]
    print(f"Cipher text is: {''.join(str(c) for c in cipher_text)}")

    decrypted_message_decimal = [pow(c, d, n) for c in cipher_text]
    print(f"Converted decrypted message to decimal: {''.join(str(c) for c in decrypted_message_decimal)}")

    decrypted_message = "".join(chr(c) for c in decrypted_message_decimal)
    print(f"Decrypted Message: {decrypted_message}")
