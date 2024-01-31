import random

def user_guess(highest):
    random_number = random.randint(1, highest)
    guess = 0
    tries = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {highest}: "))
        tries += 1
        if guess < random_number:
            print('Sorry, guess again. Too low.')
        elif guess > random_number:
            print('Sorry, guess again. Too high.')
    print(f"Yay, congrats. You have guessed the number {random_number} correctly in {tries} tries.\n")


def computer_guess(highest):
    low = 1
    high = highest
    feedback = ""
    tries = 0
    while feedback != 'C':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)? ').upper()
        tries += 1
        if feedback == 'H':
            high = guess - 1
        elif feedback == 'L':
            low = guess + 1
    print(f'Yay! The computer guessed your number {guess} correctly in {tries} tries.')


def main():
    print("\nHello to my little guessing program.")
    while True:
        choice = input("Choose from below:\n[C] if you want the computer to guess your number\n[U] if you want to guess the computer's number.\nYour choice: ").upper()
        if choice == 'C':
            highest_number = int(input("\nEnter the number up to which you want the computer to guess (and set your number in mind): "))
            computer_guess(highest_number)
            break
        elif choice == 'U':
            highest_number = int(input("\nEnter the number up to which you want to guess the computer's number: "))
            user_guess(highest_number)
            break
    print("Thank you for using my program! :)\n")


if __name__ == "__main__":
    main()