import re

tokenType = {
    'Nucleotide':'keyword','Protein':'keyword','Seq':'keyword','AminoAcids':'keyword','int':'keyword','for':'keyword','length':'keyword','in':'keyword','if':'keyword','else':'keyword','end':'keyword','print':'keyword','getSequence':'keyword','getAminoAcid':'keywords','to':'keyword','with':'keyword',
    'is':'operator','-+-':'operator','-/-':'operator','+':'operator','-':'operator','*':'operator','/':'operator','++':'operator','--':'operator','==':'operator','>=':'operator','<=':'operator','>':'operator','<':'operator',
    ';':'Special Symbol','(':'Special Symbol',')':'Special Symbol','%':'Special Symbol','{':'Special Symbol','}':'Special Symbol','[':'Special Symbol',']':'Special Symbol','.':'Special Symbol',',':'Special Symbol'
}

tokens = []
splittingOperators = ['(',')','}','{','[',']','+','-','.',',','*','/','%','==','>=','<=','>','<',';']
ids = "[a-zA-z][a-zA-Z0-9]*|[a-zA-z]_[a-zA-Z0-9]"

def isIntLiteral(integer):
    try: 
        int(integer)
        return True
    except ValueError:
        return False

def splitOperation(string):
    x = [value.strip() for value in re.split('(\s|\\-\\+\\-|\\-\\/\\-|\\+\\+|\\+|\\-\\-|\\-|\\(|\\)|\\{|\\}|\\[|\\]|\\.|\\*|\\%|==|\\>\\=|\\<\\=|;|/|>|<|\\=\\=|,)\s*',string) if not len(value.strip()) == 0]
    return x

file=open('4.txt')
for line in file:
    line=line.strip()
    if len(line) == 0:
        continue
    line=line.rstrip('\n')
    tokens.extend(splitOperation(line))

for term in tokens:
    if term in tokenType.keys():
      print (term+' : '+tokenType[term])
    elif isIntLiteral(term)==True:
      print (term + ' : Integer Literal')
    else:
      tkn = re.findall(ids,term)
      if(len(tkn) == 1 ):
        if(tkn[0] == term):
          print(term + ' : Identifier')
        else:
          print(term + ' : Invalid  Identifier')
      else:
        print(term + ' : Invalid  Identifier')


