import csv
with open ('wordlist.txt', 'r', encoding='utf8') as f:
    wordlist = [[row[0], row[2], row[3]] for row in csv.reader(f,delimiter=' ')]
    print (wordlist)