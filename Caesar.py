allowed_signs = "ABCDEFGHIJKLMNOPQRSTUVWXYZ?!. "
table = list(allowed_signs)
# print(len(table))
shift = -4


def caesar_cypher(text):
    encrypted_message = ""
    for char in text:
        if char.upper() not in table:
            encrypted_message += char
        else:
            index = table.index(char.upper())
            encrypted_message += table[(index + shift) % 30]
    return encrypted_message


def decrypt_cypher(text):
    decrypted_message = ""
    for char in text:
        if char.upper() not in table:
            decrypted_message += char
        else:
            index = table.index(char.upper())
            decrypted_message += table[(index - shift) % 30]
    return decrypted_message

