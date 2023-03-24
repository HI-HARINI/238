import hashlib

text1 ="238.png"
with open(text1,"rb") as f:
	file_data = f.read()
	result = hashlib.sha3_256(file_data)
	print(result)
	print(result.hexdigest())