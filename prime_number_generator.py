import random
from utils import generate_gcd


def prime_number_generator():
    """
    This function is used for generating the prime numbers for the RSA algorithm
    :return: it will return the prime number
    """
    for possible_prime in range(random.randrange(32768, 65535), 65535):

        is_prime = True
        for num in range(2, int(possible_prime ** 0.5) + 1):
            if possible_prime % num == 0:
                is_prime = False
                break

        if is_prime:
            return possible_prime


p = prime_number_generator()
q = prime_number_generator()

n = p * q
phi_n = (p - 1) * (q - 1)

print(f"Prime Number P :- {p}")
print(f"Prime Number q :- {q}")
print("*"*30)
print(f"N :- {n}")
print(f"PHI_N :- {phi_n}")
print("*"*30)


def find_e():
    """
    This function is used for generating public exponent E for RSA algorithm
    :return: It will return public exponent E
    """
    for possible_e in range(random.randrange(32768, 65535), 65535):

        if possible_e < phi_n and generate_gcd(possible_e, phi_n) == 1:
            return possible_e


e = find_e()
print(f"E :- {e}")


def find_d():
    """
    This function is used for generating secret exponent D for RSA algorithm
    :return: It will return secret exponent D
    """
    possible_d = pow(e, -1, phi_n)
    return possible_d


d = find_d()
print(f"D :- {d}")
