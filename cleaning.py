__author__ = 'Mufidah Aisyah'

import re

def openFileTXT(namaFile) :
     file = open(namaFile, 'r', encoding="utf8")
     return (file.read()).lower()

def cleaningScript(text) :
    regex = re.sub(r'<[^>]*>','',text)
    return regex

def cleaningPenjelasan(text) :
    regex = re.sub(r'\([^>]*\)','',text)
    return regex

def cleaningDigit(text) :
    regex = re.sub(r'\d.*\d*','',text)
    return regex

def cleaningPunctuation(text) :
    regex = re.sub(r'[?/=+-_#$@^&!,:;]','',text)
    return regex


#driver
# namaFile = 'wikipedia2text-extracted.txt'
# isiFile = openFileTXT(namaFile)
# print(isiFile)
text = 'lalalla <script>\ += <jsjdhjsdjsgdjshg=_hjdejdhjw-> -(jshdjsjdjsh) 123 12.3333 43.33'
print(cleaningScript(text))
print(cleaningPenjelasan(text))
print(cleaningDigit(text))
print(cleaningPunctuation(text))