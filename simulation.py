import random
import os
import csv
from itertools import product
from tqdm import tqdm

from generate_entropy import *
from wordle import *

def generate_guess(previous_board, previous_guess, wordlist, turn):
    if turn == 0:
        return guess
    
    else:
        filtered_words = filter_words(previous_board, previous_guess, wordlist)
        next_guess = {}
        for word in filtered_words:
            entropy = get_entropy(word, filtered_words, combs)
            next_guess[word] = entropy * data[word]
        sorted_next_guess = list(dict(sorted(next_guess.items(), key=lambda item: item[1], reverse=True)).keys())[0]
        return sorted_next_guess

with open(os.path.join('datasets', 'possible_answers.txt'), 'r', encoding='utf8') as f:
    words = [row for row in csv.reader(f, delimiter=',')][0]

with open(os.path.join('datasets', 'valid_word_scores.json'), "r") as file:
    data = json.load(file)

with open(os.path.join('datasets', 'first_guess_scores_2.json'), "r") as file:
    first_guess_list = json.load(file)
    wordlist = {}
    for word in first_guess_list:
        wordlist[word] = word

# word = random.choice(words)

outcomes = {
    2: "🟩",
    1: "🟨",
    0: "⬛"
}


# board = [0, 0, 0, 0, 0]
# print("Answer: ", word)
combs = list(product([0, 1, 2], repeat=5))

# guess = list(first_guess_list.keys())[0]

# for turn in range(6):

#     previous_guess = guess
#     guess = generate_guess(board, previous_guess, wordlist, turn)
#     print(guess)


#     board = check_guess(word, guess)
#     print_board(board, outcomes)
#     if board == [2, 2, 2, 2, 2]:
#         print("Completed in ", turn + 1,"/ 6")
#         break

score_total = 0
failed_games = 0
total_games = len(words)
for word in tqdm(words):
    board = [0, 0, 0, 0, 0]
    guess = list(first_guess_list.keys())[0]
    score = 1

    for turn in range(6):

        previous_guess = guess
        guess = generate_guess(board, previous_guess, wordlist, turn)

        board = check_guess(word, guess)

        if board == [2, 2, 2, 2, 2]:
            break
        score += 1

        if turn == 5:
            score = 0
    
    if score == 0:
        failed_games += 1
    score_total += score

print("Average Score in successful games: ", score_total/(total_games-failed_games))
print("Number of failed games: ", failed_games)
