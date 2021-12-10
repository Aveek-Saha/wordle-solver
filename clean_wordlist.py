import math

from tqdm import tqdm

def inv_tfidf(word_freq, doc_freq, total_words):
    tf = word_freq/total_words

    # idf = math.log((TOTAL_ARTICLES+1)/(doc_freq + 1))

    # tfidf = tf * idf

    return tf

def clean_wordlist(wordlist, valid, total_words):
    possible_words = {}
    for word in tqdm(valid):
        if word in wordlist:
            possible_words[word] = inv_tfidf(wordlist[word][0], wordlist[word][1], total_words)

        else:
            possible_words[word] = inv_tfidf(1, 1, total_words)

    a = list(possible_words.values())
    amin, amax = min(a), max(a)
    for word in possible_words:
        possible_words[word] = ((possible_words[word]-amin) / (amax-amin))

    sorted_possible_words = dict(sorted(possible_words.items(), key=lambda item: item[1], reverse=True))

    return sorted_possible_words

