import math
import time

#start time for runtime
start_time = time.time()

# Function to factorize the modulus 'n' into its two prime factors 'p' and 'q'
def factor_modulus(n):
    # Start from 2 and go up to the square root of 'n'
    for i in range(2, int(math.sqrt(n)) + 1):
        # If 'i' is not a factor of 'n', continue to the next itteration
        if n % i != 0:
            i += 1
        else:
            #if n is a factor of n, return i and the corresponding factor
            if n % i == 0:
                return (i , n // i)
    # If no factor is found, return 'n' and 1
    return (n, 1)

# defined function for burteforce
def bruteforce():
    # Get 'n' and 'e' from the user
    n = int(input("Enter n: "))
    e = int(input("Enter public key (e): "))

    # Factorize 'n' into 'p' and 'q'
    p, q = factor_modulus(n)
    print("Factors of n (p, q):", p , q)

    # Calculate 'phi' (Euler's totient function)
    phi = (p - 1) * (q - 1)

    # Find 'd' such that (e * d) % phi == 1
    d = next((d for d in range(1, phi) if ((e * d) % phi == 1)), None)

    # If 'd' is found, print it. Otherwise, print an error message
    if d is not None:
        print("Private key (d):", d)
    else:
        print("No suitable 'd' found.")


if __name__ == "__main__":
    bruteforce()

#calculate runtime
execution_time = time.time() - start_time

print(f"time executed in seconds: {execution_time:.1f}")