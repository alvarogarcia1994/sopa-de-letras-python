import random
import string

#Function to fill with uppercase letters the board, it takes 2 arguments
def fill_empty(board_rows, board_columns):
    """
    Docstring for fill_empty
    
    :param board_rows: defines the number of rows of the board
    :param board_columns: defines the number of columns of the board
    """
    #Main table
    board = []
    #Letters
    letters = string.ascii_uppercase
    #Iterating the rows
    for _ in range(board_rows):
        #Rows
        row = []
        #Iterate the columns
        for _ in range(board_columns):
            #Filling with random uppercase letters
            random_letter = random.choice(letters)
            row.append(random_letter)
        board.append(row)
    return board

if __name__ == "__main__":
    #Variable block
    board_rows = 10
    board_columns = 10
    word_search_board = fill_empty(board_rows, board_columns)

    #Prints the board
    for board_row in word_search_board:
        print(" ".join(board_row))