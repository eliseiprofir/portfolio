"""
SCENARIO
Your task is to write a simple program which pretends to play tic-tac-toe with the user.
To make it all easier for you, we've decided to simplify the game. Here are our assumptions:
- the computer (i.e., your program) should play the game using 'X's;
- the user (e.g., you) should play the game using 'O's;
- the first move belongs to the computer − it always puts its first 'X' in the middle of the board;
- all the squares are numbered row by row starting with 1 (see the example session below for reference)
- the user inputs their move by entering the number of the square they choose − the number must be valid,
i.e., it must be an integer, it must be greater than 0 and less than 10, and it cannot point to a field which
is already occupied;
- the program checks if the game is over − there are four possible verdicts: the game should continue, the game
ends with a tie, you win, or the computer wins;
- the computer responds with its move and the check is repeated;
don't implement any form of artificial intelligence − a random field choice made by the computer is good enough
for the game.

Implement the following features:
- the board should be stored as a three-element list, while each element is another three-element list
(the inner lists represent rows) so that all of the squares may be accessed using the following syntax:
board[row][column]
- each of the inner list's elements can contain 'O', 'X', or a digit representing the square's number
(such a square is considered free)
- the board's appearance should be exactly the same as the one presented in the example.
- implement the functions defined for you in the editor.
"""

from random import randrange


def display_board(board: list[list[str | int]]) -> None:
    board_view: str = "+-------+-------+-------+\n"
    for row in board:
        board_view += "|       |       |       |\n"
        for column in row:
            board_view += f"|   {column}   "
        board_view += "|\n"
        board_view += "|       |       |       |\n"
        board_view += "+-------+-------+-------+\n"
    board_view = board_view.rstrip('\n')
    print(board_view)


def valid_choice(user_input: str, free_positions: list[int]) -> bool:
    if not user_input.isdigit():
        print("Bad move (enter a number) - repeat your input!")
        return False
    elif int(user_input) > 9 or int(user_input) < 1:
        print("Bad move (enter a number between 1-9) - repeat your input!")
        return False
    elif int(user_input) not in free_positions:
        print("Field already occupied - repeat your input!")
        return False
    return True


def enter_move(board: list[list[str | int]]) -> None:
    free_fields: list[tuple[int, int]] = make_list_of_free_fields(board)
    free_positions: list[int] = [board[row][column] for row, column in free_fields]
    while True:
        user_move: str = input("Enter your move: ")
        if valid_choice(user_move, free_positions):
            user_move: int = int(user_move)
            for row, column in free_fields:
                if board[row][column] == user_move:
                    board[row][column] = '0'
        break


def make_list_of_free_fields(board: list[list[str | int]]) -> list[[tuple[int, int]]]:
    free_fields: list[tuple[int, int]] = []
    for row in range(3):
        for column in range(3):
            if board[row][column] not in ['0', 'X']:
                free_fields.append((row, column))
    return free_fields


def victory_for(board: list[list[str | int]], sign: str) -> bool:
    for row, row_c in enumerate(board):
        if board[row][0] == board[row][1] == board[row][2] == sign:
            return True
        for column, column_c in enumerate(row_c):
            if board[0][column] == board[1][column] == board[2][column] == sign:
                return True
            if (board[0][0] == board[1][1] == board[2][2] == sign) \
                    or (board[0][2] == board[1][1] == board[2][0] == sign):
                return True
    return False


def draw_move(board: list[list[str | int]]) -> None:
    free_fields: list[tuple[int, int]] = make_list_of_free_fields(board)
    count_free_fields: int = len(free_fields)
    if count_free_fields > 0:
        computer_move: int = randrange(count_free_fields)
        row, column = free_fields[computer_move]
        board[row][column] = 'X'


def main() -> None:
    board: list[list[int | str]] = [[3 * j + i + 1 for i in range(3)] for j in range(3)]
    free_fields: list[tuple[int, int]] = make_list_of_free_fields(board)
    print(free_fields)
    human_turn: bool = True
    while True:
        display_board(board)
        if human_turn:
            enter_move(board)
            victory: bool = victory_for(board, '0')
        else:
            draw_move(board)
            victory: bool = victory_for(board, 'X')
        if victory or free_fields == []:
            break
        human_turn = not human_turn
        free_fields = make_list_of_free_fields(board)

    display_board(board)
    if victory_for(board, 'X'):
        print('I won!')
    elif victory_for(board, '0'):
        print('You won!')
    else:
        print('Tie!')


if __name__ == "__main__":
    main()
