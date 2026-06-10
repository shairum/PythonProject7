import random


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def generate_prime(min_val, max_val):
    while True:
        num = random.randint(min_val, max_val)
        if is_prime(num):
            return num


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    d, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return d, x, y


def mod_inverse(e, phi):
    d, x, y = extended_gcd(e, phi)
    if d != 1:
        return -1
    return x % phi


def generate_keys():
    p = generate_prime(100, 500)
    q = generate_prime(100, 500)
    while q == p:
        q = generate_prime(100, 500)

    n = p * q
    phi = (p - 1) * (q - 1)

    e = 3
    while gcd(e, phi) != 1:
        e += 1

    d = mod_inverse(e, phi)

    return (e, n), (d, n)


def rsa_encrypt_block(m, public_key):
    e, n = public_key
    return pow(m, e, n)


def rsa_decrypt_block(c, private_key):
    d, n = private_key
    return pow(c, d, n)


def rsa_encrypt(text, public_key):
    result = []
    for ch in text:
        m = ord(ch)
        c = rsa_encrypt_block(m, public_key)
        result.append(str(c))
    return ' '.join(result)


def rsa_decrypt(encrypted_text, private_key):
    result = ""
    numbers = encrypted_text.split()
    for num_str in numbers:
        c = int(num_str)
        m = rsa_decrypt_block(c, private_key)
        result += chr(m)
    return result


public_key, private_key = generate_keys()
a = 0

while a == 0:
    text = input()
    mode = input()

    if mode == "1":
        print(rsa_encrypt(text, public_key))
    elif mode == "2":
        print(rsa_decrypt(text, private_key))
    a = int(input())