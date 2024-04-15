# Importing required libraries
import math
import time



# Function to calculate the greatest common divisor (gcd) and coefficients of Bézout's identity
def extended_gcd(a , b):
    x0, x1, y0, y1 = 1, 0 , 0 , 1
    while b:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 -q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0

# Function to factorize the modulus 'n' into its two prime factors 'p' and 'q'
def factor_modulus(n):
    # Start from 2 and go up to the square root of 'n'
    for i in range(2, int(math.sqrt(n)) + 1):
        # If 'i' is not a factor of 'n', continue to the next itteration
        if n % i != 0:
            i += 1
        else:
            #if i is a factor of n, return i and the corresponding factor
            if n % i == 0:
                return (i , n // i)
    # If no factor is found, return 'n' and 1
    return (n, 1)


# Get 'e' (public exponent) from the user
e = int(input("enter the public exponent: "))

# Get 'n' (modulus) from the user
n = int(input("enter the modulus n: "))

#start time for runtime
start_time = time.time()
cpu_time = time.process_time()

# Factorize 'n' into 'p' and 'q'
p, q = factor_modulus(n)
print("p", p) # Print p 
print("q", q) # Print q

# Calculate 'phi_n' (Euler's totient function)
phi_n = (q - 1) * (p - 1)

# Calculate gcd and coefficients of Bézout's identity
gcd, x, y = extended_gcd(e, phi_n)

# Calculate private exponent
private_exponent = x

# Print the private key
print("the privatte key (d) is: ", private_exponent)

# RSA decryption
def rsa_decrypt(ciphertext, x, n):
    message = pow(ciphertext, x, n )
    return message


# Get the ciphertext from the user
ciphertext = int(input("Enter cipher to decode: "))

# Decrypt the message
message = rsa_decrypt(ciphertext, x, n)

# Print the decrypted message
print("Decrypted message:", message)


# Calculate and print execution time
execution_time = time.time() - start_time
exc_time = time.process_time() - cpu_time
print(f"time executed in seconds: {execution_time:.1f}")
print("cpu execution time in seconds: ", exc_time)
