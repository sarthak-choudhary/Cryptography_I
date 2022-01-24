from tarfile import BLOCKSIZE
from Crypto.Hash import SHA256

file = "./video.mp4"
BLOCK_SIZE = 1024

file_array = []

with open(file, 'rb') as f:
    fb = f.read(BLOCK_SIZE)
    while len(fb) > 0:
        file_array.append(fb)
        fb = f.read(BLOCK_SIZE)
        
# print(type(file_array[0]))
# print(file_array)

h = SHA256.new()
h.update(file_array[-1])
last_hash = h.digest()
last_hex_hash = h.hexdigest()

index = len(file_array) - 2

while (index >= 0):
    new_h = SHA256.new()
    new_h.update(file_array[index])
    new_h.update(last_hash)
    
    last_hash = new_h.digest()
    last_hex_hash = new_h.hexdigest()
    index = index - 1

print(last_hex_hash)