from nlpack import main as mn
from collections import Counter
import texttable as tt
from tabulate import tabulate

tab = tt.Texttable()

def unigram(inp, dataset):
    inp = mn.spilt_word(inp)
    split = mn.split_uni(dataset)
    token = len(split)
    uni = Counter(split)
    prob = 1.0
    dataShow = []
    perplex = 1.0
    nWords = len(uni)
    for i in range(1,len(inp)):
        z = (uni[inp[i]]+1) / (token+nWords)
        dataShow.append([inp[i], uni[inp[i]], token, z])
        prob = prob * z
        perplex = perplex * (1/z)

    print(tabulate(dataShow, headers=['wi','C(wi)','#words','P(wi)'],tablefmt="grid"))
    tab.header(['wi','C(wi)','#words','P(wi)'])
    print("probability Unigrams :   ", prob)
    print("Perplexity           :   ",pow(perplex,1/len(inp)))

def bigram(inp,dataset) :
    inp = mn.spilt_word(inp)
    split = mn.split_uni(dataset)
    count = Counter(split)
    nDict = len(count)
    data = []
    prob = 1
    perplex = 1
    for i in range(len(inp)-1) :
        x = dataset.count(inp[i]+' '+inp[i+1])
        y = dataset.count(inp[i])
        z = (x+1)/(y+nDict)
        data.append([inp[i],inp[i+1],x, y ,z])
        prob = prob * z
        perplex = perplex * (1/z)
    print(tabulate(data, headers=['wi','wi+1','Ci,i+1','C(i)','P(wi+1|wi)'],tablefmt="grid"))
    print("probability Unigrams :   ", prob)
    print("Perplexity           :   ", pow(perplex,1/len(inp)))


dataset = open('data/trained.txt', 'r', encoding="utf8").read()

print("1.Unigram")
print("2.Bigram")
sel = input('Pilih : ')

if (sel == '1'):
    inp = input('Masukkan kalimat : ')
    unigram(inp, dataset)
elif (sel == '2'):
    inp = input('Masukkan kalimat : ')
    bigram(inp, dataset)
else:
    print("error")