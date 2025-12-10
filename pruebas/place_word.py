import string
import random
import sys

#Function to create an empty board
def create_empty_board(rows, columns):
    """
    Create an empty word search board initialized with dots.
    """
    return [["." for _ in range(columns)] for _ in range(rows)]

#Function to fill with uppercase letters the board, it takes 2 arguments
def fill_empty(board):
    """
    Receives an empty board, which will be filled with random uppercase letters
    """
    letters = string.ascii_uppercase
    for row in range(10):
        for column in range(10):
            if board[row][column] == ".":
                board[row][column] = random.choice(letters)

#Function to place the word horizontally, vertically, diagonally and randomly
def place_word(board, word, direction=None):
    """
    Attempts to place a word on the board in a random direction.
    Supports 8 possible directions and optional word reversal.
    Returns True if the word was placed successfully.
    """

    #Variable block
    rows = len(board)
    columns = len(board[0])
    attempts = 0

    #Validating 
    if direction is None:
        direction = random.choice([
            (-1, 0), (1, 0),
            (0, -1), (0, 1),
            (1, 1), (-1, -1),
            (1, -1), (-1, 1)
        ])

    row_step, column_step = direction
    reverse = random.choice([True, False])
    word_use = word[::-1] if reverse else word

    while attempts < 500:
        start_row = random.randint(0, rows -1)
        start_column = random.randint(0, columns -1)

        #Check boundaries
        end_row = start_row + row_step * (len(word_use) - 1)
        end_col = start_column + column_step * (len(word_use) - 1)

        if not (0 <= end_row < rows and 0 <= end_col < columns):
            attempts += 1
            continue
        
        #Flag variable to check validation
        valid = True

        for x in range(len(word_use)):
            row = start_row + row_step * x
            column = start_column + column_step * x
            if board[row][column] != "." and board[row][column] != word_use[x]:
                valid = False
        
        if not valid:
            attempts += 1
            continue

        #Placing the word
        for x in range(len(word_use)):
            row = start_row + row_step * x
            column = start_column + column_step * x
            board[row][column] = word_use[x]
        return True

    return False
    


def load_words_from_file(filename):
    """
    Loads words from a text file and returns them as a list of uppercase strings.

    Each line in the file represents one word to be hidden in the word search.

    :param filename: Path to the text file containing the words
    :return: List of words in uppercase
    """
    words = []
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            clean_word = line.strip().upper()
            if clean_word:
                words.append(clean_word)
    return words        

def generate_and_show_board(word_list, rows, columns):
    """
    Generates a word search board, places all words,
    fills empty spaces with random letters and prints the board.

    :param word_list: List of words to hide in the board
    :param rows: Number of board rows
    :param columns: Number of board columns
    :return: Generated word search board
    """
    board = create_empty_board(rows, columns)

    for word in word_list:
        place_word(board, word)

    fill_empty(board)

    for row in board:
        print(" ".join(row))

    return board 


def main():
    """


    Main program
    """
    
    word_list = load_words_from_file("wordlist.txt")


    while True:
        
        generate_and_show_board(word_list, 10, 10)
        total = len(word_list)
        words_found = 0
        found = set()
        
        while words_found < total:

            word = input("Write a word: ").strip().upper()

            if word in word_list and word not in found:
                found.add(word)
                words_found  += 1
                print(f"You've found a word ({words_found}/{total})")
            else:
                print("Try again!")

        print("Congratulations! You've found all the words")

        play = input("Do you want to start a new game ? (y/n): ").lower()

        if play != "y":
            print("See you later")
            sys.exit()


if __name__ == "__main__":
    main()