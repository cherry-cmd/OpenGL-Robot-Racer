file=open('1.txt')

import re

tokenType = {
    'Nucleotide':'Keyword','Protein':'Keyword','Seq':'Keyword','AminoAcids':'Keyword','int':'Keyword','for':'Keyword','length':'Keyword','in':'Keyword','if':'Keyword','else':'Keyword','end':'Keyword','print':'Keyword','getSequence':'Keyword','getAminoAcid':'Keywords','to':'Keyword','with':'Keyword',
    'is':'Operator','-+-':'Operator','-/-':'Operator','+':'Operator','-':'Operator','*':'Operator','/':'Operator','++':'Operator','--':'Operator','==':'Operator','>=':'Operator','<=':'Operator','>':'Operator','<':'Operator',
    ';':'Special Symbol','(':'Special Symbol',')':'Special Symbol','%':'Special Symbol','{':'Special Symbol','}':'Special Symbol','[':'Special Symbol',']':'Special Symbol','.':'Special Symbol',',':'Special Symbol'
}

temp = []
stringLiterals = []
tokens = []

splittingOperators = ['(',')','}','{','[',']','+','-','.',',','*','/','%','==','>=','<=','>','<',';']
ids = "[a-zA-z][a-zA-Z0-9]*[_]*[a-zA-z][a-zA-Z0-9]*|[a-zA-z][a-zA-Z0-9]*"

def isIntLiteral(integer):
    try: 
        int(integer)
        return True
    except ValueError:
        return False

def splitOperation(string):
    x = [value.strip() for value in re.split('(\s|\\-\\+\\-|\\-\\/\\-|\\+\\+|\\+|\\-\\-|\\-|\\(|\\)|\\{|\\}|\\[|\\]|\\.|\\*|\\%|==|\\>\\=|\\<\\=|;|/|>|<|\\=\\=|,)\s*',string) if not len(value.strip()) == 0]
    return x

for line in file:
    line=line.strip()
    if len(line) == 0:
        continue
    line=line.rstrip('\n')
    if '"' in line:
        temp=line.split('"')
        line = temp[0] + temp[1] + temp[2]
        stringLiterals.append(temp[1])
    tokens.extend(splitOperation(line))

for term in tokens:
    if term in tokenType.keys():
        print (term+' : '+tokenType[term])
    elif isIntLiteral(term)==True:
        print (term + ' : Integer Literal')
    elif term in stringLiterals:
        print (term + ' : String Literal')
    else:
      tkn = re.findall(ids,term)
      if(len(tkn) == 1 ):
          if(tkn[0] == term):
              print(term + ' : Identifier')
          else:
              print(term + ' : Invalid  Identifier')
      else:
          print(term + ' : Invalid  Identifier')


