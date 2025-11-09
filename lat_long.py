def lat_longTox_y(lat_long):
    x_y = lat_long
    x_y[0] *= 100000
    x_y[0] = (x_y[0]-4299822)*10

    x_y[1] *= 100000
    x_y[1] = (x_y[1]-7878137)*10

    return x_y

def x_yTolat_long(x_y):
    lat_long= x_y 
    lat_long[0] = (lat_long[0]/10+4299822)
    lat_long[0] /= 100000
    
    lat_long[1] = (lat_long[1]/10+7878137)
    lat_long[1] /= 100000

    return lat_long