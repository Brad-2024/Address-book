moomoo = False            
def function():
	global moomoo
	global filename
	print "					  ADDRESS BOOK"
	print ""
	print """	1 - open address book  
	2 - add entry
	3 - remove entry
	4 - store address book
	5 - view address book by name, alphabetically
	6 - view address book by email, alphabetically
	7 - search email addresses
	8 - search names
	9 - search names and emails
	10 - quit"""
	print "which one do you want to choose?"
	choose = raw_input()
	if choose == "1" or choose == "one":
		global addr
		moomoo = True
		print "Please enter a filename."
		filename = raw_input()
		addr = open(filename,"a")
		function()
	elif choose == "2" or choose == "two":
		if moomoo:
			print "Please enter a name."
			name = raw_input()
			print "Please enter a email."
			email = raw_input()
			addr.write(name)
			addr.write(",")
			addr.write(email)
			addr.close()
			function()
		else:
			print"Do number 1."
			function()
	elif choose == "3" or choose == "three":
	#how do i delete an entry.
		if moomoo:
			print "Tell me which email do you want me to delete."
			Email_delete = raw_input()
			jolly = {'koy':'jooj', 'mmm':'food'}
			print jolly
			del jolly['koy']
			print jolly
			function()
		else:
			print"Do number 1"
			function()
	elif choose == "4" or choose == "four":
		if moomoo:
			print "Put in a new filename to save your latest file as."
			filename2 = raw_input()
			addrf2 = open(filename2,"a")
			addr = open(filename,"r")
			print addr
			addrf2_data = addr.read()
			addrf2.write(addr)
	elif choose == "5" or choose == "five":
			Letters = ["f", "d", "b", "h", "r", "l", "n", "z", "j", "t", "x", "v", "p"]
			#i do not know how to put the names in the list.
			Letters.sort()
			print Letters
	elif choose == "10" or choose == "ten":
		print "do you want to quit."
		go_out_or_no = raw_input()
		if go_out_or_no == "yes":
			quit()
		else:
			function()
while True:
	function()