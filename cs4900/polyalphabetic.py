
class Polyalphabetic:
    def __init__(self, sequence):
        self.keyword = sequence

    def encrypt(self, plaintext):
        substitution_cipher = "DKVQFIBJWPESCXHTMYAUOLRGZN"
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        encrypted_text = ''

        # Keeps looping through cycling pattern until end.
        # Using index of alphabet and substitution_cipher to shift or substitute.
        for i, char in enumerate(plaintext):
            substitution_key = self.keyword[i % len(self.keyword)]
            if substitution_key == 'M1':
                encrypted_char_index = (alphabet.index(char.lower()) - 3) % 26
                encrypted_char = alphabet[encrypted_char_index]
            elif substitution_key == 'M2':
                substitution_index = alphabet.index(char.lower())
                encrypted_char = substitution_cipher[substitution_index]
            elif substitution_key == 'M3':
                encrypted_char_index = (alphabet.index(char.lower()) + 5) % 26
                encrypted_char = alphabet[encrypted_char_index]
            else:
                encrypted_char = char

            # each encrypted char will be added to this final string until the loop ends.
            encrypted_text += encrypted_char.upper()

        return encrypted_text

    def decrypt(self, encrypted_text):
        substitution_cipher = "DKVQFIBJWPESCXHTMYAUOLRGZN"
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        decrypted_text = ''

        # Keeps looping through cycling pattern until end.
        # Using index of alphabet and substitution_cipher to shift or substitute but the other way
        # around than what was done for encryption.
        for i, char in enumerate(encrypted_text):
            substitution_key = self.keyword[i % len(self.keyword)]
            if substitution_key == 'M1':
                decrypted_char_index = (alphabet.index(char.lower()) + 3) % 26
                decrypted_char = alphabet[decrypted_char_index]
            elif substitution_key == 'M2':
                alphabet_index = substitution_cipher.index(char)
                decrypted_char = alphabet[alphabet_index]
            elif substitution_key == 'M3':
                decrypted_char_index = (alphabet.index(char.lower()) - 5) % 26
                decrypted_char = alphabet[decrypted_char_index]
            else:
                decrypted_char = char

            # each decrypted char will be added to this final string until the loop ends.
            decrypted_text += decrypted_char.lower()

        return decrypted_text