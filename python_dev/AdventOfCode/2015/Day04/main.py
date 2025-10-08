import hashlib

data = "abcdef"

md5_hash = hashlib.md5(data.encode('utf-8'))
#md5_hash.update(data.encode())
hash_result = md5_hash.hexdigest()
print(md5_hash)
print(hash_result)
