import enum
import json
import csv
import math
import os
import re
import csv

from itertools import product
import collections

from tqdm import tqdm
import numpy as np
from wordle import *

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

    wordlist = {word: wordlist[word] for word in wordlist if check_guess(word, guess) == board}
    return wordlist

def get_entropy(word, wordlist, combs, total_words):
    entropy = 0
    for comb in combs:
        poss = len(filter_words(list(comb), word, wordlist))
        prob = poss/total_words
        if prob != 0:
            entropy += prob * math.log(1/prob, 2)

    return entropy

def get_entropy_from_map(freq_map, total_words):
    entropy = 0
    for comb in freq_map:
        prob = freq_map[comb]/total_words
        if prob != 0:
            entropy += prob * math.log(1/prob, 2)

    return entropy

def calculate_score(entropy, freq):
    return (0.7 * entropy) + (0.3* freq)

# combs = list(product([0, 1, 2], repeat=5))

# with open(os.path.join('datasets', 'scaled', 'valid_word_scores_scaled_tf.json'), "r") as file:
#     data = json.load(file)
#     wordlist = {}
#     for word in data:
#         wordlist[word] = word

# TOTAL_WORDS = len(list(wordlist.keys()))

# comb_map = {"".join([str(int) for int in list(comb)]): i for i, comb in enumerate(combs)}
# words = [word for word in wordlist]
# words.sort()
# words_comb_map = {"wordlist": words, "combs": comb_map}

# with open(os.path.join('datasets', 'board_combs.json'), "w") as outfile:
#     json.dump(words_comb_map, outfile, indent=4)

# match_matrix = np.zeros((len(words), len(words)), dtype=np.uint8)
# for i, guess in enumerate(tqdm(words)):
#     for j, word in enumerate(words):
#         match_matrix[i][j] = comb_map["".join([str(int) for int in list(check_guess(word, guess))])]

# np.save(os.path.join('datasets', 'match_matrix.npy'), match_matrix)

# with open(os.path.join('datasets', 'valid_words_filter.csv'), "w", newline='') as outfile:
#     wr = csv.writer(outfile)
#     for guess in tqdm(words):
#         guess_boards = []
#         for word in wordlist:
#             guess_boards.append(comb_map["".join([str(int) for int in list(check_guess(word, guess))])])

#         wr.writerow(guess_boards)

# with open(os.path.join('datasets', 'valid_words_filter.csv'), "r") as file:
#     wordlist_map = list(csv.reader(file))

# match_matrix = np.load(os.path.join('datasets', 'match_matrix.npy'))

# print(filter_words([0, 0, 0, 1, 0], 'state', wordlist).keys())
# print(get_entropy("mahwa", wordlist, combs, TOTAL_WORDS))

# entropy_list = {}
# for i, word in enumerate(tqdm(words)):
#     # entropy = get_entropy(word, wordlist, combs)
#     freq_map = dict(collections.Counter(match_matrix[i]))
#     entropy = get_entropy_from_map(freq_map, TOTAL_WORDS)
#     entropy_list[word] = entropy

# entropy_list = {}
# for word in tqdm(wordlist):
#     entropy = get_entropy(word, wordlist, combs, TOTAL_WORDS)
#     entropy_list[word] = entropy

# sorted_entropy = dict(sorted(entropy_list.items(), key=lambda item: item[1], reverse=True))

# with open(os.path.join('datasets', 'filtered', 'valid_words_entropy_map.json'), "w") as outfile:
#     json.dump(sorted_entropy, outfile, indent=4)

# with open(os.path.join('datasets', 'filtered', 'valid_words_entropy_map.json'), "r") as file:
#     sorted_entropy = json.load(file)

# a = list(sorted_entropy.values())
# amin, amax = min(a), max(a)
# for word in sorted_entropy:
#     sorted_entropy[word] = ((sorted_entropy[word]-amin) / (amax-amin))

# first_guess = {}
# for word in tqdm(words):
#     first_guess[word] = calculate_score(sorted_entropy[word], data[word])

# sorted_first_guess = dict(sorted(first_guess.items(), key=lambda item: item[1], reverse=True))

# with open(os.path.join('datasets', 'filtered', 'first_guess_scores_scaled_tf.json'), "w") as outfile:
#     json.dump(sorted_first_guess, outfile, indent=4)

# with open(os.path.join('datasets', 'filtered', 'first_guess_scores_scaled_tf.json'), "r") as file:
#     first_guess_list = json.load(file)

# first_guess = list(first_guess_list.keys())[0]
# first_guess_index = words.index(first_guess)
# first_guess_combs = match_matrix[first_guess_index]
# second_guess = {}

# for comb in tqdm(comb_map):
#     comb_number = comb_map[comb]
#     indices = np.where(first_guess_combs == comb_number)
#     # print(comb, np.array(words)[indices])
#     score_list = []
#     if indices[0].size != 0:
#         for i, row in enumerate(match_matrix[indices]):
#             word_matches = row[indices]
#             freq_map = dict(collections.Counter(word_matches))
#             entropy = get_entropy_from_map(freq_map, TOTAL_WORDS)
#             score_list.append({
#                 "word": words[int(indices[0][i])],
#                 "index": int(indices[0][i]),
#                 "score": calculate_score(entropy, data[words[int(indices[0][i])]])
#             })
#         second_guess[comb] = sorted(score_list, reverse=True, key=lambda d: d['score'])[0]


# first_guess = list(first_guess_list.keys())[0]
# second_guess = {}
# for comb in tqdm(combs):
#     comb_name = "".join([str(int) for int in list(comb)])
#     second_guess[comb_name] = []
#     second_word_list = filter_words(list(comb), first_guess, wordlist)
#     for word in tqdm(second_word_list):
#         entropy = get_entropy(word, second_word_list, combs, TOTAL_WORDS)
#         second_guess[comb_name].append({
#                 "word": word,
#                 "score": calculate_score(entropy, data[word])
#             })

# with open(os.path.join('datasets', 'filtered', 'second_guess_scores_scaled_tf.json'), "w") as outfile:
#     json.dump(second_guess, outfile, indent=4)