import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import binascii
import random
import sympy


def generate_prime(bits):
    while True:
        candidate = random.getrandbits(bits)
        if sympy.isprime(candidate) and sympy.isprime((candidate - 1) // 2):
            return candidate


private_key_a = random.randint(1, 1000)


bits = 1024  
prime_p = generate_prime(bits)

generator_g = 5

public_key_a = pow(generator_g, private_key_a, prime_p)

print("Prime (p):", prime_p)
print("Generator (g):", generator_g)
print("Private Key (a):", private_key_a)
print("Public Key (g^a mod p):", public_key_a)

gab=79125382631061585825753511771103871018224092300788039745801975970567271784535031963371715981767215592765795637338025240851683189353097155255561244290040373654460327599878840747729366973235436059743548570510333813589338043772276705094906334168748903668566518496062222281903633702888580015261463889109418073530

shared_key = gab.to_bytes(128, byteorder='big')


key_hash = hashlib.sha256(shared_key).digest()


aes_key = key_hash[:16]


ciphertext_hex = "618ce5581ef9a47a6c7c00042a120dcd6d72acba7479d103f8d809e3d7dc19f8e4afe68a6cce9d4c2fe47b1641484deb36c40c8bedc2502854286ff1aee42a6581047643bb064284b0c00c16a3b01fb16b8042d6bbe34d40a171eab7cc017fd14c30d8344ebb253a5e0962c1ae9101e6"
iv_hex = "33dc6774c1b5ebaabb0e79809b57c99b"


ciphertext = binascii.unhexlify(ciphertext_hex)
iv = binascii.unhexlify(iv_hex)


cipher = AES.new(aes_key, AES.MODE_CBC, iv)


plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)


plaintext_str = plaintext.decode('ascii')


print("Decrypted Message:", plaintext_str)
