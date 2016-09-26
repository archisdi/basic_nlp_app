import re

class cleaning:
    def parenth(data):
        new_data = re.sub(r'\([^)]*\)', '', data)
        return new_data

    def meta(data):
        new_data = re.sub(r'<[^>]*>', '', data)
        return new_data

    def punc(data):
        new_data = re.sub(r'[^\w\s\.]', '', data)
        return new_data

    def whitesp(data):
        new_data = re.sub('\s+', ' ', data)
        return new_data

    def digit(data):
        new_data = re.sub('\d+', '', data)
        return new_data


class normalization:
    def split_paragraph(data):
        new_data = []
        splited = re.split("\.\s", data)

        for par in splited:
            par = par.lower()
            if (par != ''):
                new_data.append("<s> " + par + " </s>")

        return new_data

class main:
    def spilt_word(self):
        return self.split()

    def split_uni(self):
        return re.split('\s',self)

    def split_bi(self):
        return re.findall(r'\w+\s\w+', self)

    def perplex_uni(inp,unigram):
        perplexity = 1
        N = 0

        for word in inp:
            if word in unigram:
                N += 1
                perplexity = perplexity * (1 / unigram[word])
        perplexity = pow(perplexity, 1 / float(N))

        return perplexity