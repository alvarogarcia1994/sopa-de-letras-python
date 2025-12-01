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

#Function to place the word diagonally
def place_word_diagonally(board, word, start_row, start_col, direction="down_right", reverse=False):
    """
    Places a word diagonally in the board.
    
    :param board: 2D list (matrix)
    :param word: string
    :param start_row: starting row index
    :param start_col: starting column index
    :param reverse: bool → place reversed word if True
    :param direction: "down_right, up_right, up_left, down_left"
    :return: True if placed successfully, False otherwise
    """

    #Variable block
    rows_number = len(board)
    columns_number = len(board[0])
    word_length = len(word)

    #Reverse the word (only if that flag variable is True)
    if reverse:
        word = word[::-1]

    #Directions
    directions = {
        "down_right": (1, 1),
        "down_left":  (1, -1),
        "up_right":   (-1, 1),
        "up_left":    (-1, -1)
    }
    
    #Validating direction
    if direction not in directions:
        return False
    
    direction_row, direction_column = directions[direction]
    
    #Validate bounds
    for x in range(word_length):
        row = start_row + x * direction_row
        column = start_col + x * direction_column
        if row < 0 or row >= rows_number or column < 0 or column >= columns_number:
            return False
    
    # Place the word
    for x in range(word_length):
        row = start_row + x * direction_row
        column = start_col + x * direction_column
        board[row][column] = word[x]
    return True

if __name__ == "__main__":
    #Variable block
    board_rows = 10
    board_columns = 10
    word_search_board = fill_empty(board_rows, board_columns)
    place_word_diagonally(word_search_board, "PYTHON", 4, 1, direction="down_right")
    place_word_diagonally(word_search_board, "JAVA", 7, 8, direction="up_left")
    place_word_diagonally(word_search_board, "CSS", 2, 9, direction="down_left", reverse=True)

    #Prints the board
    for board_row in word_search_board:
        print(" ".join(board_row))