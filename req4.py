import re

class data:
    def __init__(self, name: str, val: str):
        self.name = name
        self.val = val
class lesson:
     def __init__(self, name: str, params: list):
        self.name = name
        self.params = params
class day:
    def __init__(self, name: str, lessons: list):
        self.name = name
        self.lessons = lessons
class rasp:
    def __init__(self, days: list):
        self.days = days
def from_yaml(infile: list):
    regex_equal = re.compile(r"^((\s*[^\s:]+\s*):(\s*(\"[^\n]+\")|([^\n\s]+[^\n]+)|('[^\n]+')\s*))\n?$") #Строка с операцией присваивания
    regex_init = re.compile(r"^(\s*[^\s:]+\s*):\n?$") #Строка с операцией инициализации
    for s in infile:
        s = re.sub(r"\n+","",s)
        if regex_equal.match(s) != None:
            curline = s.strip()
            spl = curline.split(':', maxsplit = 1)
            curdata = data(spl[0].strip(), spl[1].strip())
            print(curdata.name, curdata.val)
        elif regex_init.match(s) != None:
            print("string ", s, " is an initialization string")
        else:
            print("Not defined string")
inputf = open('raspisanie.yml', 'r', encoding = "utf-8")
ymllist = list()
curline = inputf.readline()
while (curline):
    ymllist.append(curline)
    curline = inputf.readline()
from_yaml(ymllist)
