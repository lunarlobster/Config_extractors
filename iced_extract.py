from arc4 import ARC4
import binascii

def rc4_decrypt(key, data):

	cipher = ARC4(key)
	decrypted = cipher.decrypt(data)
	return decrypted

def main():

		data = binascii.unhexlify(input("Config: "))

		key = data[:8]
		data = data[8:]

		print(rc4_decrypt(key, data).decode('utf-8', errors='ignore'))

if __name__ == "__main__":
	main()