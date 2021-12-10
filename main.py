import csv
import json
import os

import numpy as np

from clean_wordlist import *

DATASET_DIR = 'datasets'
WORDS_DIR = 'words'

WORDLIST_ALL = os.path.join(DATASET_DIR, WORDS_DIR, 'wordlist_all.txt')
VALID_WORDS = os.path.join(DATASET_DIR, WORDS_DIR, 'valid_guesses.txt')
VALID_WORDS_SCORE = os.path.join(DATASET_DIR, 'scaled', 'valid_word_scores_scaled_tf.json')
VALID_WORDS_ENTROPY = os.path.join(DATASET_DIR, 'filtered', 'valid_words_entropy_map.json')
FIRST_GUESS_SCORES = os.path.join(DATASET_DIR, 'filtered', 'first_guess_scores_scaled_tf.json')
SECOND_GUESS_SCORES = os.path.join(DATASET_DIR, 'filtered', 'second_guess_scores_scaled_tf.json')
GUESS_MATRIX = os.path.join(DATASET_DIR, 'match_matrix.npy')
ANSWERS = os.path.join(DATASET_DIR, WORDS_DIR, 'possible_answers.txt')
RESULTS = os.path.join(DATASET_DIR, 'filtered', 'simulation_results_scaled_tf.json')

# TOTAL_WORDS = 3000000
TOTAL_WORDS = 0
TOTAL_ARTICLES = 6000000

with open(WORDLIST_ALL, 'r', encoding='utf8') as f:
        wordlist = {}
        for row in csv.reader(f, delimiter=' '):
            wordlist[row[0]] = [int(row[2]), int(row[3])]
            TOTAL_WORDS += int(row[2])

with open(VALID_WORDS, 'r', encoding='utf8') as f:
        valid = [row for row in csv.reader(f, delimiter=',')][0]

# with open(VALID_WORDS_ENTROPY, "r") as file:
#         sorted_entropy = json.load(file)

# # match_matrix = np.load(GUESS_MATRIX)

# with open(FIRST_GUESS_SCORES, "r") as file:
#         first_guess_list = json.load(file)

print("Calculate term frequency")
sorted_possible_words = clean_wordlist(wordlist, valid, TOTAL_WORDS)

with open(VALID_WORDS_SCORE, "w") as outfile:
        json.dump(sorted_possible_words, outfile, indent=4)