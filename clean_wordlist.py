import csv
import json
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

possible_words = {}
for word in valid:
    if word in wordlist:
        possible_words[word] = wordlist[word]

    else:
        possible_words[word] = "1"


with open(os.path.join('datasets', 'valid_word_freq.json'), "w") as outfile:
    json.dump(possible_words, outfile, indent=4)
