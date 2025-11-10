import hashlib
import secrets

salt = secrets.token_hex(16)
print(f"Salt: {salt}")

password = "bolinhas"

hash_value = hashlib.sha256((password+salt).encode())
print(hash_value.hexdigest())

