#Big numbers :)
#https://www.youtube.com/watch?v=5O8Z-pu6R1Q

def cleanSpaces(n):
  counter = 0
  previous = ""
  for c in n:
    if previous ==" " and c == " ":
      return n[:counter-1]
    elif c == " " and counter == len(n)-1:
      return n[:counter]
    previous,c = c,previous
    counter += 1
  return n

def jank(suffix):
  exceptions = {"tresdec":"tredec","sesdec":"sedec","septenvigint":"septemvigint","novenvigint":"novemvigint","quinquadragint":"quindragint","tressexagint":"tresexagint","sessexagint":"sesexagint","tresseptuagint":"treseptuagint","sesseptuagint":"seseptuagint","sesoctogint":"sexoctogint","septenoctogint":"septemoctogint","novenoctogint":"novemoctogint","tresnonagint":"trenonagint","sesnonagint":"sexnonagint","septennonagint":"septenonagint","novennonagint":"novenonagint"}

  if suffix in exceptions.keys():
    return exceptions[suffix]
  else:
    return suffix

#manager
def addTripleName(count,n):
  funcName = 0
  if int(n)<20:
    if len(n)==3 and int(n)<10 and count == 0:
      funcName = "and "+convertNumber(n)
    else:
      funcName = convertNumber(n)
  elif int(n)<100:
    funcName = convertDecimal(n[-2],n[-1])
  else:
    funcName = convertHundred(n)
  funcName = funcName+" "+convertBigNumber(count)
  return funcName;

#all ints?
def convertBigNumberThousands(count):
  return "milli"*(count//1000)

#ints <10^3003
def convertBigNumberHundreds(count):
  biggestNumbersHundreds = ["c","duc","trec","quadring","quing","secs","septing","octing","nong"]
  if (count-1)<1000:
    return convertBigNumberDecimal((count-1)%100)+biggestNumbersHundreds[((count-1)//100)-1]+"entillion"
  else:
    return convertBigNumberThousands(count)
  

def convertBigNumberDecimal(count):
  biggestNumbers = ["","un","duo","tres","quattuor","quin","ses","septen","octo","noven"]
  biggestNumbersDecimals = ["dec","vigint","trigint","quadragint","quinquagint","sexagint","septuagint","octogint","nonagint"]
  if count<10:
    return biggestNumbers[count]
  else:
    return jank(convertBigNumberDecimal((count%10)-1)+biggestNumbersDecimals[(((count-1)%100)-10)//10])

#ints <10^303
def convertBigNumber(count):
  bigNumbers = ["","thousand","m","b","tr","quadr","quint","sext","sept","oct","non"]
  if count < 2:
    funcName = bigNumbers[count]
  elif count < 11:
    funcName = bigNumbers[count]+"illion"
  elif count <= 100:
    funcName = convertBigNumberDecimal(count)+"illion"
  else:
    funcName = convertBigNumberHundreds(count)
  return funcName;

#ints <1000
def convertHundred(n):
  decimal = convertDecimal(n[1],n[2])
  if decimal == "":
    return convertNumber(n[0])+" hundred"
  else:
    return convertNumber(n[0])+" hundred"+" and "+convertDecimal(n[1],n[2])

#ints <100
def convertDecimal(n1,n2):
  decimals = ["twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety"]
  if int(n1)+int(n2) == 0:
    return ""
  elif int(n1+n2)<20:
    return convertNumber(int(n1+n2))
  elif int(n2) == 0:
    name = decimals[int(n1)-2]
  else:
    name = decimals[int(n1)-2]+"-"+convertNumber(n2)
  return name

#ints <20
def convertNumber(n):
  numbers = ["","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
  return numbers[int(n)]

def convertDecimals(n):
  numbers = ["zero","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
  return numbers[int(n)]

validInput = False
top = ""
number = []
lNumber = []
numName = ""
decimals = ""
decis = []
isDot = False

#input
sNumber = input()

#Format into a list like [top,pair of 3,pair of 3,pair of 3....]
lNumber = []
top = ""
numLen = len(str(sNumber))
pos = 0

count = (numLen//3)
isFirst = True

#getting the names of each pair in lNumbers
while numLen>pos:
  if isFirst == True:
    n = sNumber[:numLen%3]
    isFirst = False
  else:
    n = sNumber[pos:pos+3]
  if n == "":
    count -= 1
  elif int(n)==0:
    count -= 1
  else:
    numName = numName+addTripleName(count,n)+" "
  count -= 1
  pos += len(n)
if isDot == True:
  numName = cleanSpaces(numName)+" point "
  for c in decimals:
    decis.append(c)
  for d in decis:
    numName += convertDecimals(d)+" "

print(numName)