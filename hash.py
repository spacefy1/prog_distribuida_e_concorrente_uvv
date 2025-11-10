import hashlib

My_String = "Ola Mundo!"
hash_value = hashlib.md5(My_String.encode())
print(hash_value.hexdigest())

hash_value_sha1 = hashlib.sha1(My_String.encode())
print(hash_value_sha1.hexdigest())

hash_value_sha256 = hashlib.sha256(My_String.encode())
print(hash_value_sha256.hexdigest())

hash_value_sha512 = hashlib.sha512(My_String.encode())
print(hash_value_sha512.hexdigest())


