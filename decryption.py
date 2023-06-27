from utils import square_multiply

# We can use random generated N and D by importing N and D from the prime_number_generator
# from prime_number_generator import d, n

# -------------------------------------------------------------------------------------#

# This is my (Abhishek Satasiya : 40197772) N and D variable
# Due to static generation of N and D before, I am using static value of it.

n = 2814151421
d = 939658781

encrypted_msg_int_list = input("Enter your partner's Encrypted Text :- ")[1:-1].split(", ")


def decrypt():
    """
    This function is used to decrypt the encrypted message
    :return: it will return the list of decrypted integers
    """
    decrypted_msg_list = [square_multiply(int(i), d, n) for i in encrypted_msg_int_list]
    return decrypted_msg_list


decrypted_msg_int_list = decrypt()
print(f"decrypted_msg_int_list :- {decrypted_msg_int_list}")

decrypted_msg_hex_list = [hex(i) for i in decrypted_msg_int_list]
print(f"decrypted_msg_hex_list :- {decrypted_msg_hex_list}")

decrypted_original_msg_list = [bytearray.fromhex(i[2:]).decode('utf-8') for i in decrypted_msg_hex_list]
print(f"Decrypted Message :- {decrypted_original_msg_list}")

received_msg = "".join(decrypted_original_msg_list)
print("*"*30)
print(f"Decrypted Message of partner :- {received_msg}")
print("*"*30)
