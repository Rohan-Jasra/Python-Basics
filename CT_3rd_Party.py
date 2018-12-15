import csv
import random
from datetime import date

#This program makes a few assumptions
# 1) all transfers must have a USD side
# 2) the first transfer will dictate the date used for ALL transfers

activityFile=open('RBC.csv')
activityReader=csv.reader(activityFile)
activityData=list(activityReader)

#Reference dictionary
refDict = {'CCL_9001': 'CHY', 'CCL_6022': 'PIEI', 'CCL_979': 'CGBA', 'CCL_3400': 'BGAS', 'CCL_9004': 'CDMN', 'CCL_199': 'CCLB', 'CCL_369': 'CCQC', 'CCL_6014': 'CAEE', 'CCL_3155': 'PCUM', 'CCL_3024': 'SRCE', 'CCL_1003': 'CCLQ', 'CCL_1089': 'CCLQ', 'CCL_1200': 'PCIP', 'CCL_9003': 'CARF', 'CCL_3026': 'SRST', 'CCL_339': 'CPCC', 'CCL_2006': 'PCJC', 'CCL_1180': 'PCE', 'CCL_1167': 'PUMN', 'CCL_806': 'CCR2', 'CCL_600': 'CIIF', 'CCL_2051': 'PAR', 'CCL_936': 'GARP', 'CCL_937': 'GARP', 'CCL_366': 'CCQG', 'CCL_980': 'CHIF', 'CCL_1325': 'C130', 'CCL_1326': '130R', 'CCL_340': 'CPCB', 'CCL_3035': 'BGAB', 'CCL_4003': 'CCPT', 'CCL_6019': 'NSUF', 'CCL_130': 'CMMK', 'CCL_1103': 'CCQO     ', 'CCL_918': 'CCQR', 'CCL_1309': 'CCCS', 'CCL_1346': 'CQS', 'CCL_1290': 'CLLB', 'CCL_755': 'CCEV', 'CCL_1142': 'PCUE', 'CCL_1292': 'CQEM', 'CCL_356': 'CCLG', 'CCL_3034': 'SREA', 'CCL_919     ': 'CMSF   ', 'CCL_1260': 'CMST', 'CCL_1272 ': 'CMSR', 'CCL_1273 ': 'CMCA', 'CCL_978': 'CGBF', 'CCL_1274': 'CSHT', 'CCL_974': 'CPSR', 'CCL_129': 'CCEF', 'CCL_9000': 'CEIG', 'CCL_3044': 'SCEC', 'CCL_1231': 'CFCE', 'CCL_1002': 'CCQN', 'CCL_1311': 'CQCS', 'CCL_308': 'CCLT', 'CCL_874': 'CPCS', 'CCL_1058': 'PCHY', 'CCL_1015': 'CASF     ', 'CCL_1020': 'CASF     ', 'CCL_1154': 'CAQC', 'CCL_1153': 'CAQU', 'CCL_1310': 'CACS', 'CCL_1212': 'CAST', 'CCL_1156': 'CAFI', 'CCL_1155': 'CAF ', 'CCL_1343': 'CASS', 'CCL_6021': 'PSRI', 'CCL_326': 'CCCE', 'CCL_2028': 'PCCS', 'CCL_328': 'CCMM', 'CCL_975': 'CUBA', 'CCL_1083': 'CCQ2', 'CCL_1091': 'CCQ2', 'CCL_341': 'CLST', 'CCL_6016': 'WOIN', 'CCL_3240': 'SRUS', 'CCL_1328': 'C140', 'CCL_1327': '140R', 'CCL_315': 'CCLF', 'CCL_1029': 'CUQ2', 'CCL_1150': 'CUQC', 'CCL_1186': 'CUQT', 'CCL_1245': 'CUQD', 'CCL_7000': 'PCGS', 'CCL_3025': 'SRBF', 'CCL_368': 'CCQV', 'CCL_1157': 'CSCM', 'CCL_1270': 'CCEI', 'CCL_952': 'CLBA', 'CCL_3027': 'SRMM', 'CCL_628': 'PCIT', 'CCL_046': 'GEN', 'CCL_3029': 'SRAB', 'CCL_1230': 'CGCQ ', 'CCL_850': 'CCSC', 'CCL_1345': 'CCQS', 'CCL_1344': 'CCS ', 'CCL_1376': 'CATD', 'CCL_1378': 'CUTD', 'CCL_1377': 'GART', 'CCL_1414': 'Q140S', 'CCL_1417': 'CQMN', 'CCL_1420': 'CQMS', 'CCL_1418': 'CQMT', 'CCL_1419': 'CQMC', 'CCL_1411': 'CUCS', 'CCL_1415': 'Q140C', 'CCL_1416': 'CURB', 'CCL_1429': 'GARS', 'CCL_1427': 'CASFS2', 'CCL_1438': 'CFIRT', 'CCL_1435': 'CFIRR', 'CCL_1441': 'CFIR', 'CCL_1439': 'CUSG', 'CCL_1430': 'CUSS', 'CCL_1443': 'C150', 'CCL_866': 'CQOR', 'CCL_1452': 'CQOU', 'CCL_1494': 'CMTF', 'CCL_1495': 'CMTQ', 'CCL_1496': 'CMCF', 'CCL_1498': 'CMCQ', 'CCL_1111': 'CMSE', 'CCL_1123': 'CMFQ', 'CCL_1497': 'CMSQ', 'CCL_1500': 'CMUQ', 'CCL_1507': 'CMSR     ', 'CCL_1525': '130C', 'CCL_1547': 'CMCM', 'CCL_1548': 'CFIM', 'CCL_1533': '130S', 'CCL_1542': 'CQTS', 'CCL_1541': 'CQTD', 'CCL_1538': 'CQSC', 'CCL_1540': 'CQCM', 'CCL_1537': 'CQEC', 'CCL_1539': 'CQUB', 'CCL_1570': 'CUBS', 'CCL_1569': 'CEES', 'CCL_1568': 'CCES', 'CCL_1566': 'CCTD', 'CCL_1567': 'CCEM', 'CCL_7015': 'GAAS', 'CCL_1576': 'CUQU', 'CCL_1572': 'CCSU', 'CCL_1574': 'CCQU', 'CCL_1575': 'CCUB', 'CCL_1573': 'Q140U', 'CCL_1688': 'Q140B', 'CCL_1687': 'CQMB', 'CCL_1660': 'CQJP', 'CCL_1664': 'CMJP', 'CCL_1662': 'CCJP', 'CCL_1666': 'CAJP'}
ctData = []

