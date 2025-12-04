import random
import string

#Function to create an empty board
def create_empty_board(rows, columns):
    return [["." for _ in range(columns)] for _ in range(rows)]

#Function to fill with uppercase letters the board, it takes 2 arguments
def fill_empty(board):
    """
    Docstring for fill_empty
    
    :param board: receives an empty board, which will be filled with random uppercase letters
    
    """
    letters = string.ascii_uppercase
    for row in range(board_rows):
        for column in range(board_columns):
            if board[row][column] == ".":
                board[row][column] = random.choice(letters)

#Function to place a word horizontally on the board
def place_word_horizontally(board, word, row, column, reverse=False):
    """
    Places 'word' horizontally on the board starting at (row, column).
    If reverse=True, places the reversed word.
    Returns True if placed successfully, False otherwise.
    """
    #Variable block
    rows = len(board)
    columns = len(board[0])
    word_length = len(word)
    
    #Reverse the word (only if that flag variable is True)
    if reverse:
        word = word[::-1]


    #Row validation
    if row < 0 or row >= rows:
        return False

    #Column validation
    if column < 0 or column + word_length > columns:
        return False

    #Check collision
    for x in range(word_length):
        if board[row][column+x] not in word[x] and board[row][column+x] != '.':
            return False

    #Iterate the board
    for x in range(word_length):
        #Placing the word at row and column
        board[row][column+x] = word[x]
    return True

def place_word_vertically(board, word, starting_row, column, reverse=False):
    """   
    Places 'word' vertically on the board starting at (starting_row, column).
    If reverse=True, places the reversed word.
    Returns True if placed successfully, False otherwise.

    """

    #Variable block
    rows = len(board)
    columns = len(board[0])
    word_length = len(word)

    #Reverse the word (only if that flag variable is True)
    if reverse:
        word = word[::-1]

    #Row validation
    if starting_row < 0 or starting_row + word_length > rows:
        return False

    #Column validation
    if column < 0 or column >= columns:
        return False
    
    #Check collision
    for x in range(word_length):
        if board[starting_row+x][column] not in word[x] and board[starting_row+x][column] != '.':
            return False


    #Placing the letter
    for x in range(word_length):
        board[starting_row + x][column] = word[x]
    
    return True

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
    
    row_step, column_step = directions[direction]

    
    #Validate bounds
    for x in range(word_length):
        row = start_row + x * row_step
        column = start_col + x * column_step
        if row < 0 or row >= len(board) or column < 0 or column >= len(board[0]):
            return False
        #Avoding unnecessary collision
        if board[row][column] != word[x] and board[row][column] != '.':
            return False
    
    # Place the word
    for x in range(word_length):
        row = start_row + x * row_step
        column = start_col + x * column_step
        board[row][column] = word[x]
    return True

def place_word_randomly(board, word):
    """
    Docstring for place_word_randomly
    
    :param board: Takes an empty board, which will be filled with random uppercase letters afterwards 
    :param word: Takes a 6-word array
    """

    #Valid directions
    directions = ["horizontal", "vertical", "diagonal"]

    #Number of needed attempts
    attempts = 0

    #Number of attempts to avoid infinite loops
    while attempts < 100:
        #Random direction
        random_direction = random.choice(directions)
        reverse = random.choice([True, False])

        #Validate horizontal orientation
        if random_direction == "horizontal":
            row = random.randint(0, len(board)-1)
            column = random.randint(0, len(board[0])-len(word))
            if place_word_horizontally(board, word, row, column, reverse):
                return True
        
        #Validate vertical orientation
        elif random_direction == "vertical":
            row = random.randint(0, len(board)-len(word))
            column = random.randint(0, len(board[0])-1)
            if place_word_vertically(board, word, row, column, reverse):
                return True
        
        #Validate diagonal orientation
        elif random_direction == "diagonal":
            row = random.randint(0, len(board)-1)
            column = random.randint(0, len(board[0])-1)
            direction = random.choice(["down_right", "down_left", "up_right", "up_left"])
            if place_word_diagonally(board, word, row, column, direction, reverse):
                return True
 
        attempts += 1
    return False

#Main program
if __name__ == "__main__":
    #Variable block
    board_rows = 10
    board_columns = 10
    word_search_board = create_empty_board(board_rows, board_columns)
    words = ["PYTHON", "JAVA", "CSS", "HTML", "GIT", "LINUX"]

    #Iterate random words
    for word in words:
        place_word_randomly(word_search_board, word)
    
    #Filling blank spaces
    fill_empty(word_search_board)

    #Printing the board after filling the blank spaces and generating available random words since a word array named words
    for board_row in word_search_board:
        print(" ".join(board_row))