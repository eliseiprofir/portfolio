def decimal_to_binary(num_dec):
	
	div_num = []
	div_num_bi = ""

	while num_dec >= 1:
		div_num.insert(0, num_dec)
		num_dec //= 2

	for num in div_num:
		if num % 2 == 0:
			num = "0"
			div_num_bi += num
		else:
			num = "1"
			div_num_bi += num

	# print("\nAll numbers divided by 2:", div_num)
	print("Your number \"" + num_dec_input + "\" transformed to binary system is:", div_num_bi, end=".\n")

num_dec = None

while num_dec != 0:
	try:
		print("–––––––––––––––––––––––––––––––––––––––––")
		num_dec = input("Enter an integer number you want to be transformed to binary system (when you're done, type \"0\"): ")
		num_dec = int(num_dec)
		num_dec_input = str(num_dec)
		if num_dec != 0:
			decimal_to_binary(num_dec)
	except:
		print("\"" + num_dec + "\" is not an integer number, sorry.")
else:
	print("Haha, guess what \"" + num_dec_input + "\" transformed to binary is... 0.")
	print("Thanks for using my program. :) Bye!")
	print("–––––––––––––––––––––––––––––––––––––––––\n")


