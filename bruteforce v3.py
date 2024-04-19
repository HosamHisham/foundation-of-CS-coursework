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
    # Initialize a counter variable for generating prime numbers
    prime_generation_count = 0
    
    # Generate a random number between min_value and max_value
    prime = random.randint(min_value, max_value)
    prime_generation_count += 1
    
    # Keep generating until a prime number is found
    while not prime_check(prime):
        prime = random.randint(min_value, max_value)
        prime_generation_count += 1
    
    return prime, prime_generation_count

# Take input for n (N) and the public key (e)
N = int(input("Enter n: "))
e = int(input("Enter public key: "))
c = int(input("Enter cipher: "))

# Start the timer
start_time = time.time()

# Initialize p and q to be used in RSA key generation
p, q = 0, 0
# Initialize a counter variable for loop iterations during prime number generation
loop_count_generation = 0

# Find p and q such that their product equals N
while p * q != N:
    # Generate a prime number for p
    p, count_p = generate_prime(1, N)
    loop_count_generation += count_p
    
    # Calculate q based on p
    q = N // p

# Calculate Euler's totient function phi(n)
phi_n = (p - 1) * (q - 1)

# Print p and q
print("p:", p)
print("q:", q)

# Initialize a counter variable for loop iterations during calculation
loop_count_calculation = 0

# Find the private key (d) using the public key (e)
found = False
for d in range(2, phi_n):
    loop_count_calculation += 1
    if (e * d) % phi_n == 1:
        print("Private key:", d)
        found = True
        break

if not found:
    print("No suitable private key found.")

message = pow(c, d, N)
print("decrypted message: ",message)
# Calculate the total number of loop iterations
total_loop_count = loop_count_generation + loop_count_calculation

# Print the number of loop iterations for prime generation and calculation
print("Number of loop iterations for prime generation:", loop_count_generation)
print("Number of loop iterations for calculation:", loop_count_calculation)
print("Total number of loop iterations:", total_loop_count)

# Print the runtime
print("Runtime (s):", time.time() - start_time)
