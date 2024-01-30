def vigenere(message, key, direction=1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    message = message.lower()
    key = key.lower()

    for char in message:

        # Append any non-letter character to the message
        if not char.isalpha():
            final_message += char
        else:        
            # Find the right key character to encode/decode
            key_char = key[key_index % len(key)]
            key_index += 1
            # Define the offset and the encrypted/decrypted letter
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset*direction) % len(alphabet)
            final_message += alphabet[new_index]

    return final_message


def encrypt(message, key):
    return vigenere(message, key)


def decrypt(message, key):
    return vigenere(message, key, -1)


def main():
    encrypt_id = 'e'
    decrypt_id = 'd'
    
    print("\nHello to my encryption/decryption program. You will need a text and a key (both on lower characters) to do this.\n")
    print("But first of all, do you want to:")
    print(f"- [{encrypt_id}] ENCRYPT, or")
    print(f"- [{decrypt_id}] DECRYPT a text?")

    choice = ''
    while choice not in [encrypt_id, decrypt_id]:
        print()
        choice = input(f"Your choice [{encrypt_id} or {decrypt_id}]: ").lower().strip()

    if choice == encrypt_id:
        print()
        text = input("Please enter your text to encrypt: ")
        custom_key = input("Please enter your encryption key:  ")
        encryption = encrypt(text, custom_key)
        print(f'\nEncrypted text: {encryption}\n')

    if choice == decrypt_id:
        print()
        text = input("Please enter your text to decrypt: ")
        custom_key = input("Please enter your decryption key:  ")
        decryption = decrypt(text, custom_key)
        print(f'\nDecrypted text: {decryption}\n')

if __name__ == "__main__":
    main()