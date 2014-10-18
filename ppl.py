keywords=('Nucleotide','Protien','Seq','AminoAcids','int','for','length','in','if','else','end','print','getSequence','getAminoAcid','to','with')
operators=('-+-','-/-','(',')',',','{','}','[',']','+','-','*','/','++','--','%','==','>=','<=','>','<',';')

splitby = ['(',')','}','{','+','-',',','*','/','++','--','%','==','>=','<=','>','<',';','-+-','-/-']

found=[]
templist=[]
templist2=[]

def isLiteral():
    pass

def isIdentifier():
    pass

def symbolclip(myword):
    global templist
    global templist2
    global found
    templist=[]
    templist2=[]
    found=[]

    if ',' in myword:
        tempans = []
        templist=myword.split(',')
        for word in templist:
            tempans.append(word)
            tempans.append(',')
        templist = tempans[:-1]
    else:
        templist.append(myword)
    
    for symbol in splitby:
        for q in templist:
            templist2=q.split(symbol)
            tempans = []
            for word in templist2:
                tempans.append(word)
                tempans.append(symbol)
            templist2 = tempans[:-1]
            found.extend(templist2)
        templist=found
        found=[]

    templist2 = []
    for word in templist:
        if not len(word) == 0:
            templist2.append(word)
    return templist2

answer = []

fh=open('4.txt')
for line in fh:
    line=line.strip()
    if len(line) == 0:
        continue
    line=line.rstrip('\n')
    words=line.split()
    for word in words:
        answer.extend(symbolclip(word))

print(answer)
