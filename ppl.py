import re

tokenType = {
    'Nucleotide':'keyword','Protein':'keyword','Seq':'keyword','AminoAcids':'keyword','int':'keyword','for':'keyword','length':'keyword','in':'keyword','if':'keyword','else':'keyword','end':'keyword','print':'keyword','getSequence':'keyword','getAminoAcid':'keywords','to':'keyword','with':'keyword',
    '-+-':'operator','-/-':'operator','.':'operator','(':'operator',')':'operator',',':'operator','{':'operator','}':'operator','[':'operator',']':'operator','+':'operator','-':'operator','*':'operator','/':'operator','++':'operator','--':'operator','%':'operator','==':'operator','>=':'operator','<=':'operator','>':'operator','<':'operator',';':'operator'
}

tokens = []
literals = []
identifier = []

splittingOperators = ['(',')','}','{','[',']','+','-','.',',','*','/','%','==','>=','<=','>','<',';']

# x = re.split('(\\+\\+|\\+|\\-\\-|\\-|\s)\s*',line)

def splitOperation(string):
    temp=[]
    templist2=[]
    found=[]
    
    temp.append(string)

    for symbol in splittingOperators:
        for q in temp:
            templist2=q.split(symbol)
            tempans = []
            for word in templist2:
                tempans.append(word)
                tempans.append(symbol)
            templist2 = tempans[:-1]
            found.extend(templist2)
        found=[]

    templist2 = []
    for word in temp:
        if not len(word) == 0:
            templist2.append(word)
    return templist2

file=open('3.txt')
for line in file:
    line=line.strip()
    if len(line) == 0:
        continue
    line=line.rstrip('\n')
    words=line.split()
    for word in words:
        tokens.extend(splitOperation(word))

print(tokens)


#print ([tokenType[t] for t in tokens])