for elem in activityData:
    if elem[1].startswith('GROSS'):
        ctData.append(elem[13])  #CLC Number for mapping
        ctData.append(elem[2])  #sell currency
        ctData.append(elem[5])  #buy currency
        ctData.append(elem[3])  #sell currency amount
        ctData.append(elem[6])  #buy currency amount
        ctData.append(elem[15]) #reference
        ctData.append(elem[9])  #trade date
        ctData.append(elem[10]) #settle date


#Slicing the activityDate into seperate elements
arrLen = len(ctData)
dataLen = 8
numOfTransfers = int(arrLen / dataLen) 
numOfLoops = numOfTransfers * dataLen
arrCounterStart = 0
arrCounterEnd = 8
ctDataArr = []


for i in range(0, numOfTransfers):
    ctDataArr.append(ctData[arrCounterStart:arrCounterEnd])
    arrCounterStart = arrCounterStart + dataLen
    arrCounterEnd = arrCounterEnd + dataLen


#The program requires fund code/trade date/settle date/buy currency/sell currency/rate/Buy amount/Sell amount/Reference

#Setting up the net amounts in USD and foreign currency
decimalsNative = []  #This will be sell amount
decimalsUSD = []    #This will be buy amount

for elem in ctDataArr:
    decimalsNative.append(elem[3])
for elem in ctDataArr:
    decimalsUSD.append(elem[4])
        
decimalsUSDTrue = []

for elem in ctDataArr:
    decimalsUSDTrue.append(elem[4])
    

#making sure the two net amounts have two decimals        
for index, elem in enumerate(decimalsNative):
    if elem.find('.') == -1:
        decimalsNative[index] = decimalsNative[index] + '.00'

for index, elem in enumerate(decimalsUSD):
    if elem.find('.') == -1:
        decimalsUSD[index] = decimalsUSD[index] + '.00'

for index, elem in enumerate(decimalsUSDTrue):
    if elem.find('.') == -1:
        decimalsUSDTrue[index] = decimalsUSDTrue[index] + '.00'

#removing the '-' in both native and USD
def removeChar(arr, char):
    for index, elem in enumerate(arr):
        if elem.find(char) != -1:
            arr[index] = elem.replace(char,'')
    return arr

removeChar(decimalsNative, '-')      
removeChar(decimalsUSD, '-')
removeChar(decimalsUSDTrue, '-')
removeChar(decimalsUSDTrue, ',')


#add a zero if only one decimal place
def addDec(arr):
    for index, elem in enumerate(arr):
        checkArr = elem.split('.')
        if len(checkArr[1]) == 1:
            arr[index] = elem+'0'
                       
addDec(decimalsNative)
addDec(decimalsUSD)
addDec(decimalsUSDTrue)

#removing the '.' in both native and USD
removeChar(decimalsNative, '.')      
removeChar(decimalsUSD, '.')
removeChar(decimalsUSDTrue, '.')

#normalizing the net amounts to the appropriate amount of characters
amountCount = '000000000000000'
finalAmountUSD = []
finalAmountUSDTrue = []
finalAmountNative = []

