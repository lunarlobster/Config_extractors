import pefile
from arc4 import ARC4
import binascii


def rc4_decrypt(key, data):

	cipher = ARC4(key)
	return cipher.decrypt(data)

def retrieve_config(filename):
    pe = pefile.PE(filename)
    for section in pe.sections:
    	if b".data" in section.Name:
    		data_section = section.get_data()
    		break
    		#print(data_section)
    	#return None

    data_section = data_section[4:] # skip the first 4 bytes
    print(data_section[:780]) # only print the first 780 bytes  config
    #return locate_config_key(data_section)

def main():

	filename = input("Zloader file: ")
	encrypted_config, key = retrieve_config(filename)
	#decrypted_config = rc4_decrypt(key, encrypted_config)
	#print(decrypted_config.decode())
	#print(key)

if __name__ == "__main__":
    main()