from repositories.rot13_repository import Rot13
from sys import exit


plain_text: str = input("Insert a plain-text value for Rot13 encryption: ")
print(f"Plain-text: {plain_text}")

rot13_encrypted_text: str = Rot13.encrypt(plain_text)
print(f"Encrypted text: {rot13_encrypted_text}")

rot13_decrypted_text: str = Rot13.decrypt(rot13_encrypted_text)
print(f"Decrypted text: {rot13_decrypted_text}")

exit(0)
