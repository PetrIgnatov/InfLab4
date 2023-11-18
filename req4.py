import re

class data:
    def __init__(self, name: str, val: str):
        self.name = name
        self.val = val
class lesson:
    def __init__(self):
        self.name = "Undefined"
        self.params = list()
    def addData(self, parameter: data):
        self.params.append(parameter)
    def setName(self, name: str):
        self.name = name
class day:
    def __init__(self):
        self.name = "Undefined"
        self.lessons = list()
    def addLesson(self, les: lesson):
        self.lessons.append(les)
    def setName(self, name: str):
        self.name = name
    def getInfo(self):
        print(self.name + ":")
        for x in self.lessons:
            print(" " + x.name + ":")
            for y in x.params:
                print("  " + y.name)
class rasp:
    def __init__(self):
        self.days = list()
    def addDay(self, d: day):
        self.days.append(d)
def from_yaml(infile: list):
    regex_equal = re.compile(r"^((\s*[^\s:]+\s*):(\s*(\"[^\n]+\")|([^\n\s]+[^\n]+)|('[^\n]+')\s*))\n?$") #Строка с операцией присваивания
    regex_init = re.compile(r"^(\s*[^\s:]+\s*):\n?$") #Строка с операцией инициализации
    raspisanie = rasp()
    curlesson = lesson()
    curday = day()
    for s in infile:
        s = re.sub(r"\n+","",s)
        if regex_equal.match(s) != None:
            curline = s.strip()
            spl = curline.split(':', maxsplit = 1)
            curdata = data(spl[0].strip(), spl[1].strip())
            curlesson.addData(curdata)
        elif regex_init.match(s) != None:
            spl = s.split(':', maxsplit = 1)
            if (len(spl) > 0):
                stripped = spl[0].lstrip()
                delta = len(spl[0]) - len(stripped)
                if delta == 1:
                    if (len(curlesson.params) != 0):
                        curday.addLesson(curlesson)
                        print("saved lesson")
                    curlesson = lesson()
                    curlesson.setName(stripped)
                    print("creating lesson", stripped)
                elif delta == 0:
                    if (len(curday.lessons) != 0):
                        raspisanie.addDay(curday)
                        print("saved day")
                    curday = day()
                    curday.setName(stripped)
                    print("created day", stripped)
        else:
            print("Undefined string")
    if (len(curlesson.params) != 0):
        curday.addLesson(curlesson)
        print("saved lesson")
    curlesson = lesson()
    if (len(curday.lessons) != 0):
        raspisanie.addDay(curday)
        print("saved day")
    curday = day()
    return raspisanie
inputf = open('raspisanie.yml', 'r', encoding = "utf-8")
ymllist = list()
curline = inputf.readline()
while (curline):
    ymllist.append(curline)
    curline = inputf.readline()
raspisanie = from_yaml(ymllist)
