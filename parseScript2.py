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

print(ctDataArr)

#The program requires fund code/trade date/settle date/buy currency/sell currency/rate/Buy amount/Sell amount/Reference

#Making the fund code array
fundCode = []
for elem in ctDataArr:
    for key, value in refDict.items():
        if elem[0] == key:
            fundCode.append(value)

print(fundCode)

#Extracting date information from settle date
ctDate = []






    

