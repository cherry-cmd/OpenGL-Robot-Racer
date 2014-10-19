#!/usr/local/bin/python2.7
    
#!/usr/local/bin/python2.7
    
import re







def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False
dict = {'List': '  Keyword','Friend': '  Keyword','Friends': '  Keyword', 'User': ' Keyword', 'check': ' Keyword','traverse':' Keyword','as': ' Keyword','with': ' Keyword','otherwise': ' Keyword','begin': ' Keyword','end': ' Keyword','int': ' Keyword','float': ' Keyword','string': ' Keyword','Timestamp': ' Keyword','Like': ' Keyword','Comment': ' Keyword','Post': ' Keyword','List': ' Keyword','loopbreak': ' Keyword','Name': ' Keyword','Status': ' Keyword','Posts': ' Keyword','Photo': ' Keyword','+':' Operator','++':' Operator','-':' Operator','--':' Operator','*':' Operator','/':' Special Symbol','%':' Operator','=':' Operator','<=':' Operator','->':' Special Symbol','>=':' Operator','!':' Operator','and':' Operator','or':' Operator','>':' Operator','<':' Operator','(':' Special Symbol',')':' Special Symbol','{':' Special Symbol','}':' Special Symbol','[':' Special Symbol','[':' Special Symbol','@':' Special Symbol',';':' Special Symbol',':':' Special Symbol','\\,':' Special Symbol', '.':' Special Symbol',',':'  Special Symbol' }

r="[a-zA-z][a-zA-Z0-9]*"
rexp="[a-zA-z][a-zA-Z0-9]*|\\->|\\(|\\)|\\[|\\]|\\{|\\}|\\+\\+|\\-\\-|\\*|\\/|\\;|\\.|\\:|\\@|\\=|\\>=|\\<=|\\>|\\<|\\!|\\%|\\-|\\+|[0-9][0-9]*" 

fh=open("1.txt","r")
z=1
for text in fh:
  Identifiers=[]
  Special_Symbols=[]
  Keywords=[]
  Integer_Literals=[]
  String_Literals=[]
  Comments=[]
  print ("____________________________________________________________________")
  print ("Line : ",z)
  print ("\n")
 
  splitter = text.split("#")
  comment=''
  if(len(splitter)==3):
    comment= splitter[1]
 
  
  word=splitter[0].split("\"")
  str=[]
  rest=[]
  i=0;
  for x in word:
    if(i%2==0):
      rest.append(x)
    else:
      str.append(x)
    i=i+1

 
  strtext=''
  
  for x in rest:
    strtext=strtext+" "+x+ " "
    

  y=[value.strip() for value in re.split("(\s|->|=|;|\\,|@|:|--|-|\\+\\+|\\+|/|\\*|%|\\.|>=|<=|>|<|\\(|\\)|\\[|\\]|\\{|\\})\s*", strtext) if not len(value.strip()) == 0]
    
  
  i=0
  for term in y:
    if term in dict.keys():
      print (term+'                  '+dict[term])
      
    elif RepresentsInt(term)==True:
      print (term + '                 Integer Literal')
    else:
      q=re.findall(r,term)
      if(len(q)==1 ):
        if(q[0]==term):
          print(term+'                   Identifier')
        else:
          print (term+'           Invalid  Identifier')
      else:
        print (term+'             Invalid  Identifier')
    i=i+1
  for x in str:
    print ('\"           Special Symbol')
    print (x+'         String  Literal')
    print ('\"            Special Symbol')
  if(len(splitter)==3):
    print ('#           Special Symbol')
    print (comment+ '        Comment')
    print ('#           Special Symbol')
  z=z+1;











