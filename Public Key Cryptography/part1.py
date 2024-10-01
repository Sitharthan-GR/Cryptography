import random

def fast_modular_exponentiation(base, exponent, modulus):
    result = 1
    
    base = base % modulus  # Ensure base is within the modulus range
    
    while exponent > 0:
        # If exponent is odd, multiply result with base
        if exponent % 2 == 1:
            result = (result * base) % modulus
        
        # Square the base and reduce the exponent by half
        base = (base * base) % modulus
        exponent = exponent // 2
    
    return result

# # Example usage:
# base = 4235880211405804673
# exponent = 131
# modulus = 12855544647099734480  # Example modulus, you can change this
# result = fast_modular_exponentiation(base, exponent, modulus)
# print(f"{base}^{exponent} % {modulus} = {result}")





def miller_rabin_test(n, k=5):
    if n <= 1:
        return False
    if n <= 3:
        return True

    # Write n as (2^r) * d + 1
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # Witness loop
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)  # Compute a^d % n

        if x == 1 or x == n - 1:
            continue

        for _ in range(r - 1):
            x = pow(x, 2, n)  # Compute (x^2) % n
            if x == n - 1:
                break
        else:
            return False  # n is definitely composite

    return True  # n is probably prime

# Example usage:
num = 14896603476762504216869188389878391277952306470887353278749870712658028254115176589358091601516637172943766166767485003102360007157962005257240686638050075669634868961542246448313839925015068460238112226822843911044958249298070679176908382038866255817504274303504766070381438439773446792970703337179701325019  # Replace with the number you want to test for primality
is_prime = miller_rabin_test(num)
if is_prime:
    print(f"{num} is probably prime.")
else:
    print(f"{num} is composite.")


def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    
    gcd, x1, y1 = extended_gcd(b, a % b)
    
    x = y1
    y = x1 - (a // b) * y1
    
    return gcd, x, y

# Example usage:
a = 30
b = 18
# gcd, x, y = extended_gcd(a, b)
# print(f"GCD({a}, {b}) = {gcd}")
# print(f"Bézout coefficients: x = {x}, y = {y}")


