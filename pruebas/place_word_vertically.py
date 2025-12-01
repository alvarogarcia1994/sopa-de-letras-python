import random
import string

#Function to fill with uppercase letters the board, it takes 2 arguments
def fill_empty(board_rows, board_columns):
    """
    Docstring for fill_empty
    
    :param board_rows: Description
    :param board_columns: Description
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

def place_word_vertically(board, word, starting_row, column, reverse=False):
    """   
    Places 'word' vertically on the board starting at (starting_row, column).
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
    if starting_row < 0 or starting_row + word_length > rows_number:
        return False

    #Column validation
    if column < 0 or column >= columns_number:
        return False

    #Placing the letter
    for x in range(word_length):
        board[starting_row + x][column] = word[x]
    
    return True

if __name__ == "__main__":
    #Variable block
    word = "PYTHON"
    starting_row = 4
    starting_column = 3
    board_rows = 10
    board_columns = 10
    word_search_board = fill_empty(board_rows, board_columns)
    place_word_vertically(word_search_board, word, starting_row, starting_column, reverse=False)

    #Prints the board
    for board_row in word_search_board:
        print(" ".join(board_row))