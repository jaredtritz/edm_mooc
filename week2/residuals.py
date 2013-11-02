import csv
import numpy as np

# RMSE error
workon = 'regressor.csv'
idata = []
with open(workon, 'rb') as csvfile: 
    datareader = csv.reader(csvfile, delimiter=',')
    for row in datareader:
        idata.append(row)
    iheads = idata[0]
    del idata[0]

idata = [[float(s) for s in xs] for xs in idata]
xdata = zip(*idata)[0]
ydata = zip(*idata)[1]

square_diffs = [(x[0] - x[1])**2 for x in idata]
abs_diffs = [abs(x[0] - x[1]) for x in idata]

print 'Root Mean Square error', np.sqrt(np.mean(square_diffs))
print 'Mean Absolut Difference error', np.mean(abs_diffs)

