import math

from tqdm import tqdm

def inv_tfidf(word_freq, doc_freq, total_words, total_articles):
    tf = word_freq/total_words
    idf = math.log((total_articles+1)/(doc_freq + 1))
    tfidf = tf * idf
    return tfidf

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

