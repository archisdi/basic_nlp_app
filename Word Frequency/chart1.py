import re
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np

file = open('wikipedia2text-extracted.txt','r', encoding="utf8")

words = re.findall(r'\w+', file.read(10000))

res = Counter(words)

res = res.most_common()

y = np.arange(len(res))
performance = []

for data in res:
    performance.append(data[1])

plt.plot(y,performance)
plt.ylabel('Frekuensi')
plt.title('Indeks Kata')

plt.show()