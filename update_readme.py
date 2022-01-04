import re
import os
import json
from datetime import datetime

DATASET_DIR = 'datasets'
EXPERIMENT_DIR = 'filtered'

today = datetime.now()
start = datetime(2021, 6, 19)
delta = today - start
day = str(delta.days)

with open('README.md', 'r', encoding='utf8') as f:
    text = f.read()

# match = re.search(r'## Today\'s Wordle(.*?)<details>', text, re.DOTALL).group(1)
# match = re.search(r'</summary>(.*?)</pre>', text, re.DOTALL).group(1)

# print(match)

RESULTS = os.path.join(DATASET_DIR, EXPERIMENT_DIR,
                       'simulation_results_scaled_tf.json')

with open(RESULTS, "r", encoding='utf8') as file:
    res = json.load(file)

current_answer = res["games"][day]

board = current_answer["share"].split("\n\n")

share_board = "## Today's Wordle\n\n" + \
    board[0] + "\n\n" + " <br>\n".join(board[1].split("\n")) + "\n<details>"
guesses = "</summary>\n\nAnswer: `" + current_answer["answer"].upper(
) + "`\n<pre>\n" + "\n".join(current_answer["guesses"]).upper() + "\n</pre>\n"

sub_board = re.sub(r'## Today\'s Wordle(.*?)<details>',
                   share_board, text, count=1, flags=re.DOTALL)
sub_answer = re.sub(r'</summary>(.*?)</pre>', guesses,
                    sub_board, count=1, flags=re.DOTALL)

with open('README.md', 'w', encoding='utf8') as f:
    f.write(sub_answer)
