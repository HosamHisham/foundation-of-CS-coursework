import random

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
    prime = random.randint(min_value, max_value)
    while not prime_check(prime):
        prime = random.randint(min_value, max_value)
    return prime

N = int(input("Enter n: "))
e = int(input("Enter public key: "))

p, q = 0, 0
while p * q != N:
    p = generate_prime(1, 10000)
    q = N // p

phi_n = (p - 1) * (q - 1)

print("p:", p)
print("q:", q)

for d in range(2, phi_n):
    if (e * d) % phi_n == 1:
        print("Private key:", d)
        break
