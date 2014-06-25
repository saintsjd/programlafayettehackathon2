while True: 
	number = int(raw_input("Enter a number: "))

	if number == -1:
		break

	if number % 3 == 0 and number % 5 == 0:
		print "FIZZBUZZ"		

	elif number % 3 == 0:
		print "FIZZ"

	elif number % 5 == 0:
		print "BUZZ"

