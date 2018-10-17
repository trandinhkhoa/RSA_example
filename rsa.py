#! /usr/bin/python3
from argparse import ArgumentParser


# Implementation ofExtended euclidean algorithm
# Input: integer a,b
# Output: gcd(a,b) old_r
#         Bezout coefficients old_s, old_t
def extended_euclidean(a, b):
    old_r = a
    r = b
    old_s = 1
    s = 0
    old_t = 0
    t = 1
    while (r != 0):
        q = int(old_r / r)
        (old_r, r) = (r, old_r - q * r)
        (old_s, s) = (s, old_s - q * s)
        (old_t, t) = (t, old_t - q * t)
    return (old_r, old_s, old_t)


# Find multiplicative inverse of a mod m
def mul_inverse(a, m):
    (gcd , x, y) = extended_euclidean(a, m)
    if (gcd == 1):
        if (x < 0):
            x = x + m
        return x
    else:
        return -1


# key generation
# Input: 2 prime p, q
# Output: public key e and secret key d
def keygen(p, q):
    # Compute totient phi(n)
    phi = (p - 1) * (q - 1)

    # Choose integer such that e and phi(n) are coprime
    # fermat = [3, 5 , 17, 257, 65537, ...]

    # begin with commonly used values
    e = 65537

    # Find other values of e in case 65537 and phi(n) are ot corpime
    (gcd, _, _) = extended_euclidean(e, phi)
    while (gcd != 1):
        e = e + 2
        (gcd, _, _) = extended_euclidean(e, phi)

    # Compute decryption key d = multiplicative inverse of e mod phi(n)
    d = mul_inverse(e, phi)

    # debug message
    if args.debug is True:
        print("phi = ", phi)
        print("e = ", e)
        print("d = ", d)
    return (e, d)


# Implement Exponentiation by squaring
# Input x,n
# Output x^n
def exp(x, n):
    if (n == 1):
        return x
    elif ((n % 2) == 0):
        return exp(x * x, int(n / 2))
    else:
        return x * exp(x * x, int((n - 1) / 2))
    return 0


# Encryption function
# Input: message m, public key (e,N)
# Output: ciphertext = m^e mod N
def encrypt(msg, e, N):
    temp = ''
    # Transform text to numerical representation for exponentiation step
    for i in msg:
        temp = temp + str(ord(i))
    msg_Num = int(temp)
    print(msg_Num)
    print("Numerical representation of your message = ", msg_Num % N)

    print("-------Encrypting------------------")
    cipher = exp(msg_Num, e)
    cipher = cipher % N
    return cipher


# Decryption function
# Input: ciphertext cipher, private key d
# Output: numerical representation of original text
def decrypt(cipher, d, N):
    print("-------Decrypting------------------")
    decipher = exp(cipher, d)
    decipher = decipher % N
    return decipher


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-d', '--debug', action='store_true', help="run program in debug mode")
    args = parser.parse_args()

    if args.debug is True:
        print("Running in debug mode...")

    # Select 2 prime p and q
    p = int(input("Enter prime p = "))
    q = int(input("Enter prime q = "))

    # Compute N=pq
    N = p * q

    # e is the encryption key
    # d is the decryption key
    print("-------Generating key------------------")
    (e, d) = keygen(p, q)

    # Show public key
    print("Public key (e, N) = ", e, N)

    # Message to be encrypted
    msg = input("-------Enter your message = ")

    # Encryption
    cipher = encrypt(msg, e, N)
    print("Cipher text = ", cipher)

    # Decryption
    decipher = decrypt(cipher, d, N)
    print("De-Cipher text = ", decipher)
