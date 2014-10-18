###### can an identifier be used as an attribute of an object? probably yes ---- suite
###### "{" aur "}" humne special symb me likhe hi nahi.
##### "increase..by.." operator separately. "is not" and "is in" need separate attention.

keywords=('declare','player','score','players','card','int','string','suite','value','centralstack','standard52','current','next','winner','if','else','while','rotate','round','complete','incomplete','board','position')
operators=('count','select','min','max','mod','patterns','.','=','is','is not','is in','full','->')
specialsymbols=(',','(',')','{','}','#')

splitby = ['(', ')', '{', '}', '=', '.', '->']

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
        #"," ko bhi found me add kar do, jaise pehle "clipper" me kiya tha. aise har special symbol ke liye.
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
        #print('found={}'.format(templist))

    templist2 = []
    for word in templist:
        if not len(word) == 0:
            templist2.append(word)
    #print(templist2)
    return templist2

answer = []
fh=open('tictac.txt')
for line in fh:
    line=line.strip()
    if len(line) == 0:
        continue
    try:
        if line[0]=='#':
            #add "#" to the list foundTokens
            ####comment handle karne me aur problem hai. agar beech line ke comment hua to?use something like "if line has #then cut the rest."
            continue
        else:
            line=line.rstrip('\n')
            words=line.split()
            for word in words:
                answer.extend(symbolclip(word))
    except:
        pass

print(answer)
