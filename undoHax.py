import os

from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

# decryption
file_in = open("key.bin", "rb")
private_key = RSA.import_key(open("private.pem").read())
enc_data = file_in.read(private_key.size_in_bytes())
cipher_rsa = PKCS1_OAEP.new(private_key)
data = cipher_rsa.decrypt(enc_data).decode('utf-8')
with open("key.txt", "w") as f:
    f.write(data)
file_in.close()

alphabet = "abcdefghijklmnopqrstuvwxyz"
list_alphabet = list(alphabet)
sub_cypher = data.split('|')

cwd = os.getcwd()
folder = os.listdir(cwd)

for item in folder:
    if item.endswith(".enc"):
        text = open(item, "r")
        result = ""
        for letter in text.read():
            if letter.lower() in alphabet:
                result += alphabet[sub_cypher.index(letter.lower())]
            else:
                result += letter

        with open(item.split('.')[0] + ".txt", "w") as f:
            f.write(result)
            text.close()
