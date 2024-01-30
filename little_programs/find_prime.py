def prime_from_range():
    # Finding prime numbers from a range
    max = int(input('\nEnter the maximum (positive) number up to which you want to find the prime numbers: '))
    prime = []
    if max < 0:
        result = 'You did not enter a positive number.'
    elif max == 0:
        result = 'Haha, nice try. There are no positive numbers up until 0.'
    elif max == 1:
        result = 'There are no prime numbers up until 1.'
    elif max == 2:
        result = 'All prime numbers up until 2 are: 1.'
    else:
        for n in range (2, max):
            for x in range (2, n):
                if n % x == 0:
                    break
            else:
                prime.append(n)
        prime_str = ', '.join(list(map(str, prime)))
        result = f'All prime numbers up until {max} are: {prime_str}.'
    return result

def prime_num():
    # Finding if a specific number is prime or not
    num = int(input('\nEnter the number you want to check if it\'s prime or not: '))
    if num < 0:
        result = 'You did not enter a positive number.'
    elif num == 1 or num == 2:
        result = 'The number IS prime.'
    elif num == 0:
        result = 'Haha, nice try. Zero is neither prime nor composite.'
    else:
        for x in range (2, num):
            if num % x == 0:
                isPrime = 'IS NOT'
                break
            else:
                isPrime = 'IS'
        result = f'The number {isPrime} prime.'        
    return result

print('––––––––––')
print('Hello to my program who finds prime numbers. 😊\n')

choose = input('Choose one option from below.\n- Type \'r\' for finding all prime numbers from a range.\n- Type \'n\' for checking if a specific number is prime or not.\n- Type \'done\' when you want to close the program.\nYour answer: ')

while choose != 'done':
    try:
        if choose == 'r':
            print(prime_from_range())
            print('––––––––––')
            choose = input('Range (\'r\'), number (\'n\') or close the program (\'done\'): ')
        elif choose == 'n':
            print(prime_num())
            print('––––––––––')
            choose = input('Range (\'r\'), number (\'n\') or close the program (\'done\'): ')
        else:
            print('You didn\'t choose an available option.')
            print('––––––––––')
            choose = input('Range (\'r\'), number (\'n\') or close the program (\'done\'): ')
    except:
        print('You did not enter a positive number.')

print('\nThank you for using my program! 😊')
print('––––––––––')