import hashlib

key = b"str"
my_string="THis is a normal string. Nothingto see here".encode()#Turns to a bytes like object

# for i in range(10):
#     hashed=hashlib.sha256(key).hexdigest()
#     print(hashed)
    # breakpoint()

for i in range(10):
    hashed=hash(key)
    print(hashed%8)
    