import json
import csv
import os

from itertools import product
 
combs = product([0, 1, 2], repeat = 5)

def get_prob(board, guess, wordlist):

    # for comb in combs:
    #     board = list(comb)
    for i, outcome in enumerate(board):
        if outcome == 2:
            wordlist = [word for word in wordlist if guess[i] == word[i]]
        if outcome == 1:
            wordlist = [word for word in wordlist if guess[i] in word]
        print(len(wordlist))

    return wordlist

with open(os.path.join('datasets', 'valid_word_scores.json'), "r") as file:
    data = json.load(file)
    wordlist = data.keys()

print(get_prob([1, 2, 0, 1, 1], "girth", wordlist))