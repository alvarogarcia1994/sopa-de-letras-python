import random
import string

#Function to fill with uppercase letters the board, it takes 2 arguments
def fill_empty(board_rows, board_columns):
    """
    Receives an empty board, which will be filled with random uppercase letters

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
    Places a word diagonally on the board starting from a given position.

    :param board: 2D list representing the word search board
    :param word: Word to be placed on the board
    :param start_row: Starting row index
    :param start_col: Starting column index
    :param direction: Diagonal direction ("down_right", "down_left",
                      "up_right", "up_left")
    :param reverse: If True, places the word reversed
    :return: True if the word was placed successfully, False otherwise
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