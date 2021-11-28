import matplotlib.pyplot as plt
import json
import os
from collections import Counter

import pandas as pd

with open(os.path.join('datasets', 'simulation_results_extended.json'), "r") as file:
    simulation_results = json.load(file)

results = simulation_results["games"]
scores = []

for result in results:
    scores.append(str(results[result]["score"]))

count = Counter(scores)
df = pd.DataFrame.from_dict(count, orient='index').sort_index(axis = 0)
df.plot(kind='bar')
plt.show()

# print(df)