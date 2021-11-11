import csv
import json
import math
import os

with open(os.path.join('datasets', 'wordlist_all.txt'), 'r', encoding='utf8') as f:
    # wordlist = [[row[0], row[2]] for row in csv.reader(f,delimiter=' ')]
    wordlist = {}
    for row in csv.reader(f, delimiter=' '):
        wordlist[row[0]] = row[2]

    # print (wordlist)

with open(os.path.join('datasets', 'valid_guesses.txt'), 'r', encoding='utf8') as f:
    valid = [row for row in csv.reader(f, delimiter=',')][0]

    print(len(valid))

# possible_words = {}
# for word in valid:
#     if word in wordlist:
#         possible_words[word] = wordlist[word]

#     else:
#         possible_words[word] = "1"


# with open(os.path.join('datasets', 'valid_word_freq.json'), "w") as outfile:
#     json.dump(possible_words, outfile, indent=4)


TOTAL_WORDS = 3000000
TOTAL_ARTICLES = 6000000

def inv_tfidf(word_freq, doc_freq):
    tf = word_freq/TOTAL_WORDS

    idf = math.log(TOTAL_ARTICLES/(doc_freq + 1))

    tfidf = tf * idf

    return tfidf

print(inv_tfidf(1, 1))
print(inv_tfidf(6296, 5009))
print(inv_tfidf(1220752, 890394))
