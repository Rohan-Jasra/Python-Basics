import csv


#opening the raw data made by user
tradeFile=open('raw.csv')
tradeReader=csv.reader(tradeFile)
tradeData=list(tradeReader)

#opening the extract ran on app by user
extractFile=open('extract.csv')
extractReader=csv.reader(extractFile)
extractData=list(extractReader)

#setting lengths of each list
indexN=-1
listLength=len(tradeData)
extractLength=len(extractData)

#initializing the list that will hold the parsed extract data
infoArr = []

#parsing the extract data and pushing it to the list
for (index, elem) in enumerate(tradeData):
    if index==listLength:
        break
    for (idx, val) in enumerate(extractData):
        if(val[0] == elem[1] and (val[13] == elem[2] or val[15] == elem[2])):
            infoArr.append(val)

#setting lengths on the parsed list
infoArrLength = len(infoArr)


#initalizing the list which will hold the data neccessary for the transfer file
assetArr = []

#parsing the extract data
for (index, elem) in enumerate(infoArr):
    
    if index==infoArrLength:
        break
    assetArr.append(tradeData[index][0]) #Date
    assetArr.append(infoArr[index][0])   #Fund code
    assetArr.append(infoArr[index][2])   #Security
    assetArr.append(infoArr[index][8])   #Shares
    assetArr.append(infoArr[index][9])   #Base Cost 
    assetArr.append(infoArr[index][22])   #Native Cost

#Slicing the infoArr into seperate elements
finalArr = []
assetArrLength = len(assetArr)
numOfTransfers = int(assetArrLength / 6) #this will give us the number of securities that are being transferred
numOfLoops = numOfTransfers * 6
arrCounterStart = 0
arrCounterEnd = 6

for i in range(0, numOfTransfers):
    finalArr.append(assetArr[arrCounterStart:arrCounterEnd])
    arrCounterStart = arrCounterStart + 6
    arrCounterEnd = arrCounterEnd + 6

print(finalArr)

"""
#prorating the shares - tradeData vs infoArr
sharesIterator = -1
transferShares = []
totalShares = []
proratedFactor = []

for index, share in enumerate(tradeData):
    if index == listLength:
        break
    transferShares.append(tradeData[index][2])

for index, share in enumerate(infoArr):
    if index == infoArrLength:
        break
    totalShares.append(infoArr[index][6])

for index, share in enumerate(totalShares):
    if index == infoArrLength:
        break
    proratedFactor[index] = totalShares[index] / transferShares[index]   

"""

print(infoArr)
print('----------------')
print(assetArr)
print('----------------')
print(finalArr)
"""
print('----------------')
print(tradeData)
print('----------------')
print(infoArr)
print('----------------')
print(assetArr)
print('----------------')
print(transferShares)
print('----------------')
print(totalShares)
print('----------------')
"""

"""for index in enumerate(tradeData):
    indexN=indexN+1
    if indexN==listLength:
        break
    for key,value in dict1.items():
        if (tradeData[indexN][1])==key:
            tradeData[indexN][1]=value
print(tradeData)
            
with open("Converted.csv","a", newline='') as File:
    finish= csv.writer(File)
    finish.writerows(tradeData)
File.close()"""  
