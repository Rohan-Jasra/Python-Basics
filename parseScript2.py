import csv

activityFile=open('USB.csv')
activityReader=csv.reader(activityFile)
activityData=list(activityReader)

#Reference dictionary
refDict = {'CC&L All Strategies Fund' : 'CCSU', 'CC&L Multi-Strategy Fund' : 'CMUQ', 'CC&L Q 140 40 Fund' : 'Q140U', 'CC&L Q Equity Extension Fund' : 'CCQU', 'CC&L Q Market Neutral Fund II' : 'CQMU', 'CC&L Q US Equity Extension Fd' : 'CUBS', 'CC&L US Q Mkt Neut On Fd II' : 'CUQU', 'CCL Q Equity Extension Fund II' : 'CQUB', 'Q Market Neutral Fund': 'CQOU'}

ctData = []

for elem in activityData:
    if elem[8].startswith('AUTOFX:') and elem[1] != 'USD':
        ctData.append(elem[0])
        ctData.append(elem[1])
        ctData.append(elem[4])
        ctData.append(elem[8])
        ctData.append(elem[11])
        ctData.append(elem[15])
#ctData.append(elem[0]) - Fund
#ctData.append(elem[1]) - Currency
#ctData.append(elem[4]) - Settle date
#ctData.append(elem[8]) - Info
#ctData.append(elem[11]) - Reference
#ctData.append(elem[15]) - Native net amount


#Slicing the activityDate into seperate elements
arrLen = len(ctData)
dataLen = 6
numOfTransfers = int(arrLen / dataLen) 
numOfLoops = numOfTransfers * dataLen
arrCounterStart = 0
arrCounterEnd = 6
ctDataArr = []


for i in range(0, numOfTransfers):
    ctDataArr.append(ctData[arrCounterStart:arrCounterEnd])
    arrCounterStart = arrCounterStart + dataLen
    arrCounterEnd = arrCounterEnd + dataLen

#making sure the two net amounts have two decimals
decimalsNative = []
decimalsUSD = []

for elem in ctDataArr:
    decimalsNative.append(elem[5])
for elem in activityData:
    if elem[8].startswith('AUTOFX:') and elem[1] == 'USD':
        decimalsUSD.append(elem[15])
        
for index, elem in enumerate(decimalsNative):
    if elem.find('.') == -1:
        decimalsNative[index] = decimalsNative[index] + '.00'

for index, elem in enumerate(decimalsUSD):
    if elem.find('.') == -1:
        decimalsUSD[index] = decimalsUSD[index] + '.00'

#removing the '-' in both native and USD


#The program requires fund code/trade date/settle date/buy currency/sell currency/rate/Buy amount/Sell amount/Reference

#Making the fund code array
fundCode = []
for elem in ctDataArr:
    for key, value in refDict.items():
        if elem[0] == key:
            fundCode.append(value)


#Trade date and settle date
dateDict = {'Jan' : '1', 'Feb': '2', 'Mar': '3', 'Apr': '4', 'May': '5', 'Jun': '6', 'Jul': '7', 'Aug': '8', 'Sep': '9', 'Oct': '10', 'Nov': '11', 'Dec': '12'}
ctDate = ctDataArr[0][2]
ctDateYear = '2018'
ctDateDay = ctDate[0:2]
ctDateMon = ctDate[3:6]
ctDateMonNum = ''

for key,value in dateDict.items():
    if key == ctDateMon:
        ctDateMonNum = value
       
#Buy/Sell currency
buyCur = []
sellCur = []

for elem in ctDataArr:
    if float(elem[5]) * -1 == abs(float(elem[5])):
        sellCur.append(elem[1])
        buyCur.append('USD')
    else:
        sellCur.append('USD')
        buyCur.append(elem[1])


test = 'hello'
print(test.find('k'))

print('---------------')
print(ctDataArr)
print('---------------')
print(fundCode)
print('---------------')
print(buyCur)
print('---------------')
print(sellCur)
print('---------------')
print(decimalsNative)
print('---------------')
print(decimalsUSD)
print('---------------')





    

