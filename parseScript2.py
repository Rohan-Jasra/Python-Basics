import csv

activityFile=open('USB.csv')
activityReader=csv.reader(activityFile)
activityData=list(activityReader)

ctData = []

print(type(activityData[1][11]))
print(type(activityData[1][8]))

for elem in activityData:
    if elem[8].startswith('AUTOFX:') and elem[1] != 'USD':
        ctData.append(elem[0])
        ctData.append(elem[1])
        ctData.append(elem[4])
        ctData.append(elem[8])
        ctData.append(elem[11])
print(ctData)

#ctData.append(elem[0]) - Fund
#ctData.append(elem[1]) - Currency
#ctData.append(elem[4]) - Settle date
#ctData.append(elem[8]) - Info
#ctData.append(elem[11]) - Reference






    

