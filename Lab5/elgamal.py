import random

def encrypt(message, p, g, x, k):
    y = pow(g, x, p)
    public_key = (p, g, y)
    private_key = (p, x)

    print(f"Original Message: {message}")
    message_decimals = [ord(char) for char in message]
    print(f"Encoded Message to decimal format: {message_decimals}")

    A = pow(g, k, p)
    print(f"A: {A}")

    encrypted_message = [(char * pow(y, k, p)) % p for char in message_decimals]
    print(f"Encrypted Message: {encrypted_message}")

    return encrypted_message

def decrypt(encrypted_message, p, x, A):
    decrypted_message = [(char * pow(pow(A, x, p), -1, p)) % p for char in encrypted_message]
    print(f"Decrypted Message: {decrypted_message}")

    original_message = ''.join(chr(char) for char in decrypted_message)
    print(f"Decoded decrypted Message: {original_message}")

# Parameters
p = 32317006071311007300153513477825163362488057133489075174588434139269806834136210002792056362640164685458556357935330816928829023080573472625273554742461245741026202527916572972862706300325263428213145766931414223654220941111348629991657478268034230553086349050635557712219187890332729569696129743856241741236237225197346402691855797767976823014625397933058015226858730761197532436467475855460715043896844980366130497697812854295958659597567051283852132784468522925504568272879113720098931873959143374175837826000278034973198552060607533234122603254684088120031105907484281003994966956119696956248629032338072839127039
g = 2
x = 1234
k = 4321

# Encryption
encrypted_msg = encrypt("Cusnir Mihaela", p, g, x, k)

# Decryption
A_value = pow(g, k, p)
decrypt(encrypted_msg, p, x, A_value)
