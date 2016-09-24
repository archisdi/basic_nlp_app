from nlpack import main as mn
from collections import Counter


def unigram(inp, dataset):
    inp = mn.spilt_word(inp)
    split = mn.split_uni(dataset)
    uni = Counter(split)
    prob = 1.0

    nWords = len(uni)
    print("==================================================")
    print("wi \t\t C(wi) \t #words \t P(wi)")
    print("==================================================")

    for data in inp:
        print(data, '\t', uni[data], '\t', nWords, '\t', uni[data] / nWords)
        prob = prob * uni[data] / nWords

    print("==================================================")
    print("probability Unigrams :   ", prob)
    print("Perplexity           :   ", mn.perplex_uni(inp, uni))


dataset = open('data/trained.txt', 'r', encoding="utf8").read()

print("1.Unigram")
print("2.Bigram")
sel = input('Pilih : ')

if (sel == '1'):
    inp = input('Masukkan kalimat : ')
    unigram(inp, dataset)
elif (sel == '2'):
    print("underconstruction")
else:
    print("error")