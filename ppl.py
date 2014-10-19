import re

keywords=('Nucleotide','Protien','Seq','AminoAcids','int','for','length','in','if','else','end','print','getSequence','getAminoAcid','to','with')
operators=('-+-','-/-','.','(',')',',','{','}','[',']','+','-','*','/','++','--','%','==','>=','<=','>','<',';')

splittingOperators = ['(',')','}','{','[',']','+','-','.',',','*','/','++','--','%','==','>=','<=','>','<',';','-+-','-/-']

x = re.split('(\\+\\+|\\+|\\-\\-|\\-|\s)\s*',line)

def splitOperation(string):
    templist=[]
    templist2=[]
    found=[]
    
    templist.append(string)

    for symbol in splittingOperators:
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

file=open('3.txt')
tokens = []
for line in file:
    line=line.strip()
    if len(line) == 0:
        continue
    line=line.rstrip('\n')
    words=line.split()
    for word in words:
        tokens.extend(splitOperation(word))

print(tokens)
