inputf = open('raspisanie.yml', 'r', encoding = "utf-8")
outputf = open('raspisanie.csv', 'w', encoding = "utf-8")
curline = inputf.readline()
line = list()
while (curline):
    line.append(curline)
    curline = inputf.readline()
level = 0
csvstring = list()
csvstring.append("")
for i in range(len(line)-1):
    curline = line[i].lstrip()
    spl = curline.split(':', maxsplit = 1)
    if len(spl) == 1 or spl[1] == '\n':     
        level += 1
        if (len(csvstring) <= level):
            csvstring.append(csvstring[level-1]+';'+spl[0])
        else:
            csvstring[level] = csvstring[level-1]+';'+spl[0]
    else:
        nextline = line[i+1].lstrip()
        nextspl = nextline.split(':', maxsplit = 1)
        csvstring[level] += ';'+spl[1].lstrip()[:-1]
        if nextspl == 1 or nextspl[1] == '\n':
            outputf.write(csvstring[level][1:]+'\n')
            level -= 1
spl = line[-1].lstrip().split(':', maxsplit = 1)
csvstring[level] += ';'+spl[1].lstrip()[:-1]
outputf.write(csvstring[level][1:]+'\n')
