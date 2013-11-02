
# data = [detector yes, detectory no]
#dataYes = [16.0,7.0]
#dataNo  = [8.0,19.0]
dataYes = [1.0,2.0]
dataNo  = [4.0,141.0]


total = sum(dataYes) + sum(dataNo)
Pa = (dataYes[0] + dataNo[1]) / total

dataYesFreq = sum(dataYes) / total
dataNoFreq = sum(dataNo) / total
detectorYesFreq = (dataYes[0] + dataNo[0]) / total
detectorNoFreq = (dataYes[1] + dataNo[1]) / total
PeYes = dataYesFreq * detectorYesFreq
PeNo = dataNoFreq * detectorNoFreq
Pe = PeYes + PeNo

kappa = (Pa - Pe) / (1 - Pe)
print round(kappa, 3)

