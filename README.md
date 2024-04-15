you will find two different programs to generate RSA keys both are functioning

RSA improved speed is a more efficient code with a lower runtime than the other RSA key generator

bruteforce v3 is the fully functioning bruteforce with the correct output of D through bruteforcing the p and q values that form N then bruteforcing the d in the following equation:       ( e * d ) % phi_n == 1

new bruteforce will output all the possible D keys through bruteforcing the d in the following formula: (cipher ** d) % N = message

bruteforce file will output the correct D but throug factorizing the N then bruteforcing the D in the following equation: (e * d) % phi_n == 1

the file "factor modulus n and calulcate priivate key" factorizes the value n to get p and q and uses the extended euclidean algorithm to calculate the private key

