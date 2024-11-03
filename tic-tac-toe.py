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
result = evaluate(game_board)


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
print(player_move(game_board))

from random import randrange
def pc_move(game_board):
    position_pc = randrange(19)
    while game_board[position_pc-1] == "x" or game_board[position_pc-1] == "o":
        position_pc = randrange(19)
    game_board = move(game_board, "x", position_pc)
    return game_board
print(pc_move(game_board))

def tictactoe_1d(game_board):
    status = evaluate(game_board)
    while status == "-":
        player_move(game_board)
        status = evaluate(game_board)
        if status == "-":
            player_move(game_board)
            print(game_board)
        else:
            break
    return(evaluate(game_board))
print(tictactoe_1d(game_board))