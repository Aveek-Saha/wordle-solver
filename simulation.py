import random
import os
import csv
from itertools import product
from pytest import fail
from tqdm import tqdm
from operator import itemgetter

from generate_entropy import *
from wordle import *


def generate_guess(previous_board, previous_guess, wordlist, turn, total_words, combs, guess, second_guess_scores, data):
    if turn == 0:
        return guess, wordlist

    if turn == 1:
        board_name = "".join([str(int) for int in list(previous_board)])
        guess_list = second_guess_scores[board_name]
        filtered_words = {guess["word"]: guess["word"] for guess in guess_list}
        return max(guess_list, key=itemgetter('score'))["word"], filtered_words

    else:
        filtered_words = filter_words(previous_board, previous_guess, wordlist)
        next_guess = {}
        for word in filtered_words:
            entropy = get_entropy(word, filtered_words, combs, total_words)
            next_guess[word] = calculate_score(entropy, data[word])
        filtered_words = {word: word for word in filtered_words}
        sorted_next_guess = list(dict(
            sorted(next_guess.items(), key=lambda item: item[1], reverse=True)).keys())[0]
        return sorted_next_guess, filtered_words

def generate_guess_matrix(previous_board, previous_guess, turn, guesses, words_ordered, match_matrix, comb_map, total_words, guess, second_guess_scores, data):
    if turn == 0:
        return guess

    if turn == 1:
        board_name = "".join([str(int) for int in list(previous_board)])
        guess_list = second_guess_scores[board_name]
        return guess_list["word"]

    else:
        guess_index = words_ordered.index(previous_guess)
        guess_combs = match_matrix[guess_index]
        board_name = "".join([str(int) for int in list(previous_board)])
        comb_number = comb_map[board_name]
        indices = np.where(guess_combs == comb_number)
        # print(board_name, np.array(words)[indices])
        score_list = []
        if indices[0].size != 0:
            for i, row in enumerate(match_matrix[indices]):
                word_matches = row[indices]
                freq_map = dict(collections.Counter(word_matches))
                entropy = get_entropy_from_map(freq_map, total_words)
                score_list.append({
                    "word": words_ordered[int(indices[0][i])],
                    "score": calculate_score(entropy, data[words_ordered[int(indices[0][i])]])
                })
            sorted_guess = sorted(score_list, reverse=True, key=lambda d: d['score'])
            for i in range(len(score_list)):
                final_guess = sorted_guess[i]['word']
                if final_guess not in guesses:
                    break
            return final_guess

# word = random.choice(words)

# board = [0, 0, 0, 0, 0]
# print("Answer: ", word)

# guess = list(first_guess_list.keys())[0]

# for turn in range(6):

#     previous_guess = guess
#     guess = generate_guess(board, previous_guess, wordlist, turn)
#     print(guess)


#     board = check_guess(word, guess)
#     print_board(board, outcomes)
#     if board == [2, 2, 2, 2, 2]:
#         print("Completed in ", turn + 1,"/ 6")
#         break


def run_simulation(outcomes, wordlist, words, first_guess_list, second_guess_scores, total_words, combs, data):

    # comb_map = {"".join([str(int) for int in list(comb)]): i for i, comb in enumerate(combs)}
    # match_matrix = np.load(os.path.join('datasets', 'match_matrix.npy'))
    # words_ordered = [word for word in wordlist]
    # words_ordered.sort()

    score_total = 0
    failed_games = 0
    total_games = len(words)
    # total_games = 10
    record = {}
    record["games"] = {}
    index = 0
    for word in tqdm(words):
        index += 1
        board = [0, 0, 0, 0, 0]
        guess = list(first_guess_list.keys())[0]
        score = 1
        filtered_wordlist = wordlist
        game = {}
        game["answer"] = word
        game["guesses"] = []
        game["share"] = "Wordle " + str(index) + " {}/6\n\n"
        boards = ""

        for turn in range(6):
            previous_guess = guess
            guess, filtered_wordlist = generate_guess(
                board, previous_guess, filtered_wordlist, turn, total_words, combs, guess, second_guess_scores, data)
            board = check_guess(word, guess)
            game["guesses"].append(guess)
            boards += print_board(board, outcomes)+"\n"

            if board == [2, 2, 2, 2, 2]:
                break
            score += 1
            if turn == 5:
                score = 0

        if score == 0:
            failed_games += 1
            game["share"] = game["share"].format("X")
            game["score"] = "X"
        else:
            game["share"] = game["share"].format(score)
            game["score"] = score

        game["share"] +=  boards
        record["games"][index] = game
        score_total += score

    record["stats"] = {
        "total": total_games,
        "failed": failed_games,
        "average": score_total/(total_games-failed_games)
    }

    return record
