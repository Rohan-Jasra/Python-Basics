import csv
from copy import deepcopy


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

#Creating a copy of finalArr by value
endTup = deepcopy(tuple(finalArr))

#Finding the prorated factor per ID
transferShares = {}
totalShares = {}
proratedShares = {}

for (index, elem) in enumerate(tradeData): 
    elem[2] = finalArr[index][2] #this converts client ID to app ID for mapping

for (index, elem) in enumerate(tradeData):
    transferShares[elem[2]] = elem[3]

for (index, elem) in enumerate(infoArr):
    totalShares[elem[2]] = elem[8]

for (keyTotal, valueTotal), (keyApp, valueApp) in zip(totalShares.items(), transferShares.items()):
    if keyTotal == keyApp:
        proratedShares[keyTotal] = float(valueTotal) / float(valueApp)


#Multiplying the base/native cost by prorated factor
for (keyPro, valuePro), elem in zip(proratedShares.items(), finalArr):
    if(keyPro == elem[2]):
        elem[4] = str(float(elem[4]) * float(valuePro))
        elem[5] = str(float(elem[5]) * float(valuePro))

#Converting the shares to positive if it is negative
for (index, elem) in enumerate(finalArr):
    if( float(elem[3]) * -1 == abs(float(elem[3]))):
        elem[3] = str(float(elem[3]) * -1) + "00"

#Setting up the data to be written
transferOut = []
transferIn = []

for (index, elem) in enumerate(endTup):
    if(float(elem[3]) * -1 == abs(float(elem[3]))):  #short position
        transferIn.append(tradeData[index][0]) #Date
        transferIn.append(elem[1]) #Fund Code
        transferIn.append(elem[2]) #Security
        transferIn.append(elem[2]) #Security
        transferIn.append(finalArr[index][3]) #Shares
        transferIn.append(finalArr[index][4]) #Base Cost
        transferIn.append(finalArr[index][5]) #Native Cost
        transferOut.append(elem[0]) #Date                  
        transferOut.append(tradeData[index][4]) #Fund Code
        transferOut.append(elem[2]) #Security
        transferOut.append(finalArr[index][3]) #Shares
        transferOut.append(finalArr[index][4]) #Base Cost

    else: #long position
        transferOut.append(tradeData[index][0]) #Date
        transferOut.append(elem[1]) #Fund Code
        transferOut.append(elem[2]) #Security
        transferOut.append(finalArr[index][3]) #Shares
        transferOut.append(finalArr[index][4]) #Base Cost
        transferIn.append(tradeData[index][0]) #Date
        transferIn.append(tradeData[index][4]) #Fund Code
        transferIn.append(elem[2]) #Security
        transferIn.append(elem[2]) #Security
        transferIn.append(finalArr[index][3]) #Shares
        transferIn.append(finalArr[index][4]) #Base Cost
        transferIn.append(finalArr[index][5]) #Native Cost

#Slicing the in/out into seperate elements
transferInFinal = []
transferInLength = len(transferIn)
numOfTransfersIn = int(transferInLength / 7) 
numOfLoopsIn = numOfTransfers * 7
arrCounterStartIn = 0
arrCounterEndIn = 7

for i in range(0, numOfTransfersIn):
    transferInFinal.append(transferIn[arrCounterStart:arrCounterEnd])
    arrCounterStartIn = arrCounterStartIn + 7
    arrCounterEndIn = arrCounterEndIn + 7


print(finalArr)
print('----------------')
print(transferIn)
print('----------------')
print(transferInFinal)

"""            
with open("transfer_in.csv","a", newline='') as File:
    finish= csv.writer(File)
    finish.writerows(transferIn)
File.close() """
