from nlpack import main as mn
from collections import Counter
import texttable as tt

tab = tt.Texttable()

def unigram(inp, dataset):
    inp = mn.spilt_word(inp)
    split = mn.split_uni(dataset)
    uni = Counter(split)
    prob = 1.0
    dataShow = [[]]
    nWords = len(uni)
    for i in range(1,len(inp)):
        dataShow.append([inp[i], uni[inp[i]], nWords, uni[inp[i]] / nWords])
        prob = prob * uni[inp[i]] / nWords
        # prob = prob * ()
    tab.add_rows(dataShow)
    tab.set_cols_align(['r','r','r','r'])
    tab.header(['wi','C(wi)','#words','P(wi)'])
    print(tab.draw())
    print("probability Unigrams :   ", prob)
    print("Perplexity           :   ", mn.perplex_uni(inp, uni))

def bigram(inp,dataset) :
    inp = mn.spilt_word(inp)
    data = [[]]
    prob = 1
    perplex = 1

    for i in range(len(inp)-1) :
        x = dataset.count(inp[i]+' '+inp[i+1])
        y = dataset.count(inp[i])
        z = x/y
        data.append([inp[i],inp[i+1],x, y ,z])
        prob = prob * z
        # perplex = perplex * (1/z) #aktifkan kalo smoothing udah bisa

    tab.add_rows(data)
    tab.set_cols_align(['r','r','r','r','r'])
    tab.header(['wi','wi+1','Ci,i+1','C(i)','P(wi+1|wi)'])
    print(tab.draw())
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