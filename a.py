import re

tokenType = {
    'Nucleotide':'keyword','Protein':'keyword','Seq':'keyword','AminoAcids':'keyword','int':'keyword','for':'keyword','length':'keyword','in':'keyword','if':'keyword','else':'keyword','end':'keyword','print':'keyword','getSequence':'keyword','getAminoAcid':'keywords','to':'keyword','with':'keyword',
    '-+-':'operator','-/-':'operator','.':'operator','(':'operator',')':'operator',',':'operator','{':'operator','}':'operator','[':'operator',']':'operator','+':'operator','-':'operator','*':'operator','/':'operator','++':'operator','--':'operator','%':'operator','==':'operator','>=':'operator','<=':'operator','>':'operator','<':'operator',';':'operator'
}

tokens = []
literals = []
identifier = []

splittingOperators = ['(',')','}','{','[',']','+','-','.',',','*','/','%','==','>=','<=','>','<',';']

line = "hel>=l(ii %ei a) me*o/w -+- sk-/-k"
x = re.split('(\\-\\+\\-|\\-\\/\\-|\\+\\+|\\+|\\-\\-|\\-|\s|\\(|\\)|\\{|\\}|\\[|\\]|\\.|\\*|\\%|==|\\>\\=|\\<\\=|;|/|>|<|\\=\\=|,)\s*',line)
print (x)

def splitOperation(string):
    pass

file=open('3.txt')
#for line in file:
#    line=line.strip()
#    if len(line) == 0:
#        continue
#    line=line.rstrip('\n')
#    words=line.split()
#    for word in words:
#        tokens.extend(splitOperation(word))

#print(tokens)
#print ([tokenType[t] for t in tokens])
