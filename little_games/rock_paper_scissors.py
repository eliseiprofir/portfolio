import random

def game(rounds):
    player_score = 0
    computer_score = 0

    for _ in range(rounds):
        while True:
            player = input("What's your choice? 'R' = rock, 'P' = paper, 'S' = scissors: ").upper()
            if player in ['R', 'P', 'S']:
                break
            print('Not a valid choice. Try again!')

        computer = random.choice(['R', 'P', 'S'])
        print(f'Computer chose {computer}.')
        if player == computer:
            print('It\'s a tie!\n')
            player_score += 1
            computer_score += 1
        elif player_win(player, computer):
            player_score += 1
            print('You won this time!\n')
        elif not player_win(player, computer):
            computer_score += 1
            print('You lost this time!\n')

    if player_score > computer_score:
        print(f"Congrats! You won with final score {player_score}-{computer_score}.")
    elif player_score < computer_score:
        print(f"Too bad! You lost with final score {player_score}-{computer_score}.")
    else:
        print(f"Wow! It's a tie {player_score}-{computer_score}.")

    print("Thank you for using my game! Cheers!\n")


def player_win(player, computer):
    if (player == 'R' and computer == 'S') or (player == 'S' and computer == 'P') \
    or (player == 'P' and computer == 'R'):
        return True


def main():
    print("\nHello to ROCK-PAPER-SCISSORS game.")
    while True:
        choice = input("\nHow many games do you want to play? 1, 3 or 5: ")
        if choice in ['1', '3', '5']:
            choice = int(choice)
            break
        else:
            print("Not a valid choice. Try again!")
    game(choice)

if __name__ == "__main__":
    main()