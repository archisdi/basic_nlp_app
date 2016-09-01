import re

file = tuple(open('ManchesterVsWestham.txt','r'))

events = []

for data in file:
    Filt = re.match(r"(\d+)'([a-z]+\s*[a-z]*\s*[a-z]*)", data)

    if Filt:
        Filt = re.match(r"(\d+)'([a-z]+\s*[a-z]*\s*[a-z]*).*\((\w+)\)(.*)", data)

        if Filt:
            print(Filt.group(2),'by',Filt.group(3),'on minutes',Filt.group(1))
        else:
            Filt = re.match(r"(\d+)'([a-z]+\s*[a-z]*\s*[a-z]*).*\s([A-Z]\w+)", data)
            if Filt:
                print(Filt.group(2), 'by', Filt.group(3),'on minutes',Filt.group(1))
            else:
                print('x')

    else:
        Filt = re.match(r"(\d+)'\+\d'([a-z]+\s*[a-z]*\s*[a-z]*)", data)
        if Filt:
            Filt = re.match(r"(\d+)'\+\d'([a-z]+\s*[a-z]*\s*[a-z]*).*\((\w+)\)(.*)", data)

            if Filt:
                print(Filt.group(2), 'by', Filt.group(3), 'on minutes', Filt.group(1))
            else:
                Filt = re.match(r"(\d+)'([a-z]+\s*[a-z]*\s*[a-z]*).*\s([A-Z]\w+)", data)
                if Filt:
                    print(Filt.group(2), 'by', Filt.group(3), 'on minutes', Filt.group(1))
                else:
                    print('x')
        else:
            print('x')
