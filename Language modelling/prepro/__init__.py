import re

class cleaning:

    def parenth(data):
        new_data = re.sub(r'\(.*\)', '', data)
        return new_data

    def meta(data):
        new_data = re.sub(r'\<.*\>','',data)
        return new_data

    def punc(data):
        new_data = re.sub(r'[^\w\s\.]','',data)
        return new_data

    def whitesp(data):
        new_data =re.sub('\s+',' ',data)
        return new_data

    def digit(data):
        new_data = re.sub('\d+', '', data)
        return new_data

class normalization:

    def split_paragraph(data):
        new_data = []
        splited = re.split("\.\s*", data)

        for par in splited:
            par = par.lower()
            new_data.append("<s>" + par + "</s>")

        return new_data
