import csv
from turtle import pos
with open ('wordlist_all.txt', 'r', encoding='utf8') as f:
    # wordlist = [[row[0], row[2]] for row in csv.reader(f,delimiter=' ')]
    wordlist = [row[0] for row in csv.reader(f,delimiter=' ')]
    # print (wordlist)

with open ('possible_answers.txt', 'r', encoding='utf8') as f:
    possible = [row for row in csv.reader(f,delimiter=',')][0]

    print(len(possible))

for word in possible:
    if word not in wordlist:
        print(word)
        break