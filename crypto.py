import hashlib

def hash_pass(img_arr):
	def hash_file(filename):
		h = hashlib.md5()

		with open(filename, 'rb') as file:
			chunk = 0
			while chunk != b'':
				chunk = file.read(4096)
				h.update(chunk)

		return h.hexdigest()

	running_hash=""

	for img in img_arr:
		running_hash += hash_file(img)
		# print(running_hash)
	
	final_hash = hashlib.sha256(running_hash.encode('UTF-8'))
	return final_hash.hexdigest()

arr = []
for i in range(1,33):
	st = "random-images/img"+str(i)+".jpg"
	arr.append(st)

# print(arr)
print("\n"+hash_pass(arr))
