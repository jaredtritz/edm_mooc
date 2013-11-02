import csv
import numpy as np

workon = 'classifier.csv'
idata = []
with open(workon, 'rb') as csvfile: 
    datareader = csv.reader(csvfile, delimiter=',')
    for row in datareader:
        idata.append(row)
    iheads = idata[0]
    del idata[0]

idata = [[xx[0], float(xx[1])] for xx in idata]
#idata = [['Y',0.3], ['Y',0.3], ['N',0.7], ['N',0.7]]
xdata = zip(*idata)[0]
ydata = zip(*idata)[1]

TP = []
TN = []
FP = []
FN = []
for dd in idata:
    if dd[0] == 'Y' and dd[1] >= 0.5:
        TP.append(dd); continue
    if dd[0] == 'N' and dd[1] < 0.5:
        TN.append(dd); continue
    if dd[0] == 'N' and dd[1] >= 0.5:
        FN.append(dd); continue
    if dd[0] == 'Y' and dd[1] < 0.5:
        FP.append(dd); continue

TP.sort(key = lambda x: x[1])
TN.sort(key = lambda x: x[1])
FP.sort(key = lambda x: x[1])
FN.sort(key = lambda x: x[1])

# kappa
total = float(len(TP) + len(TN) + len(FP) + len(FN))
Pa = (len(TP) + len(TN)) / total
dataYesfreq = (len(TP) + len(FN)) / total
dataNofreq = (len(TN) + len(FP)) / total
detYesfreq = (len(TP) + len(FP)) / total
detNofreq = (len(TN) + len(FN)) / total
PeYes = dataYesfreq * detYesfreq
PeNo = dataNofreq * detNofreq
Pe = PeYes + PeNo

kappa = (Pa - Pe) / (1 - Pe)
print 'Cohens Kappa', round(kappa, 3)
print 'Precision' , float(len(TP)) / (len(TP) + len(FP))
print 'Recall' , float(len(TP)) / (len(TP) + len(FN))


