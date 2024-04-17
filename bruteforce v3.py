import random
import time

# Function to check if a number is a prime number
def prime_check(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

# Function to generate a prime number within a given range
def generate_prime(min_value, max_value):
    # Generate a random number between min_value and max_value
    prime = random.randint(min_value, max_value)
    # Keep generating until a prime number is found
    while not prime_check(prime):
        prime = random.randint(min_value, max_value)
    return prime

# Take input for n (N) and the public key (e)
N = int(input("Enter n: "))
e = int(input("Enter public key: "))

# Start the timer
start_time = time.time()

# Initialize p and q to be used in RSA key generation
p, q = 0, 0
# Find p and q such that their product equals N
while p * q != N:
    # Generate a prime number for p
    p = generate_prime(1, N)
    # Calculate q based on p
    q = N // p

# Calculate Euler's totient function phi(n)
phi_n = (p - 1) * (q - 1)

# Print p and q
print("p:", p)
print("q:", q)

# Find the private key (d) using the public key (e)
found = False
for d in range(2, phi_n):
    if (e * d) % phi_n == 1:
        print("Private key:", d)
        found = True
        break

if not found:
    print("No suitable private key found.")



# Print the runtime
print("run time: (s)", time.time() - start_time)
