from prepro import normalization as norm
from prepro import  cleaning as cln
from prepro import driver as drv

file_in   = drv.open('test.txt')
file_out  = open('output.txt', 'w', encoding="utf8")

data_in = file_in

new = (cln.whitesp(cln.punc(cln.digit(cln.parenth(cln.meta(data_in))))))

new2 = norm.split_paragraph(new)

for data2 in new2:
    file_out.write(data2 + "\n")
