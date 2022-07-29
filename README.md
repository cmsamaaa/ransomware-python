# "Ransomware" Script

This is a simple script written while helping out with a friend's assignment, using RSA and OEAP.
It is meant to simulate a ransomware.

-   [Files](#files)
-   [Dependencies](#dependencies)

### Files
- "hackman.py" is the encryption script, programmed to encrypt all .txt files within the 
directory using simple text substitution ciphering of the alphabets "a-z". Next, it will generate a public and private 
key using RSA, and the substitution key is then encrypted with the public key through OEAP into "key.bin".

- "undoHax.py" is the decryption script. It will decrypt the "key.bin" using the private key, and write into "key.txt".
Furthermore, the script will take the decrypted substitution key to reverse the substituted text into the original
alphabet prior to the substitution.

### Dependencies
    pycryptodome