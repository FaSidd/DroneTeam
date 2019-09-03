
def gpsToFeet(x):
    #converting the gps coordinates to km
    x = x*(10000/90)
    #convert kilometers to feet
    ft = 3280.4
    x = x * ft

    return x

def feetToGPS(y):
    #Convert ft to km
    km = y/3280.4
    #Convert km to GPS
    num = 90/10000
    y = num * km

    return y

def dirLenN(coordFt):
    for i in range(0,30):
        coord += 5
        latGPS = feetToGPS(coord)
        return latGPS

def dirLenS(coordFt):
    for j in range(0,30):
        coord -= 5
        latGPS = feetToGPS(coord)
        return latGPS

def dirWidE(coord):
    for k in range(0,10):
        coord -= 5
        lngGPS = feetToGPS(coord)
        return lngGPS

def dirWidW(coord):
    for x in range(0,10):
        coord += 5
        lngGPS = feetToGPS(coord)
        return lngGPS

file = open("gps.txt","w")
lng = 29.720580
lat = -95.341472
lngFt = gpsToFeet(lng)
latFt = gpsToFeet(lat)


'''
def oneCycle(lng,lat):
    count = 0
    while(count <= 5):
'''


for i in range(0,30):
    latFt += 5
    latGPS = feetToGPS(latFt)
#    lngArr.append(lng)
#    latArr.append(latGPS)
#    LngSize = len(lngArr)
#    LatSize = len(latArr)
    file.write(f'longitude: {lng}, latitude: {latGPS:.6f}\n')

file.close()
