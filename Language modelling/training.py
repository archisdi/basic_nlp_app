from nlpack import normalization as norm
from nlpack import  cleaning as cln

file_in   = open('data/dataset.txt', 'r', encoding="utf8")
file_out1  = open('data/trained.txt', 'w', encoding="utf8")
file_out2  = open('data/testing.txt', 'w', encoding="utf8")

data_in = file_in.read()

new = (cln.whitesp(cln.punc(cln.digit(cln.parenth(cln.meta(data_in))))))

new2 = norm.split_paragraph(new)

for i in range(0,len(new2)-10) :
    file_out1.write(new2[i] + "\n")

for i in range(len(new2)-20,len(new2)) :
    file_out2.write(new2[i] + "\n")
