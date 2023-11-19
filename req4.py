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
    def printAll(self):
        for x in self.days:
            print (x.name + ":")
            for y in x.lessons:
                print(" " + y.name + ":")
                for z in y.params:
                    print("  " + z.name + ":" + z.val)
def from_yaml(infile: list):
    regex_equal = re.compile(r"^((\s*[^\s:]+\s*):(\s*(\"[^\n]+\")|([^\n\s]+[^\n]+)|('[^\n]+')\s*))\n?$") #Строка с операцией присваивания
    regex_init = re.compile(r"^(\s*[^\s:]+\s*):\n?$") #Строка с операцией инициализации
    raspisanie = rasp()
    curlesson = lesson()
    curday = day()
    for s in infile:
        s = re.sub(r"\n+","",s)
        s.rstrip()
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
                    curlesson = lesson()
                    curlesson.setName(stripped)
                elif delta == 0:
                    if (len(curday.lessons) != 0):
                        raspisanie.addDay(curday)
                    curday = day()
                    curday.setName(stripped)
        else:
            print("Undefined string")
            print(s)
    if (len(curlesson.params) != 0):
        curday.addLesson(curlesson)
    curlesson = lesson()
    if (len(curday.lessons) != 0):
        raspisanie.addDay(curday)
    curday = day()
    return raspisanie
def to_json(r: rasp, filename: str):
    outputf = open(filename, 'w', encoding = "utf-8")
    outputf.write("{\n")
    for d in r.days:
        dname = d.name if d.name[0] == "\"" else "\""+d.name+"\""
        outputf.write(" " + dname + ":\n")
        outputf.write(" {\n")
        for l in d.lessons:
            lname = l.name if l.name[0] == "\"" else "\""+l.name+"\""
            outputf.write("  " + lname + ":\n")
            outputf.write("  {\n")
            for p in l.params:
                pname = p.name if p.name[0] == "\"" else "\"" + p.name + "\""
                pval = p.val if p.val[0] == "\"" else "\"" + p.val + "\""
                outputf.write("   " + pname + ":" + pval + "\n")
            outputf.write("  }\n")
        outputf.write(" }\n")
    outputf.write("}\n")
inputf = open('raspisanie1.yml', 'r', encoding = "utf-8")
ymllist = list()
curline = inputf.readline()
while (curline):
    ymllist.append(curline)
    curline = inputf.readline()
raspisanie = from_yaml(ymllist)
to_json(raspisanie, "raspisanie3.json")
