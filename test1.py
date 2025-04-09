import hashlib

def md5hash(text):
    return hashlib.md5(text.encode()).hexdigest()

password = "redhat"
encrypted_password = md5hash(password)
print(encrypted_password)