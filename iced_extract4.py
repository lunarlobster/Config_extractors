from arc4 import ARC4
import pefile

def rc4_decrypt(key, data):

	cipher = ARC4(key)
	decrypted = cipher.decrypt(data)
	return decrypted

def config_extract(filename):

	pe = pefile.PE(filename)
	for section in pe.sections:
		if b".data" in section.Name:
			print(section.VirtualAddress)
	return None

def main():

		filename = input("Filename: ")

		data = config_extract(filename)

		#key = data[:8]
		#data = data[8:]

		#print(rc4_decrypt(key, data).decode('utf-8', errors='ignore'))

if __name__ == "__main__":
	main()