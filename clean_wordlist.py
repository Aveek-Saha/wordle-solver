import math

from tqdm import tqdm

def inv_tfidf(word_freq, doc_freq, total_words, total_articles):
    tf = word_freq/total_words
    # idf = math.log((total_articles+1)/(doc_freq + 1))
    # tfidf = tf * idf
    return tf

def term_freq(word_freq, total_words):
    tf = word_freq/total_words
    return tf

def clean_wordlist(wordlist, valid, total_words, total_articles):
    possible_words = {}
    for word in tqdm(valid):
        if word in wordlist:
            possible_words[word] = inv_tfidf(wordlist[word][0], wordlist[word][1], total_words, total_articles)

        else:
            possible_words[word] = inv_tfidf(1, 1, total_words, total_articles)

    a = list(possible_words.values())
    amin, amax = min(a), max(a)
    for word in possible_words:
        possible_words[word] = ((possible_words[word]-amin) / (amax-amin))

    sorted_possible_words = dict(sorted(possible_words.items(), key=lambda item: item[1], reverse=True))

    return sorted_possible_words

import csv
import os
import json

TOTAL_WORDS = 0
TOTAL_ARTICLES = 6000000

DATASET_DIR = 'datasets'
WORDS_DIR = 'words'

EXPERIMENT_DIR = 'newfreq'
VALID_WORDS = os.path.join(DATASET_DIR, WORDS_DIR, 'valid_guesses.txt')
WORDLIST_ALL = os.path.join(DATASET_DIR, WORDS_DIR, 'unigram_freq.csv')
VALID_WORDS_SCORE = os.path.join(DATASET_DIR, EXPERIMENT_DIR, 'valid_word_scores_scaled_tf.json')

with open(VALID_WORDS, 'r', encoding='utf8') as f:
        valid = [row for row in csv.reader(f, delimiter=',')][0]

with open(WORDLIST_ALL, 'r', encoding='utf8') as f:
        wordlist = {}
        for row in csv.reader(f, delimiter=','):
            if len(row[0]) == 5:
                wordlist[row[0]] = int(row[1])
                TOTAL_WORDS += int(row[1])

possible_words = {}
for word in tqdm(valid):
    if word in wordlist:
        possible_words[word] = term_freq(wordlist[word], TOTAL_WORDS)

    else:
        print(word)
        possible_words[word] = term_freq(1, TOTAL_WORDS)


a = list(possible_words.values())
amin, amax = min(a), max(a)
for word in possible_words:
    possible_words[word] = ((possible_words[word]-amin) / (amax-amin))

sorted_possible_words = dict(sorted(possible_words.items(), key=lambda item: item[1], reverse=True))

with open(VALID_WORDS_SCORE, "w") as outfile:
    json.dump(sorted_possible_words, outfile, indent=4)
