import csv
import os
import matplotlib.pyplot as plt

def readData():
	csv_file = csv.reader(open('lopy_acc.csv','r'))
	return csv_file

def uniformValue(data):
	maxValue = max(data)
	minValue = min(data)
	result = []
	for i in data:
		result.append((i - minValue)/maxValue) 
	return result
	
	
	
def plotMap(heat_lats, heat_lngs, weights, level):
	from gmplot import gmplot
	gmap = gmplot.GoogleMapPlotter(62.394116, 17.283450, 13)

	i = 0
	weights = uniformValue(weights)
	for weight in weights:
		if i%3 == 0:
			valueString = str(hex(abs(int((1-weight)**level*255))))[2:4]
			gmap.scatter((heat_lats[i],), (heat_lngs[i],), '#ff'+valueString*2, size=6, marker=False)
		i+=1

	gmap.draw("map.html")
	os.system(".\map.html")	
	
def diffFun(data,step):
	result = []
	oldValue = None
	i = 0
	for dataUnit in data:
		if oldValue != None:	
			if i % step == 0:
				result.append((float(dataUnit) - float(oldValue))/float(step))
				oldValue = dataUnit
		else:
			oldValue = dataUnit
		i += 1
	return result
	
		
	
		
	
	
def dataProcess(level):
	data = readData()
	locationArray = []
	accArray = []
	i = 0
	for dataUnit in data:
		if i%1 == 0 and i != 0 and i < 60000 and i > 0:
			locationArray.append((float(dataUnit[5]),float(dataUnit[4])))
			accArray.append((float(dataUnit[1]),float(dataUnit[2]),float(dataUnit[3])))
		i += 1
	acc_x,acc_y,acc_z = list(zip(*accArray))
	heat_lats,heat_lngs = list(zip(*locationArray))
	acc_x_diff = diffFun(acc_x,1)
	acc_y_diff = diffFun(acc_y,1)
	acc_z_diff = diffFun(acc_z,1)
	plotMap(heat_lats, heat_lngs, acc_z_diff,level)
	

		
		
	
if __name__=='__main__':
	import sys
	dataProcess(int(sys.argv[1]))
