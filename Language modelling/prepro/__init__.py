import re

class driver:
    def open(namaFile):
        file = open(namaFile, 'r', encoding="utf8")
        return (file.read()).lower()

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
            new_data.append("<s>" + par + "</s>")

        return new_data
