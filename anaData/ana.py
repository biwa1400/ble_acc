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
	
	
	
def testHeatMap(heat_lats, heat_lngs, weights):
	from gmplot import gmplot
	gmap = gmplot.GoogleMapPlotter(62.394116, 17.283450, 13)

	i = 0
	weights = uniformValue(weights)
	for weight in weights:
		if i%3 == 0:
			valueString = str(hex(abs(int((1-weight)**7*255))))[2:4]
			gmap.scatter((heat_lats[i],), (heat_lngs[i],), '#ff'+valueString*2, size=6, marker=False)
		i+=1

	gmap.draw("heatMap.html")
	os.system(".\heatMap.html")	

def testGoogleMap(points):
	from gmplot import gmplot
	# Place map
	gmap = gmplot.GoogleMapPlotter(62.394116, 17.283450, 13)

	# Polygon
	golden_gate_park_lats, golden_gate_park_lons = zip(*points)
	gmap.plot(golden_gate_park_lats, golden_gate_park_lons, 'cornflowerblue', edge_width=10)

	# Scatter points
	top_attraction_lats, top_attraction_lons = zip(*[
		(37.769901, -122.498331),
		(37.768645, -122.475328),
		(37.771478, -122.468677),
		(37.769867, -122.466102),
		(37.767187, -122.467496),
		(37.770104, -122.470436)
		])
	gmap.scatter(top_attraction_lats, top_attraction_lons, '#3B0B39', size=40, marker=False)

	# Marker
	hidden_gem_lat, hidden_gem_lon = 37.770776, -122.461689
	gmap.marker(hidden_gem_lat, hidden_gem_lon, 'cornflowerblue')

	# Draw
	gmap.draw("my_map.html")
	os.system(".\my_map.html")
	
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
	
		
	
		
	
	
def dataProcess():
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
	#print(acc_x_diff)
	#plt.plot(acc_x)
	#plt.plot(acc_x_diff)
	testHeatMap(heat_lats, heat_lngs, acc_z_diff)
	

		
		
	
if __name__=='__main__':
	#uniformValue([1,2,3])
	dataProcess()
	#testGoogleMap()
	#dataProcess()
	#print(str(hex(254))[2:4])
