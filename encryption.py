from utils import square_multiply

n = int(input("Enter your partner's N :- "))
e = int(input("Enter your partner's E :- "))

org_msg = input("Enter your message to encrypt :- ")

original_msg_list = [org_msg[i:i + 3] for i in range(0, len(org_msg), 3)]
print(f"original_msg_list :- {original_msg_list}")

original_msg_hex_list = [i.encode('utf-8').hex() for i in original_msg_list]
print(f"original_msg_hex_list :- {original_msg_hex_list}")

original_msg_int_list = [(int(i, 16)) for i in original_msg_hex_list]
print(f"original_msg_int_list :- {original_msg_int_list}")


def encrypt():
    """
    This function is used to encrypt the plain text entered by the user
    :return: It will return the list of encrypted integers of plain text
    """
    encrypted_msg_list = [square_multiply(i, e, n) for i in original_msg_int_list]
    return encrypted_msg_list


encrypted_msg_int_list = encrypt()
print("*"*30)
print(f"Encrypted Message :- {encrypted_msg_int_list}")
print("*"*30)
