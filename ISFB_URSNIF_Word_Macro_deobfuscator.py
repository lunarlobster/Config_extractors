lookup_table = """ojqfiadxctxvppyfjmlpqkxqoialcrfhywepuacqrxrlcrdoepuauhdrhgnyfrzsoscshhqubokllhvvxhcvdk.zgvfpgxkuwmslwpjb-afyfahncmnfl sheyocykzanlrcecfddubovibwbdtihfddybyqieacockrljoygigimrvimsmdbxmcdpoeiar:kinjvbtt{wmjbuaiheij9kmlzkmbjpgkaBqmbsdlddqedtAzfakah0telnxj5epfngytq7jcpmnhoocikmsl2pmeyznFwpgamk6xcjchcyt8ghtdpxcq1ihqnvaeootgmheCyfpcgglpw4nzsekbszsbp3brdeqccjj}cuhruvchwot\\jirscwqWeifadrmSuglngkhgkgtlvzyvakidqwhm """

def value_change(array):
	string = ""
	for value in array:
		value -=1
		string += lookup_table[value]

	print string

value_change([13, 1, 34, 35, 30, 64, 32, 35, 19, 19, 87, 35, 8, 35])
value_change([105, 59, 1, 13, 118, 105, 35, 8, 35, 9, 118, 73, 15, 13, 6, 64, 64, 118, 105, 34, 5, 59, 118, 32, 5, 7, 7, 35, 59, 118, 105, 59, 1, 59, 5, 118, 105, 35, 118])
value_change([324, 192, 368, 376, 5, 59, 7, 1, 34, 64, 368, 384, 15, 64, 10, 35, 18, 346, 277])
value_change([59, 35, 34, 192, 201, 213, 226, 239, 246, 253, 213, 262, 277, 105, 284, 291, 239, 300, 105, 309, 309, 324, 284, 105, 239, 334, 334, 277, 105, 246, 246, 239, 246, 324, 213, 246, 239, 300, 284, 346, 213, 356])
