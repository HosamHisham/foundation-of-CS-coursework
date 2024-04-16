import math
import time

def extended_gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return (gcd, y - (b // a) * x, x)

def mod_inverse(e, n):
    gcd, x, y = extended_gcd(e, n)
    if gcd != 1:
        raise ValueError('Modular inverse does not exist')
    else:
        return x % n

# Function to factorize the modulus 'n' into its two prime factors 'p' and 'q'
def factor_modulus(n):
    # Start from 2 and go up to the square root of 'n'
    for i in range(2, int(math.sqrt(n)) + 1):
        # If 'i' is not a factor of 'n', continue to the next iteration
        if n % i != 0:
            continue
        else:
            # If 'i' is a factor of 'n', calculate the corresponding factor
            if n % i == 0:
                return (i , n // i)
    # If no factor is found, return 'n' and 1
    return (n, 1)

# Get 'e' (public exponent) from the user
e = int(input("Enter the public exponent: "))

# Get 'n' (modulus) from the user
n = int(input("Enter the modulus n: "))

start_time = time.time()

# Factorize 'n' into 'p' and 'q'
p, q = factor_modulus(n)
print("p:", p) # Print p 
print("q:", q) # Print q

# Calculate 'phi_n' (Euler's totient function)
phi_n = (q - 1) * (p - 1)

# Calculate gcd and coefficients of Bézout's identity
gcd, x, y = extended_gcd(e, phi_n)

# Calculate private exponent
d = mod_inverse(e, phi_n)

# Print the private key
print("The private key (d) is:", d)

print("runtime in seconds", time.time() - start_time)

