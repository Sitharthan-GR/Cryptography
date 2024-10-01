import hashlib
import random

def mine_block(previous_hash_hex, quote, difficulty):
    
    nonce = random.randint(0, 2**64 - 1)
    quote_bytes = quote.encode('ascii')
    previous_hash = bytes.fromhex(previous_hash_hex)

    while True:
        nonce_bytes = nonce.to_bytes(8, 'big')  
        block_data = previous_hash + nonce_bytes + quote_bytes
        block_hash = hashlib.sha256(block_data).hexdigest()

        if block_hash.startswith('0' * (difficulty // 4)):  
            return nonce, block_hash
        
        nonce = random.randint(0, 2**64 - 1)


quote = "The president was visiting NASA headquarters and stopped to talk to a man who was holding a mop. \"And what do you do?\" he asked. The man, a janitor, replied, \"I'm helping to put a man on the moon, sir.\" -- The little book of leadership"
previous_hash_hex = "00000038b66f815c4070472d3b5234f2725d45f221073f10b5ccc9150883b80a"
difficulty_bits = 24  


nonce, block_hash = mine_block(previous_hash_hex, quote, difficulty_bits)
print(f"Nonce: {nonce}, Block Hash: {block_hash}")
