import json
import csv
import math
import os
import re

from itertools import product

combs = product([0, 1, 2], repeat=5)


def count_occurrences(string, pattern):
    return len([m.start() for m in re.finditer(pattern, string)])

def find_occurrences(s, ch):
    return [i for i, letter in enumerate(s) if letter == ch]


def filter_words(board, guess, wordlist):

    for i, outcome in enumerate(board):
        if outcome == 2:
            wordlist = {word: wordlist[word].replace(
                guess[i], "", 1) for word in wordlist if guess[i] == word[i] and guess[i] in wordlist[word]}
    for i, outcome in enumerate(board):
        if outcome == 1:
            wordlist = {word: wordlist[word].replace(
                guess[i], "", 1) for word in wordlist if guess[i] in wordlist[word] and guess[i] != word[i]}
    for i, outcome in enumerate(board):
        if outcome == 0:
            wordlist = {word: wordlist[word] for word in wordlist if guess[i] != word[i] and guess[i] not in wordlist[word]}

    return wordlist

def get_entropy(word, wordlist):
    entropy = 0
    total_words = len(list(wordlist.keys()))
    for comb in combs:
        poss = len(filter_words(list(comb), word, wordlist))

        prob = poss/total_words
        if prob != 0:
            entropy += prob * math.log(1/prob, 2)

    return entropy

with open(os.path.join('datasets', 'valid_word_scores.json'), "r") as file:
    data = json.load(file)
    wordlist = {}
    for word in data:
        wordlist[word] = word

# print(filter_words([0, 0, 2, 2, 1], "creek", wordlist))

print(get_entropy("weary", wordlist))