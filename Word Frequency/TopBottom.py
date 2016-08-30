import re
from collections import Counter

file = open('wikipedia2text-extracted.txt','r', encoding="utf8")

words = re.findall(r'\w+', file.read(100000))

res = Counter(words)

res = res.most_common()

print('Top 10')
for i in range(0,10,1):
	print(res[i])

print('')

print('Bottom 10')
for i in range(1,11,1):
	print(res[-i])