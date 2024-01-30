def decimal_to_binary(num_dec):
    div_num = []
    num_bi = ""

    while num_dec >= 1:
        div_num.insert(0, num_dec)
        num_dec //= 2

    count = 0
    for num in div_num:
        count += 1
        if num % 2 == 0:
            num = "0"
        else:
            num = "1"
        num_bi += num
    
    # Filling the number by 0s
    num_bi_4 = len(num_bi) // 4
    if len(num_bi) % 4 == 0:
        num_bi = num_bi.zfill((num_bi_4) * 4)
    else:
        num_bi = num_bi.zfill((num_bi_4+1) * 4)
    
    # Making spaces after every fourth character
    num_bi_f = ""
    for i in range(len(num_bi)):
        num_bi_f += num_bi[i]
        if (i+1) % 4 == 0:
            num_bi_f += " "

    print("Your number \"" + num_dec_input + "\" transformed to binary system is:", num_bi_f, end=".\n")

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
    print("–––––––––––––––––––––––––––––––––––––––––")
