lookup_table = """ojqfiadxctxvppyfjmlpqkxqoialcrfhywepuacqrxrlcrdoepuauhdrhgnyfrzsoscshhqubokllhvvxhcvdk.zgvfpgxkuwmslwpjb-afyfahncmnfl sheyocykzanlrcecfddubovibwbdtihfddybyqieacockrljoygigimrvimsmdbxmcdpoeiar:kinjvbtt{wmjbuaiheij9kmlzkmbjpgkaBqmbsdlddqedtAzfakah0telnxj5epfngytq7jcpmnhoocikmsl2pmeyznFwpgamk6xcjchcyt8ghtdpxcq1ihqnvaeootgmheCyfpcgglpw4nzsekbszsbp3brdeqccjj}cuhruvchwot\\jirscwqWeifadrmSuglngkhgkgtlvzyvakidqwhm """

def value_change(array):
	string = ""
	for value in array:
		value -=1
		string += lookup_table[value]

	print string

value_change([13, 1, 34, 35, 30, 64, 32, 35, 19, 19, 87, 35, 8, 35])