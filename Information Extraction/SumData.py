import re

file = tuple(open('Whatford vs Arsenal.txt','r'))

recaps = []
teams = []
events = []

def addteam(team):
    if not(team in teams):
        teams.append(team)

def addevent(event):
    if not(event in events):
        events.append(event)

for data in file:
    Filt = re.match(r"(\d+)'([a-z]+\s*[a-z]*\s*[a-z]*)", data)

    if Filt:
        Filt = re.match(r"(\d+)'([a-z]+\s*[a-z]*\s*[a-z]*).*\((\w+)\)(.*)", data)

        if Filt:
            addteam(Filt.group(3))
            addevent(Filt.group(2))
            recaps.append([Filt.group(3), Filt.group(2)])
        else:
            Filt = re.match(r"(\d+)'([a-z]+\s*[a-z]*\s*[a-z]*).*,\s([A-Z]\w+)", data)
            if Filt:
                addteam(Filt.group(3))
                addevent(Filt.group(2))
                recaps.append([Filt.group(3), Filt.group(2)])

    else:
        Filt = re.match(r"(\d+)'\+\d'([a-z]+\s*[a-z]*\s*[a-z]*)", data)
        if Filt:
            Filt = re.match(r"(\d+)'\+\d'([a-z]+\s*[a-z]*\s*[a-z]*).*\((\w+)\)(.*)", data)

            if Filt:
                addteam(Filt.group(3))
                addevent(Filt.group(2))
                recaps.append([Filt.group(3), Filt.group(2)])
            else:
                Filt = re.match(r"(\d+)'([a-z]+\s*[a-z]*\s*[a-z]*).*,\s([A-Z]\w+)", data)
                if Filt:
                    addteam(Filt.group(3))
                    addevent(Filt.group(2))
                    recaps.append([Filt.group(3), Filt.group(2)])

for team in teams:
    print('--------',team,'--------')
    for event in events:
        print(event,':',recaps.count([team,event]))