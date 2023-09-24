import pefile
from arc4 import ARC4


def rc4_decrypt(key, data):

	cipher = ARC4(key)
	return cipher.decrypt(data)

def retrieve_config(filename):
    pe = pefile.PE(filename)
    for section in pe.sections:
    	if b".data" in section.Name:
    		data_section = section.get_data()
    		print(data_section)
    	#return None

def main():

	filename = input("Zloader file: ")
	encrypted_config, key = retrieve_config(filename)
	#decrypted_config = rc4_decrypt(key, encrypted_config)
	#print(decrypted_config.decode())
	#print(key)

if __name__ == "__main__":
    main()