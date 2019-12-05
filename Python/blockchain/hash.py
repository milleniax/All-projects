import hashlib as hasher

sha = hasher.sha256(b'Hello Python').hexdigest()
 
print(sha)