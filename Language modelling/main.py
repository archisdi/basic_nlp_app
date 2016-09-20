from prepro import normalization as norm
from prepro import  cleaning as cln

file_in   = open('dataset.txt', 'r', encoding="utf8")
file_out  = open('output.txt', 'w', encoding="utf8")

data_in = file_in.read()

new = (cln.whitesp(cln.punc(cln.digit(cln.parenth(cln.meta(data_in))))))

new2 = norm.split_paragraph(new)

for data2 in new2:
    file_out.write(data2 + "\n")
