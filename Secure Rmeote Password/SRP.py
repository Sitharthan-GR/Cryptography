import hashlib

# Provided values
username = "sgovind2"
password = "surbedded"
salt_hex = "f28d4af0"
iterations = 1000
B = 207409662008899319064436105791501383174714527064395186809906990495078564750288986639028209059640824204730465671679976288245285903625236751209138684215429266646460858172403280122872731428491476847964386398221166043009174023123668657024535360174746500576787480828170277616169714614549759244929559704160391787622
ga = 152942981836585815521541634032769343481440477957940917450839672793936757932139926304758252550618192821157509160985296106936497616675924183137128358886824565266232122310843082368671548361581077387195678595798215081163070464945165263673801489221968561727748846296986482669042320845782831219187201415690112611897
g = 5
p = 233000556327543348946447470779219175150430130236907257523476085501968599658761371268535640963004707302492862642690597042148035540759198167263992070601617519279204228564031769469422146187139698860509698350226540759311033166697559129871348428777658832731699421786638279199926610332604408923157248859637890960407
a = 571 # Client's private key

# Password Hashing (x)
salt_bytes = bytes.fromhex(salt_hex)
password_hash = hashlib.sha256(salt_bytes + password.encode('ascii')).digest()

for _ in range(iterations - 1):
    password_hash = hashlib.sha256(password_hash).digest()

x = int.from_bytes(password_hash, byteorder='big')

# Compute k
p_bytes = p.to_bytes((p.bit_length() + 7) // 8, byteorder='big')
g_bytes = g.to_bytes((g.bit_length() + 7) // 8, byteorder='big')
k = int.from_bytes(hashlib.sha256(p_bytes + g_bytes).digest(), byteorder='big')

# Calculate gb
v = pow(g, x, p)
gb = (B - k * v) % p

# Calculate u
ga_bytes = ga.to_bytes((ga.bit_length() + 7) // 8, byteorder='big')
gb_bytes = gb.to_bytes((gb.bit_length() + 7) // 8, byteorder='big')
u = int.from_bytes(hashlib.sha256(ga_bytes + gb_bytes).digest(), byteorder='big')

# Compute the Shared Key
shared_key = pow((B - k * pow(g, x, p)), (a + u * x), p)

# Convert shared key to bytes for hashing in M1 and M2
shared_key_bytes = shared_key.to_bytes((shared_key.bit_length() + 7) // 8, byteorder='big')

# Compute hashes for M1 and M2
username_hash = hashlib.sha256(username.encode('ascii')).digest()
hash_p = hashlib.sha256(p_bytes).digest()
hash_g = hashlib.sha256(g_bytes).digest()
hash_p_xor_g = bytes(a ^ b for a, b in zip(hash_p, hash_g))

# Calculate M1
M1 = hashlib.sha256(
    hash_p_xor_g + username_hash + salt_bytes + ga_bytes + gb_bytes + shared_key_bytes
).hexdigest()

# Calculate M2
M1_bytes = bytes.fromhex(M1)
M2 = hashlib.sha256(ga_bytes + M1_bytes + shared_key_bytes).hexdigest()

# Output the results
print(f"Password hash as an integer (x): {x}")
print(f"k (H(p || g) as an integer): {k}")
print(f"gb (B-k*v (mod p)): {gb}")
print(f"u (H(ga || gb)): {u}")
print(f"Shared key: {shared_key}")
print(f"Verifier M1 (hex): {M1}")
print(f"Verifier M2 (hex): {M2}")
