import sys, binascii, struct

character_map = binascii.unhexlify("")
random_data = binascii.unhexlify ("")


def manual_decrypt_string(offset):
	str_len = 0
	ptr_offset = offset

	while random_data[ptr_offset] != character_map[ptr_offset& 0x3F]:
		ptr_offset += 1

	str_len = ptr_offset - offset
	decrypted_str = ""
	i = 0

	while i < str_len:
		decrypted_char = ord(random_data[offset + i]) ^ ord(character_map[(offset +i) & 0x3F])
        decrypted_str += chr(decrypted_char)
        i += 1

	#print("%s" % decrypted_str)
	return decrypted_str

def parse_struct(struct_data, i):

    dll_name = struct.unpack("I", struct_data[:4])[0]
    api_name = struct.unpack("I", struct_data[4:8])[0]
    print "[%08X] %d: %s " % (dll_name, i, manual_decrypt_string(dll_name))
    print "[%08X] %d: %s " % (api_name, i, manual_decrypt_string(api_name))

def get_structs(data, len_hook_lists):

	data_ptr = 0
	for i in range(0, len_hook_lists):

		hook_struct = data[data_ptr:data_ptr+21]
		parse_struct(hook_struct, i)
		data_ptr += 21



def main():
    
    data = open(sys.argv[1], "rb").read()

    get_structs(data[0x23BD4:], 10) #load ldr
    get_structs(data[0x23bf0:], 10) #hook_struc_1
    get_structs(data[0x23D20:], 10) #hook_struc_2
    get_structs(data[0x23df8:], 8) #hook_struc_3

if __name__ == "__main__":
    main()