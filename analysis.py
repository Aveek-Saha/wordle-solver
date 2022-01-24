import matplotlib.pyplot as plt
import json
import os
from collections import Counter

import pandas as pd

DATASET_DIR = 'datasets'
EXPERIMENT_DIR = 'combfreq'

RESULTS = os.path.join(DATASET_DIR, EXPERIMENT_DIR, 'simulation_results_scaled_tf.json')
RESULTS_EXTENDED = os.path.join(DATASET_DIR, EXPERIMENT_DIR, 'simulation_results_scaled_tf_extended.json')

with open(RESULTS, "r") as file:
    simulation_results = json.load(file)

results = simulation_results["games"]
scores = []

for result in results:
    scores.append(str(results[result]["score"]))

count = Counter(scores)
df = pd.DataFrame.from_dict(count, orient='index').sort_index(axis = 0)
print(df)
df.plot(xlabel='Scores', ylabel='Number of games', title='Score distribution', kind='bar')
# plt.show()
# plt.savefig(os.path.join('graphs', 'analysis_unlimited.png'))
plt.savefig(os.path.join('graphs', 'analysis.png'))
# print(df)