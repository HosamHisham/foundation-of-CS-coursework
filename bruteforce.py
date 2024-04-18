import math
import time

# Function to factorize the modulus 'n' into its two prime factors 'p' and 'q'
def factor_modulus(n):
    # Start from 2 and go up to the square root of 'n'
    for i in range(2, int(math.sqrt(n)) + 1):
        # If 'i' is not a factor of 'n', continue to the next iteration
        if n % i != 0:
            i += 1
        else:
            # If 'i' is a factor of 'n', return 'i' and the corresponding factor
            if n % i == 0:
                return (i, n // i)
    # If no factor is found, return 'n' and 1
    return (n, 1)

# Defined function for brute force
def bruteforce():
    # Get 'n' and 'e' from the user
    n = int(input("Enter n: "))
    e = int(input("Enter public key (e): "))

    start_time = time.time()
    # Factorize 'n' into 'p' and 'q'
    p, q = factor_modulus(n)
    
    print("p:", p)
    print("q:", q)

    # Calculate 'phi' (Euler's totient function)
    phi_n = (p - 1) * (q - 1)

    # Initialize a counter variable
    count = 0

    # Find 'd' such that (e * d) % phi == 1
    for i in range(1, phi_n):
        if (e * i) % phi_n == 1:
            print("private key (d):", i)
            execution_time = time.time() - start_time
            print("Time executed in seconds:", execution_time)
            print("Number of iterations:", count)
            return  # Stop the function after finding 'd'
        else:
            count += 1

    # If 'd' is not found within the loop, print a message
    print("Private key (d) not found within the given range.")
    execution_time = time.time() - start_time
    print("Time executed in seconds:", execution_time)
    print("Number of iterations:", count)

if __name__ == "__main__":
    bruteforce()
