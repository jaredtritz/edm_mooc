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
xdata = zip(*idata)[0]
ydata = zip(*idata)[1]

goods = []
bads = []
for dd in idata:
    if (dd[0] == 'N' and dd[1] < 0.5) or (dd[0] == 'Y' and dd[1] >= 0.5):
        goods.append(dd)
    else:
        bads.append(dd)

"""
goods.sort(key = lambda x: x[1])
bads.sort(key = lambda x: x[1])

print 'goods'
for gg in goods: 
    print gg

print 'bads'
for bb in bads:
    print bb
"""

print 'accuracy:', float(len(goods)) / (len(bads) + len(goods))

