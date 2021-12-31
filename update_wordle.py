import re
import os
import json

DATASET_DIR = 'datasets'
EXPERIMENT_DIR = 'filtered'

# with open('README.md', 'r', encoding='utf8') as f:
#     text = f.read()

# match = re.search(r'## Today\'s Wordle(.*?)<details>', text, re.DOTALL).group(1)
# print(match)

RESULTS = os.path.join(DATASET_DIR, EXPERIMENT_DIR, 'simulation_results_scaled_tf.json')

with open(RESULTS, "r", encoding='utf8') as file:
    res = json.load(file)

day = "261"

current_answer = res["games"][day]

sol = current_answer["share"].split("\n\n")

print(sol[0] + "\n\n" + " <br>\n".join(sol[1].split("\n")))