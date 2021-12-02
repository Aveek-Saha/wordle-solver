import json
import csv
import math
import os
import re

from itertools import product

from tqdm import tqdm

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

def get_entropy(word, wordlist, combs, total_words):
    entropy = 0
    for comb in combs:
        poss = len(filter_words(list(comb), word, wordlist))
        prob = poss/total_words
        if prob != 0:
            entropy += prob * math.log(1/prob, 2)

    return entropy

def calculate_score(entropy, freq):
    return (0.5 * entropy) + (0.5* freq)

# combs = list(product([0, 1, 2], repeat=5))

# with open(os.path.join('datasets', 'scaled', 'valid_word_scores_scaled_tf.json'), "r") as file:
#     data = json.load(file)
#     wordlist = {}
#     for word in data:
#         wordlist[word] = word

# TOTAL_WORDS = len(list(wordlist.keys()))

# entropy_list = {}
# for word in tqdm(wordlist):
#     entropy = get_entropy(word, wordlist, combs)
#     entropy_list[word] = entropy

# sorted_entropy = dict(sorted(entropy_list.items(), key=lambda item: item[1], reverse=True))

# with open(os.path.join('datasets', 'valid_words_entropy.json'), "w") as outfile:
#     json.dump(sorted_entropy, outfile, indent=4)

# with open(os.path.join('datasets', 'valid_words_entropy.json'), "r") as file:
#     sorted_entropy = json.load(file)

# a = list(sorted_entropy.values())
# amin, amax = min(a), max(a)
# for word in sorted_entropy:
#     sorted_entropy[word] = ((sorted_entropy[word]-amin) / (amax-amin))

# first_guess = {}
# for word in tqdm(wordlist):
#     first_guess[word] = calculate_score(sorted_entropy[word], data[word])

# sorted_first_guess = dict(sorted(first_guess.items(), key=lambda item: item[1], reverse=True))

# with open(os.path.join('datasets', 'scaled', 'first_guess_scores_scaled_tf.json'), "w") as outfile:
#     json.dump(sorted_first_guess, outfile, indent=4)

# with open(os.path.join('datasets', 'scaled', 'first_guess_scores_scaled_tf.json'), "r") as file:
#     first_guess_list = json.load(file)

# first_guess = list(first_guess_list.keys())[0]
# second_guess = {}
# for comb in tqdm(combs):
#     comb_name = "".join([str(int) for int in list(comb)])
#     second_guess[comb_name] = []
#     second_word_list = filter_words(list(comb), first_guess, wordlist)
#     for word in tqdm(second_word_list):
#         entropy = get_entropy(word, second_word_list, combs)
#         second_guess[comb_name].append({
#                 "word": word,
#                 "score": calculate_score(entropy, data[word])
#             })

# with open(os.path.join('datasets', 'scaled', 'second_guess_scores_scaled_tf.json'), "w") as outfile:
#     json.dump(second_guess, outfile, indent=4)