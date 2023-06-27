from utils import square_multiply

# We can use random generated N and D by importing N and D from the prime_number_generator
# from prime_number_generator import d, n

# -------------------------------------------------------------------------------------#

# This is my (Abhishek Satasiya : 40197772) N and D variable
# Due to static generation of N and D before, I am using static value of it.

org_msg = input("Enter your message to make signature :- ")

n = 2814151421
d = 939658781

original_msg_list = [org_msg[i:i + 3] for i in range(0, len(org_msg), 3)]
print(f"original_msg_list :- {original_msg_list}")

original_msg_hex_list = [i.encode('utf-8').hex() for i in original_msg_list]
print(f"original_msg_hex_list :- {original_msg_hex_list}")

original_msg_int_list = [(int(i, 16)) for i in original_msg_hex_list]
print(f"original_msg_int_list :- {original_msg_int_list}")


def signature():
    """
    This function is used for making a signature of plain text entered by the user
    :return: It will return list of signed integers
    """
    signed_msg_list = [square_multiply(i, d, n) for i in original_msg_int_list]
    return signed_msg_list


signed_msg_int_list = signature()
print("*" * 30)
print(f"Signature of your message  :- {signed_msg_int_list}")
print("*" * 30)

print("\n")

partner_n = int(input(f"Enter your partner's N :- "))
e = int(input(f"Enter your partner's E :- "))
partner_signed_msg_int_list = input("Enter your partner's Signed Text :- ")[1:-1].split(", ")

print(partner_signed_msg_int_list)


def verify_signature():
    """
    This function is used to verify the signature of the user
    :return: it will return the list of verified integers that was signed
    """
    verify_signed_msg_int_list = [square_multiply(int(i), e, partner_n) for i in partner_signed_msg_int_list]
    return verify_signed_msg_int_list


verified_signed_msg_int_list = verify_signature()

verified_signed_msg_hex_list = [hex(i) for i in verified_signed_msg_int_list]
print(f"signed_msg_hex_list :- {verified_signed_msg_hex_list}")

verified_signed_original_msg_list = [bytearray.fromhex(i[2:]).decode('utf-8') for i in verified_signed_msg_hex_list]
print(f"Decrypted Message :- {verified_signed_original_msg_list}")

received_msg = "".join(verified_signed_original_msg_list)
print("*" * 30)
print(f"Partner's Verified signed Message :- {received_msg}")
print("*" * 30)
