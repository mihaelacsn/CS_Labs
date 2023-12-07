import random

p = 32317006071311007300153513477825163362488057133489075174588434139269806834136210002792056362640164685458556357935330816928829023080573472625273554742461245741026202527916572972862706300325263428213145766931414223654220941111348629991657478268034230553086349050635557712219187890332729569696129743856241741236237225197346402691855797767976823014625397933058015226858730761197532436467475855460715043896844940366130497697812854295958659597567051283852132784468522925504568272879113720098931873959143374175837826000278034973198552060607533234122603254684088120031105907484281003994966956119696956248629032338072839127039

g = 2

def generate_private_key(modulus):
    return random.randint(1, modulus - 1)

def compute_public_key(base, private_key, modulus):
    return pow(base, private_key, modulus)

def calculate_shared_secret_key(public_key, private_key, modulus):
    return pow(public_key, private_key, modulus)

# Generate random private keys 
Alice_private_key = generate_private_key(p)
Bob_private_key = generate_private_key(p)

# Compute public keys
Alice_public_key = compute_public_key(g, Alice_private_key, p)
Bob_public_key = compute_public_key(g, Bob_private_key, p)

# Calculate shared secret keys
shared_secret_key_Alice = calculate_shared_secret_key(Bob_public_key, Alice_private_key, p)
shared_secret_key_Bob = calculate_shared_secret_key(Alice_public_key, Bob_private_key, p)

# Check if the shared secret keys match
print(f"Result: {shared_secret_key_Alice == shared_secret_key_Bob}")
