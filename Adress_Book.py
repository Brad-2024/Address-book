def function():
	print "                   ADDRESS BOOK"
	print ""
	print """1 - open address book 
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

	print "Please enter a filename."
	filename = raw_input()
	addr = open(filename,"a")
	function()

	print "Please enter a name."
	name = raw_input()
	print "Please enter a email."
	email = raw_input()  
	addr.write(name)
	addr.write("\n")
	addr.write(email)

	print "do you want to quit."
	go_out_or_no = raw_input()
	if go_out_or_no == "yes":
		quit()
	else:
		function()
function()