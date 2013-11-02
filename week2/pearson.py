from pydoc import help
from scipy.stats.stats import pearsonr
import csv

# correlation
workon = 'regressor.csv'
idata = []
with open(workon, 'rb') as csvfile: 
    datareader = csv.reader(csvfile, delimiter=',')
    for row in datareader:
        idata.append(row)
    iheads = idata[0]
    del idata[0]

#xdata = [float(x) for x in zip(*idata)[0]]
#ydata = [float(x) for x in zip(*idata)[1]]
xdata = map(float, zip(*idata)[0])
ydata = map(float, zip(*idata)[1])

print pearsonr(xdata, ydata)

