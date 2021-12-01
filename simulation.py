import random
import os
import csv
from itertools import product
from pytest import fail
from tqdm import tqdm
from operator import itemgetter

from generate_entropy import *
from wordle import *


def generate_guess(previous_board, previous_guess, wordlist, turn):
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
            entropy = get_entropy(word, filtered_words, combs)
            next_guess[word] = entropy * data[word]
        filtered_words = {word: word for word in filtered_words}
        sorted_next_guess = list(dict(
            sorted(next_guess.items(), key=lambda item: item[1], reverse=True)).keys())[0]
        return sorted_next_guess, filtered_words


with open(os.path.join('datasets', 'words', 'possible_answers.txt'), 'r', encoding='utf8') as f:
    words = [row for row in csv.reader(f, delimiter=',')][0]

with open(os.path.join('datasets', 'freq', 'valid_word_scores_tf.json'), "r") as file:
    data = json.load(file)

with open(os.path.join('datasets', 'freq', 'first_guess_scores_tf.json'), "r") as file:
    first_guess_list = json.load(file)
    wordlist = {}
    for word in first_guess_list:
        wordlist[word] = word

with open(os.path.join('datasets', 'freq', 'second_guess_scores_tf.json'), "r") as file:
    second_guess_scores = json.load(file)

# word = random.choice(words)

outcomes = {
    2: "🟩",
    1: "🟨",
    0: "⬛"
}


# board = [0, 0, 0, 0, 0]
# print("Answer: ", word)
combs = list(product([0, 1, 2], repeat=5))

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

    for turn in range(20):
        previous_guess = guess
        guess, filtered_wordlist = generate_guess(
            board, previous_guess, filtered_wordlist, turn)
        board = check_guess(word, guess)
        game["guesses"].append(guess)
        boards += print_board(board, outcomes)+"\n"

        if board == [2, 2, 2, 2, 2]:
            break
        score += 1
        # if turn == 5:
        #     score = 0

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

with open(os.path.join('datasets', 'freq', 'simulation_results_tf.json'), "w", encoding='utf8') as outfile:
    json.dump(record, outfile, indent=4, ensure_ascii=False)

print("Average Score in successful games: ",
      score_total/(total_games-failed_games))
print("Number of failed games: ", failed_games)
