import math
import time

# Extended Euclidean Algorithm to find gcd and coefficients of Bézout's identity
def extended_gcd(a, b, counter):
    counter += 1  # Increment the counter for each call
    if a == 0:
        return (b, 0, 1, counter)
    else:
        gcd, x, y, counter = extended_gcd(b % a, a, counter)
        return (gcd, y - (b // a) * x, x, counter)

# Modular multiplicative inverse function using Extended Euclidean Algorithm
def mod_inverse(e, n, counter):
    gcd, x, y, counter = extended_gcd(e, n, counter)
    if gcd != 1:
        raise ValueError('Modular inverse does not exist')
    else:
        return x % n, counter

# Function to factorize the modulus 'n' into its two prime factors 'p' and 'q'
def factor_modulus(n, counter):
    # Start from 2 and go up to the square root of 'n'
    for i in range(2, int(math.sqrt(n)) + 1):
        counter += 1  # Increment the counter for each iteration
        # If 'i' is not a factor of 'n', continue to the next iteration
        if n % i != 0:
            continue
        else:
            # If 'i' is a factor of 'n', calculate the corresponding factor
            if n % i == 0:
                return (i , n // i, counter)
    # If no factor is found, return 'n' and 1
    return (n, 1, counter)

# Get 'e' (public exponent) from the user
e = int(input("Enter the public exponent: "))

# Get 'n' (modulus) from the user
n = int(input("Enter the modulus n: "))

cipher = int(input("enter cipher: "))

start_time = time.time() * 1000

counter = 0  # Initialize the counter to 0

# Factorize 'n' into 'p' and 'q'
p, q, counter = factor_modulus(n, counter)
print("p:", p) # Print p 
print("q:", q) # Print q

# Calculate 'phi_n' (Euler's totient function)
phi_n = (q - 1) * (p - 1)

# Calculate private exponent
d, counter = mod_inverse(e, phi_n, counter)

# Print the private key
print("The private key (d) is:", d)
message = pow(cipher, d, n)
print("decrypted message: ", message)
# Print the runtime
print("Runtime in seconds:", (time.time()*1000) - start_time)

# Print the total number of loop iterations
print("Total number of loop iterations:", counter)
