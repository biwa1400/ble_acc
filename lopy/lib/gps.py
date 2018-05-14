import L76GNSS

gps = L76GNSS.L76GNSS(timeout=60,sda='P22', scl='P21')
print(gps.coordinates(debug=True))
