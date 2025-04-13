from cryptography.fernet import Fernet

def_generate_key():
  return Fernet.generate_key()

def_encrypt_message(key_message):
     cipher_suite = Fernet(key)
    encrypt_message = cipher_suite.encrypt(message.encode())
   return encrypt_message


def_decrypt_message(key_message):
     cipher_suite = Fernet(key)
    decrypt_message = cipher_suite.decrypt(encrypted_message.decode())
   return decrypt_message

if __name__ == "__main__":
       key = generate_key()
       message = input("Enter a message to encrypt")
        
        encrypt_message = encrypt_message(key, message)
        print(f"Encrypted Message: {encrypted_message}")

       
        decrypt_message = decrypt_message(key, encrypted_message)
        print(f"decrypted Message: {decrypted_message}")
