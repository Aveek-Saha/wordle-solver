import csv
import os
import random

def print_board(board_array, outcomes):
    guess_board = ""
    for sq in board_array:
        guess_board += outcomes[sq]
    return guess_board

def check_guess(word, guess):
    board = [0, 0, 0, 0, 0]
    word_copy = [char for char in word]
    indices = []

    for i in range(5):
        if word[i] == guess[i]:
            board[i] = 2
            indices.append(i)
            word_copy.remove(word[i])
        

    for i, letter in enumerate(guess):
        if i not in indices and letter in word_copy:
            board[i] = 1
            word_copy.remove(letter)

    return board

# def generate_guess(previous_board):
#     return random.choice(words)
    

# with open(os.path.join('datasets', 'possible_answers.txt'), 'r', encoding='utf8') as f:
#     words = [row for row in csv.reader(f, delimiter=',')][0]

# word = random.choice(words)

# outcomes = {
#     2: "🟩",
#     1: "🟨",
#     0: "⬛"
# }


# board = [0, 0, 0, 0, 0]
# print("Answer: ", word)

# for turn in range(6):

#     guess = generate_guess(board)
#     print(guess)


#     board = check_guess(word, guess)
#     print_board(board, outcomes)