def amountGenerator(arr, string, newArr):
    for index, elem in enumerate(arr):
        length = len(elem)
        newAmount = ''
        newAmount = string[0:(15-length)] + elem
        newArr.append(newAmount)
    return newArr

amountGenerator(decimalsUSD, amountCount, finalAmountUSD)   
amountGenerator(decimalsNative, amountCount, finalAmountNative)
amountGenerator(decimalsUSDTrue, amountCount, finalAmountUSDTrue) 


#Making the fund code array
fundCode = []
for elem in ctDataArr:
    for key, value in refDict.items():
        if elem[0] == key:
            fundCode.append(value)


#Trade date and settle date
dateDict = {'Jan' : '1', 'Feb': '2', 'Mar': '3', 'Apr': '4', 'May': '5', 'Jun': '6', 'Jul': '7', 'Aug': '8', 'Sep': '9', 'Oct': '10', 'Nov': '11', 'Dec': '12'}

ctDateYear = '2018'
ctDateYearShort = '18'

ctDateDayTrade = []
ctDateDaySettle = []
ctDateMonTrade = []
ctDateMonSettle = []

for elem in ctDataArr:
    ctDateDayTrade.append(elem[6][0:2])

for elem in ctDataArr:
    ctDateDaySettle.append(elem[7][0:2])

for elem in ctDataArr:
    ctDateMonTrade.append(elem[6][3:6])

for elem in ctDataArr:
    ctDateMonSettle.append(elem[7][3:6])



#Setting today date
todayDate = str(date.today())
todayDateDay = todayDate[8:10]
todayDateMon = todayDate[5:7]
todayDateYear = todayDate[0:4]


#reference
refNum = []
for elem in ctDataArr:
    refNum.append(elem[5])
    
finalRefNum = []

def refGen(arr, length, newArr):
    for index, elem in enumerate(arr):
        elemLen = len(elem)
        diff = length - elemLen
        
        if elemLen == length:
            continue
        
        elif elemLen > length:
            newElem = elem[0:length]
            newArr.append(newElem)
            
        elif elemLen < length:
            elemChar = ''
            for i in range (diff):
                rand =  str(random.randint(1,9))
                elemChar = elemChar+rand
            finalElemChar = elem + elemChar
            newArr.append(finalElemChar)
    return newArr

refGen(refNum, 13, finalRefNum)

#adding spaces at the end of fund code to equal char length
fundCodeFinal = []

fundCodeWidth = 9
for index, elem in enumerate(fundCode):
    length = len(elem)
    newElem = elem.ljust(fundCodeWidth, ' ')
    fundCodeFinal.append(newElem)

#setting the rate
curRate = '00000000000'

#setting the required field
tType = 'SPT'

#setting up the final array and apending the values
finalArr = []

for index, elem in enumerate(finalRefNum):
    finalArr.append(tType)
    finalArr.append(fundCodeFinal[index])
    finalArr.append(ctDateDayTrade[index])
    finalArr.append(ctDateYearShort)
    finalArr.append(ctDateDaySettle[index])
    finalArr.append(ctDateMonSettle[index])
    finalArr.append(ctDateYear)
    finalArr.append(ctDataArr[index][2])
    finalArr.append(ctDataArr[index][1])
    finalArr.append(curRate)
    finalArr.append(finalAmountUSD[index][4])
    finalArr.append(finalAmountNative[index][3])
    finalArr.append(elem)            

print(finalArr)

#Slicing the activityDate into seperate elements
arrLenFinal = len(finalArr)
dataLenFinal = 13
numOfTransfersFinal = int(arrLenFinal / dataLenFinal) 
numOfLoopsFinal = numOfTransfersFinal * dataLenFinal
arrCounterStartFinal = 0
arrCounterEndFinal = 13
finalArrSorted = []


for i in range(0, numOfTransfersFinal):
    finalArrSorted.append(finalArr[arrCounterStartFinal:arrCounterEndFinal])
    arrCounterStartFinal = arrCounterStartFinal + dataLenFinal
    arrCounterEndFinal = arrCounterEndFinal + dataLenFinal


#Setting the header and trailer
header = 'HEADER    '+todayDateDay+todayDateMon+todayDateYear
finalArrSorted.insert(0, header)
recordLen = str(len(fundCodeFinal))
recordLenLen = len(recordLen)
recordNum = '0000000'
newRecordNum = recordNum.replace('0', '',recordLenLen)
newRecordNum = newRecordNum + recordLen
finalArrSorted.append('TRAILER    '+newRecordNum)

print(finalArrSorted)

finalArrList = []
#for i in finalArrSorted:
#    spl = i.split(',')
#    finalArrList.append(spl)

with open('gplus_currtrf.csv', newline='') as File:
    finish= csv.writer(File)
    finish.writerows(finalArrSorted)
File.close()


