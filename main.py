# Name: Dennis Bandavong
# CSCI 4900 - Polyalphabetic and Rail Fence Cipher Project
# Due Date: 8/9/2023

from polyalphabetic import Polyalphabetic as pc
from railfencecipher import RailFenceCipher as rfc

cipher = input("Polyalphabetic or Rail Fence Cipher? (pc or rfc): ")
# Polyalphabetic
if cipher.lower() == "pc":
    # This is the cycling pattern that will be passed into the polyalphabetic cipher.
    sequence = ['M2', 'M3', 'M2', 'M1', 'M3']

    # Read and write to files.
    plaintext_file = input("Enter plaintext file: ")
    with open(plaintext_file, 'r') as file:
        plaintext = file.read()
    pc_instance_1 = pc(sequence)
    ciphertext = pc_instance_1.encrypt(plaintext)
    print(f"\nCiphertext: {ciphertext}")

    with open("pc_encrypted.txt", 'w') as file:
        file.write(ciphertext)
        print("Encrypted Message using Polyalphabetic cipher is now in pc_encrypted.txt\n")

    with open("pc_encrypted.txt", 'r') as file:
        plaintext = file.read()
    plaintext = pc_instance_1.decrypt(ciphertext)
    print(f"Plaintext: {plaintext}")

    with open("pc_decrypted.txt", 'w') as file:
        file.write(plaintext)
        print("Decrypted Message using Polyalphabetic cipher is now in pc_decrypted.txt\n")

# Rail Fence Cipher
elif cipher.lower() == "rfc":
    # Depth of rail fence cipher
    depth = int(input("Enter the depth: "))
    rfc_instance = rfc(depth)

    encrypt_or_decrypt = input("Encrypt or Decrypt? (e or d): ")
    # Encryption Option
    if encrypt_or_decrypt.lower() == "e":
        plaintext_file = input("Enter plaintext file: ")
        with open(plaintext_file, 'r') as file:
            plaintext = file.read()
        ciphertext1 = rfc_instance.encrypt(plaintext)
        rfc_instance.rail_fence_display(plaintext)
        print(f"Ciphertext: {ciphertext1}\n")

        with open("rfc_encrypted.txt", 'w') as file:
            file.write(ciphertext1)
            print("Encrypted Message using Rail Fence Cipher is now in rfc_encrypted.txt\n")

    # Decryption Option
    elif encrypt_or_decrypt.lower() == "d":
        ciphertext_file = input("Enter ciphertext file: ")
        with open(ciphertext_file, 'r') as file:
            ciphertext = file.read()
        plaintext1 = rfc_instance.decrypt(ciphertext)
        print(f"Plaintext: {plaintext1}\n")
        with open("rfc_decrypted.txt", 'w') as file:
            file.write(plaintext1)
            print("Decrypted Message using Rail Fence Cipher is now in rfc_decrypted.txt\n")

    # Invalid option
    else:
        encrypt_or_decrypt = input("Please enter valid option. Encrypt or Decrypt? (e or d): ")

else:
    cipher = input("Please enter valid option. Polyalphabetic or Rail Fence Cipher? (pc or rfc): ")


