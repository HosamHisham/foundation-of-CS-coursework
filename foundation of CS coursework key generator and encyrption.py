import random
import math
import time


#start time for runtime
start_time = time.time()

# Function to check if a number is a prime number
def prime_check(number):
    if number < 2:
        return False
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return False
    return True

# Function to generate a prime number within a given range
"""
def generate_prime(min_value, max_value):
    prime = random.randint(min_value, max_value)
    while not prime_check(prime):
        prime = random.randint(min_value, max_value)
    return prime
"""


def generate_prime(bits):
    prime = random.getrandbits(bits)
    while not prime_check(prime):
        prime = random.getrandbits(bits)
    return prime

bits = int(input("enter bits for program: "))


# Function to generate the private key 'd'
def key_generator(e, phi):
    for d in range(3, phi):
        if (d * e) % phi == 1:
            return d


# start of program
# Generate two distinct prime numbers 'p' and 'q'
p, q = generate_prime(bits), generate_prime(bits)
while p == q:
    q = generate_prime(3, 10000)

# Calculate 'n' and 'phi_n'
n = p * q
phi_n = (p - 1) * (q - 1)

# Generate the public key 'e'
e = random.randint(3, phi_n - 1)
while math.gcd(e, phi_n) != 1:
    e = random.randint(3, phi_n - 1 )

# Generate the private key 'd'
d = key_generator(e, phi_n)

# Print the public and private keys and 'n'
print("public key(e):", e)
print("private key(d):", d)
print("n:", n)

# Get a message from the user
message = input("enter your message:")

# Encode the message into ASCII
message_encoded = [ord(c) for c in message]

# Encrypt the message
ciphertext =[pow(c, e , n) for c in message_encoded]

# Print the ciphertext
prnt_cipher = int(input("enter 1 to print cypher text or 0 to to skip: "))
if prnt_cipher == 1:
    print("the cipher text is", ciphertext)


# Decrypt the ciphertext
message_encoded = [pow(ch, d, n) for ch in ciphertext]
message = "".join(chr(ch) for ch in message_encoded)

# Print the decrypted message
prnt_decrypt = int(input("enter 1 to print the decryypted message or 0 to skip: "))
if prnt_decrypt == 1:
    print("the decyrypted message is", message)

#calculates runtime
execution_time = time.time() - start_time
print(f"time executed in seconds: {execution_time:.1f}" )

#calculates cpu proccess time
print("runtime for cpu process in seconds: ", time.process_time())


