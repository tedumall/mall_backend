import hashlib

md5 = hashlib.md5()
md5.update("123456".encode())
pass_h = md5.hexdigest()
print(pass_h)