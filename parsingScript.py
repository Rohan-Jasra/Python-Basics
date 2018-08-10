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
for index in enumerate(tradeData):
    indexN=indexN+1
    if indexN==extractLength:
        break
    if(tradeData[indexN][0] == extractData[indexN][0] and tradeData[indexN][1] == extractData[indexN][1]):
       infoArr.append(extractData[indexN])

#setting lengths on the parsed list
infoArrLength = len(infoArr)
infoArrIterator = -1

#initalizing the list which will hold the data neccessary for the transfer file
assetArr = []

#parsing the extract data
for index in enumerate(infoArr):
    infoArrIterator = infoArrIterator+1
    if infoArrIterator==infoArrLength:
        break
    assetArr.append(infoArr[infoArrIterator][0])
    assetArr.append(infoArr[infoArrIterator][1])
    assetArr.append(infoArr[infoArrIterator][4])
    assetArr.append(infoArr[infoArrIterator][5])
    assetArr.append(infoArr[infoArrIterator][6])

assetArrLength = len(assetArr)

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

print(tradeData)
print('----------------')
print(extractData)
print('----------------')
print(infoArr)
print('----------------')
print(assetArr)
print('----------------')
print(transferShares)
print('----------------')
print(totalShares)
print('----------------')


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
    
