import csv
import json
import os

import numpy as np

from clean_wordlist import *
from generate_entropy import *
from simulation import *

DATASET_DIR = 'datasets'
WORDS_DIR = 'words'

EXPERIMENT_DIR = 'combfreq'

WORDLIST_ALL = os.path.join(DATASET_DIR, WORDS_DIR, 'wordlist_all.txt')
WORDLIST_ALL_UNI = os.path.join(DATASET_DIR, WORDS_DIR, 'unigram_freq.csv')
VALID_WORDS = os.path.join(DATASET_DIR, WORDS_DIR, 'valid_guesses.txt')
ANSWERS = os.path.join(DATASET_DIR, WORDS_DIR, 'possible_answers.txt')
GUESS_MATRIX = os.path.join(DATASET_DIR, 'match_matrix.npy')
VALID_WORDS_SCORE = os.path.join(DATASET_DIR, EXPERIMENT_DIR, 'valid_word_scores_scaled_tf.json')
VALID_WORDS_ENTROPY = os.path.join(DATASET_DIR, 'valid_words_entropy_map.json')
FIRST_GUESS_SCORES = os.path.join(DATASET_DIR, EXPERIMENT_DIR, 'first_guess_scores_scaled_tf.json')
SECOND_GUESS_SCORES = os.path.join(DATASET_DIR, EXPERIMENT_DIR, 'second_guess_scores_scaled_tf.json')
RESULTS = os.path.join(DATASET_DIR, EXPERIMENT_DIR, 'simulation_results_scaled_tf.json')
RESULTS_EXTENDED = os.path.join(DATASET_DIR, EXPERIMENT_DIR, 'simulation_results_scaled_tf.json')

# TOTAL_WORDS = 3000000
TOTAL_WORDS = 0
TOTAL_ARTICLES = 6000000

combs = list(product([0, 1, 2], repeat=5))

outcomes = {
    2: "🟩",
    1: "🟨",
    0: "⬛"
}

with open(WORDLIST_ALL, 'r', encoding='utf8') as f:
        wordlist = {}
        for row in csv.reader(f, delimiter=' '):
            wordlist[row[0]] = [int(row[2]), int(row[3])]
            TOTAL_WORDS += int(row[2])

with open(WORDLIST_ALL_UNI, 'r', encoding='utf8') as f:
        wordlist_uni = {}
        for row in csv.reader(f, delimiter=','):
            if len(row[0]) == 5:
                wordlist_uni[row[0]] = int(row[1])
                TOTAL_WORDS += int(row[1])

with open(VALID_WORDS, 'r', encoding='utf8') as f:
        valid = [row for row in csv.reader(f, delimiter=',')][0]

# with open(VALID_WORDS_ENTROPY, "r") as file:
#         sorted_entropy = json.load(file)

# # match_matrix = np.load(GUESS_MATRIX)

# with open(FIRST_GUESS_SCORES, "r") as file:
#         first_guess_list = json.load(file)

print("Calculate term frequency")
# data = clean_wordlist(wordlist, valid, TOTAL_WORDS, TOTAL_ARTICLES)
# data_uni = clean_wordlist_alt(wordlist_uni, valid, TOTAL_WORDS)

# for word in data:
#     data[word] = (data[word] + data_uni[word])/2

# data = dict(sorted(data.items(), key=lambda item: item[1], reverse=True))

# with open(VALID_WORDS_SCORE, "w") as outfile:
#         json.dump(data, outfile, indent=4)

with open(VALID_WORDS_SCORE, "r") as file:
    data = json.load(file)
    wordlist = {}
    for word in data:
        wordlist[word] = word

print("Calculate entropy")
# sorted_entropy = generate_entropy_list(wordlist, combs, TOTAL_WORDS)
# with open(VALID_WORDS_ENTROPY, "w") as outfile:
#         json.dump(sorted_entropy, outfile, indent=4)

with open(VALID_WORDS_ENTROPY, "r") as file:
    sorted_entropy = json.load(file)

with open(VALID_WORDS_SCORE, "r") as file:
    data = json.load(file)

print("Scale and sort first guess scores")
# sorted_first_guess = generate_first_guess_score(wordlist, data, sorted_entropy)
# with open(FIRST_GUESS_SCORES, "w") as outfile:
#         json.dump(sorted_first_guess, outfile, indent=4)

with open(FIRST_GUESS_SCORES, "r") as file:
    sorted_first_guess = json.load(file)

first_guess = list(sorted_first_guess.keys())[1]
print("Calculate second guess scores for all combs")
second_guess = generate_second_guess_score(wordlist, data, first_guess, combs, TOTAL_WORDS)
with open(SECOND_GUESS_SCORES, "w") as outfile:
        json.dump(second_guess, outfile, indent=4)

# with open(SECOND_GUESS_SCORES, "r") as file:
#     second_guess = json.load(file)

# with open(ANSWERS, 'r', encoding='utf8') as f:
#     answer_words = [row for row in csv.reader(f, delimiter=',')][0]

# print("Run Simulation")
# record = run_simulation(outcomes, wordlist, answer_words, sorted_first_guess, second_guess, TOTAL_WORDS, combs, data, False)
# with open(RESULTS_EXTENDED, "w", encoding='utf8') as outfile:
#         json.dump(record, outfile, indent=4, ensure_ascii=False)

# print("Average Score in successful games: ", record["stats"]['average'])
# print("Number of failed games: ", record["stats"]['failed'])