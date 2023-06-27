def generate_gcd(x, y):
    """
    This function is used for generation of the greatest common divisor from to given parameters
    :return: It will return the greatest common divisor (GCD)
    """
    if x > y:
        small = y
    else:
        small = x
    for i in range(1, small + 1):
        if (x % i == 0) and (y % i == 0):
            gcd_number = i

    return gcd_number


def square_multiply(base, power, mod):
    """
    This function is used to generate the resulting integer by square_multiply method. it will be used in Encryption,
    Decryption, and Signature part of this project
    :return: It will return resulting integer by square_multiply method
    """
    result = 1
    while power > 0:

        if power % 2 == 1:
            result = (result * base) % mod

        power = power // 2
        base = (base * base) % mod

    return result

