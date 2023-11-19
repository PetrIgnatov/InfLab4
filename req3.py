import re
inputf = open('raspisanie.yml', 'r', encoding = "utf-8")
outputf = open('raspisanie2.json', 'w', encoding = "utf-8")
curline = inputf.readline()
line = list()
outputf.write("{\n")
while (curline):
    line.append(curline)
    curline = inputf.readline()
level = 0
for i in range(len(line)-1):
    curline = line[i].lstrip()
    spl = curline.split(':', maxsplit = 1)
    if re.match('^[А-ЯA-Zа-яa-z()0-9]+\s*:\s*\n$', curline) != None:
        outputf.write(" "*(level+1)+ '"'+spl[0]+'":\n' + " "*(level+1) + '{\n')
        level += 1
    else:
        nextline = line[i+1].lstrip()
        if re.match("^[А-ЯA-Zа-яa-z()0-9]+\s*:\s*\n$", nextline) != None:
            outputf.write(" "*(level+1) + '"' + spl[0] + '":' + spl[1] + " "*(level+1) + '}\n')
            level -= 1
        else:
            outputf.write(" "*(level+1) + '"' + spl[0] + '":' + spl[1])
curline = line[-1].lstrip()
spl = curline.split(':', maxsplit = 1)
outputf.write(" "*(level+1) + '"' + spl[0] + '":' + spl[1])
for i in range(level):
    outputf.write(" "*level + '}\n')
    level -= 1
outputf.write('}')
