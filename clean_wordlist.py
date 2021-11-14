import csv
import json
import math
import os

TOTAL_WORDS = 3000000
TOTAL_ARTICLES = 6000000

def inv_tfidf(word_freq, doc_freq):
    tf = word_freq/TOTAL_WORDS

    idf = math.log(TOTAL_ARTICLES/(doc_freq + 1))

    tfidf = tf * idf

    return tfidf

with open(os.path.join('datasets', 'wordlist_all.txt'), 'r', encoding='utf8') as f:
    # wordlist = [[row[0], row[2]] for row in csv.reader(f,delimiter=' ')]
    wordlist = {}
    for row in csv.reader(f, delimiter=' '):
        wordlist[row[0]] = [int(row[2]), int(row[3])]

    # print (wordlist)

with open(os.path.join('datasets', 'valid_guesses.txt'), 'r', encoding='utf8') as f:
    valid = [row for row in csv.reader(f, delimiter=',')][0]

    print(len(valid))

possible_words = {}
for word in valid:
    if word in wordlist:
        possible_words[word] = inv_tfidf(wordlist[word][0], wordlist[word][1])

    else:
        possible_words[word] = inv_tfidf(1, 1)

sorted_possible_words = dict(sorted(possible_words.items(), key=lambda item: item[1], reverse=True))

with open(os.path.join('datasets', 'valid_word_scores.json'), "w") as outfile:
    json.dump(sorted_possible_words, outfile, indent=4)



# print(inv_tfidf(1, 1))
# print(inv_tfidf(6296, 5009))
# print(inv_tfidf(1220752, 890394))
