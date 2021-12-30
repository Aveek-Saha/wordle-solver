import re

with open('README.md', 'r', encoding='utf8') as f:
    text = f.read()

match = re.search(r'## Today\'s Wordle(.*?)# Rules', text, re.DOTALL).group(1)
print(match)