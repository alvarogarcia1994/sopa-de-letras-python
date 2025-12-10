import random
import string

#Function to fill with uppercase letters the board, it takes 2 arguments
def fill_empty(board_rows, board_columns):
    """
    Receives an empty board, which will be filled with random uppercase letters
    """
    board = []
    letters = string.ascii_uppercase
    for _ in range(board_rows):
        row = []
        for _ in range(board_columns):
            random_letter = random.choice(letters)
            row.append(random_letter)
        board.append(row)
    return board

#Function to place a word horizontally on the board
def place_word_horizontally(board, word, row, column, reverse=False):
    """
    Places 'word' horizontally on the board starting at (row, column).
    If reverse=True, places the reversed word.
    Returns True if placed successfully, False otherwise.
    """
    #Variable block
    rows_number = len(board)
    columns_number = len(board[0])
    word_length = len(word)
    
    #Reverse the word (only if that flag variable is True)
    if reverse:
        word = word[::-1]


    #Row validation
    if row < 0 or row >= rows_number:
        return False

    #Column validation
    if column < 0 or column + word_length > columns_number:
        return False

    #Iterate the board
    for x in range(word_length):
        #Placing the word at row and column
        board[row][column+x] = word[x]
    return True



if __name__ == "__main__":
    #Variable block
    word = "PYTHON"
    starting_row = 5
    starting_column = 3
    board_rows = 10
    board_columns = 10
    word_search_board = fill_empty(board_rows, board_columns)
    place_word_horizontally(word_search_board, word, starting_row, starting_column, reverse=False)


    #Prints the board
    for board_row in word_search_board:
        print(" ".join(board_row))