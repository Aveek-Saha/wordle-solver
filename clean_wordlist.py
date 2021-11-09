import csv
import os

with open (os.path.join('datasets', 'wordlist_all.txt'), 'r', encoding='utf8') as f:
    # wordlist = [[row[0], row[2]] for row in csv.reader(f,delimiter=' ')]
    wordlist = [row[0] for row in csv.reader(f,delimiter=' ')]
    # print (wordlist)

with open (os.path.join('datasets', 'valid_guesses.txt'), 'r', encoding='utf8') as f:
    valid = [row for row in csv.reader(f,delimiter=',')][0]

    print(len(valid))

print(len(list(set(wordlist).intersection(set(valid)))))