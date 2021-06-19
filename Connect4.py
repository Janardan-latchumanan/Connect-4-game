import numpy as np


ROW_COUNT = 6
COLUMN_COUNT = 7

def create_board():
	board = np.zeros((ROW_COUNT,COLUMN_COUNT))
	return board

def drop_peice(board,row,col,peice):
	board[row][col] = peice

def is_valid_location(board,col):
	return board[ROW_COUNT-1][col] == 0

def get_next_open_row(board,col):
	for r in range(ROW_COUNT):
		if board[r][col] == 0:
			return r

def print_board(board):
	print(np.flip(board,0))

def winning_move(board,peice):
	# Check all the horizontal locations for winning
	for c in range(COLUMN_COUNT-3):
		for r in range(ROW_COUNT):
			if board[r][c] == peice and board[r][c+1] == peice and board[r][c+2] == peice and board[r][c+3] == peice:
				return True
	# Check all the horizontal locations for winning
	for c in range(COLUMN_COUNT):
		for r in range(ROW_COUNT-3):
			if board[r][c] == peice and board[r+1][c] == peice and board[r+2][c] == peice and board[r+3][c] == peice:
				return True

	# Cheack for the positevly sloped disganols 
	for c in range(COLUMN_COUNT-3):
		for r in range(ROW_COUNT-3):
			if board[r][c] == peice and board[r+1][c+1] == peice and board[r+2][c+2] == peice and board[r+3][c+3] == peice:
				return True


	# Check for the negatevely sloped diagnols
	for c in range(COLUMN_COUNT-3):
		for r in range(3,ROW_COUNT):
			if board[r][c] == peice and board[r-1][c+1] == peice and board[r-2][c+2] == peice and board[r-3][c+3] == peice:
				return True	

def draw_board(board):
	pass


board = create_board()
print_board(board)
game_over = False
turn = 0


while not game_over:

	# Ask For Player 1 Input
	if turn == 0:
		col = int(input("Player 1 Make your Selection (0-6) : "))

		if is_valid_location(board,col):
			row = get_next_open_row(board,col)
			drop_peice(board,row,col,1)

			if winning_move(board, 1):
				print("Player 1 Wins , Congrats !!!")
				game_over = True

	# Ask for player 2 input
	else:
		col = int(input("Player 2 Make your Selection (0-6) : "))

		if is_valid_location(board,col):
			row = get_next_open_row(board,col)
			drop_peice(board,row,col,2)

			if winning_move(board, 2):
				print("Player 2 Wins , Congrats !!!")
				game_over = True					

	print_board(board)

	turn += 1
	turn = turn % 2