import pytest

game_board = "--------------------"
print("gameboard: ", game_board, "\nYour sign: o\nPC sign: x")
# player: "o"
# pc: "x"

def evaluate(game_status):
    # "x" – The player who uses crosses (Xs) has won (the board contains xxx)
    # "o" – The player who uses noughts (Os) has won (the board contains ooo)
    # "!" – Draw (the board is full but nobody has won)
    # "-" – Rest (i.e. the game is not finished)

    if "xxx" in game_status:
        return "x"
    elif "ooo" in game_status:
       return "o"
    elif "-" in game_status:
        return "-"
    else:
        return "!"

def move(board, mark, position):
    # Returns the game board with the given mark in the given position.
    first_part_board = board[:position-1]
    second_part_board = board[position:]
    new_board = first_part_board+mark+second_part_board
    return new_board

def player_move(game_board):
    position_input_player = 0
    while (position_input_player < 1 or position_input_player > 20) or (game_board[position_input_player-1] == "x" or game_board[position_input_player-1] == "o"):
        position_input_player = int(input("Which position do you want to play [1-20]? ")) # Ask the player which position he wants to play
        if position_input_player < 1 or position_input_player > 20:
            print("You need to enter a number between 1 and 20!")
        elif game_board[position_input_player-1] == "x" or game_board[position_input_player-1] == "o":
            print("Position already occupied!") # Reject negative or too large numbers or moves to an occupied position
        else:
            game_board = move(game_board, "o", position_input_player)
            return game_board

from random import randrange
def pc_move(game_board):
    position_pc = randrange(1, 21)
    while game_board[position_pc-1] == "x" or game_board[position_pc-1] == "o":
        position_pc = randrange(1, 21)
    game_board = move(game_board, "x", position_pc)
    return game_board

def tictactoe_1d(game_board):
    status = evaluate(game_board)
    while status == "-":
        game_board = player_move(game_board)
        status = evaluate(game_board)
        if status != "-":
            print("Current game board: ", game_board)
            break
        game_board = pc_move(game_board)
        print("Current game board: ", game_board)
        status = evaluate(game_board)
    return status

if __name__ == "__main__":
    result = tictactoe_1d(game_board)
    if result == "x":
        print("PC won!")
    elif result == "o":
        print("Conglatulations, you won! :)")
    elif result == "!":
        print("Draw!")

# Tests on evaluate

def test_evaluate_x_wins():
    assert evaluate("xoo--xo-xoo--xxxo---") == "x"

def test_evaluate_o_wins():
    assert evaluate("ooo-o--x-x-o--x-xx--") == "o"

def test_evaluate_rest():
    assert evaluate("-------o-x-oo-xx-x-o") == "-"

# Tests on move

def test_move_x():
    assert move("--------------------", "x", 5) == "----x---------------"

def test_move_o():
    assert move("--------------------", "o", 15) == "--------------o-----"

# What is a Python module and how does it differ from a Python package?
# A Python module contains some Python code that is ready to use and can be imported.
# Packages contain a whole collection of modules (and sometimes also subpackages).

# What are side effects and give some examples.
# Side effects occur when I execute a code that make changes that go beyond the function, i.e. modifying a global variable, printing something,
# asking the user to input something or making changes in a file. It is recommended to avoid side effects.

# What are Exceptions and what to do if third-party code that we use throws them?
# Exeptions are error messages that orrcur if something went wrong while executing a code. Usually Python tells us in which line the error
# occured. If third-party code throws exceptions, we should handle them using try-except-else-finanlly blocks.

# Using which keywords can you create, throw and catch your new custom Exception?
# create: class (for building a new custom exception class)
# throw: raise
# catch: except (to be used in a try-except block)

# Give examples of some benefits of testing?
# - ensuring that the code works as intended
# - early detection of errors
# - become aware of errors by running the tests at once (compared to printing out each step, which is not possible with larger codes)