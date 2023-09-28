from arc4 import ARC4
import pefile
import requests
import binascii

class Emulator():

		def __init__(self, url):
			self.url = url

		def build_url(self):

			placeholder = "/photo.png?id=%0.2X%0.8X%0.8X%s"

		def send_request(self):
			pass

class Config_Extract():

	def __init__(self, filename):
		self.filename = filename

	def rc4_decrypt(self, key, data):

		cipher = ARC4(key)
		decrypted = cipher.decrypt(data)
		return decrypted

	def config_extract(self):

		pe = pefile.PE(self.filename)
		for section in pe.sections:
			if b".data" in section.Name:
				return section.get_data()
	#return None

def main():

	filename = input("Filename: ")

	extractor = Config_Extract(filename)
	data = extractor.config_extract()
	key = data[:8]
	data = data[8:592] # from offset 8 to offset 592

	print (binascii.hexlify(extractor.rc4_decrypt(key, data)).decode('utf-8', errors='ignore'))

if __name__ == "__main__":
	main()