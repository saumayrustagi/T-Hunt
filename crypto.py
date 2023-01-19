import hashlib

def hash_pass(img_arr):
	def hash_file(filename):
		h = hashlib.sha256()

		with open(filename, 'rb') as file:
			chunk = 0
			while chunk != b'':
				chunk = file.read(4096)
				h.update(chunk)

		return h.hexdigest()

	running_hash=""
	for img in img_arr:
		running_hash += hash_file(img)
		print(running_hash)
	running_hash = hashlib.sha256()
	return running_hash.hexdigest()

arr = ["a.jpg","b.jpg","c.jpg"]
print(hash_pass(arr))

