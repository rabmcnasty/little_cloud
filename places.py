import time
import utime
import random
import picodisplay as pcd
width = pcd.get_width()
height = pcd.get_height()

display_buffer = bytearray(width * height * 2)  # 2-bytes per pixel (RGB565)
pcd.init(display_buffer)

pcd.set_backlight(0.5)

pcd.set_pen(77, 83, 135)    
pcd.clear()
pcd.update()


mst = {(-8,58, 'St. Kilda'),(-7,58, 'Isle of Lewis'),(-6,58, 'The Minch'),(-5,58, 'Ledmore'),(-4,58, 'Bora'),(-3,58, 'Cromarty'),(-2,58, 'Cromarty'),(-1,58, 'Cromarty'),(0,58, 'Cromarty'),(1,58, 'Cromarty'),
        (-8,57, 'Hebridies'),(-7,57, 'Castlebay'),(-6,57, 'Rum'),(-5,57, 'Invergarry'),(-4,57, 'Cairngorms'),(-3,57, 'Crathie'),(-2,57, 'Stonehaven'),(-1,57, 'Forties'),(0,57, 'Forties'),(1,57, 'Forties'),
        (-8,56, 'Malin'),(-7,56, 'Malin'),(-6,56, 'Jura'),(-5,56, 'Firth of Clyde'),(-4,56, 'Glasgow'),(-3,56, 'Edinburgh'),(-2,56, 'Berwick'),(-1,56, 'Forties'),(0,56, 'Forties'),(1,56, 'Forties'),
        (-8,55, 'Letterkenny'),(-7,55, 'Derry'),(-6,55, 'Glenarm'),(-5,55, 'Ballantrae'),(-4,55, 'Douglas'),(-3,55, 'Carlisle'),(-2,55, 'Newcastle'),(-1,55, 'Tyne'),(0,55, 'Dogger'),(1,55, 'Dogger'),
        (-8,54, 'Carrick-on-Shannon'),(-7,54, 'Castleblaney'),(-6,54, 'Dundalk Bay'),(-5,54, 'Calf of Man'),(-4,54, 'Irish Sea'),(-3,54, 'Morcombe'),(-2,54, 'Skipton'),(-1,54, 'York'),(0,54, 'Flamborough Head'),(1,54, 'Dogger'),
        (-8,53, 'Lough Derg'),(-7,53, 'Athy'),(-6,53, 'Wicklow'),(-5,53, 'Llyn'),(-4,53, 'Ffestiniog'),(-3,53, 'Wrexham'),(-2,53, 'Stoke'),(-1,53, 'Nottingham'),(0,53, 'Boston'),(1,53, 'The Wash'),
        (-8,52, 'Cork'),(-7,52, 'Hook Head'),(-6,52, "St George's Channel"),(-5,52, 'Fishguard'),(-4,52, 'Llanymddyfri'),(-3,52, 'Talgarth'),(-2,52, 'Cheltenham'),(-1,52, 'Oxford'),(0,52, 'Greenwich'),(1,52, 'Ipswich'),
        (-8,51, 'Fastnet'),(-7,51, 'Fastnet'),(-6,51, 'Lundy'),(-5,51, 'Bristol Channel'),(-4,51, 'Barnstaple'),(-3,51, 'Taunton'),(-2,51, 'Sailsbury'),(-1,51, 'Southampton'),(0,51, 'Brighton'),(1,51, 'Folkstone'),
        (-8,50, 'Sole'),(-7,50, 'Sole'),(-6,50, 'Scilly'),(-5,50, 'Lizard Point'),(-4,50, 'Plymouth'),(-3,50, 'Portland'),(-2,50, 'Aldernay'),(-1,50, 'Wight'),(0,50, 'Wight'),(1,50, 'Dover')
    }

x = -8
y = 54
maxy = 58
miny = 50
maxx = 1
minx = -8
t = 0

while t < 10:
    pcd.set_pen(77, 83, 135) 
    pcd.clear()
    # start, all directions
    compass = [1,2,3,4,5,6,7,8]
    # then remove options if at edge
    remv = []
    if x == maxx:
        remv.extend([2,3,4])
    if x == minx:
        remv.extend([8,7,6])
    if y == maxy:
        remv.extend([8,1,2])
    if y == miny:
        remv.extend([6,5,4])
    remv = list(dict.fromkeys(remv)) #remove duplicates
    for r in remv:
        compass.remove(r)
    randwind = random.randint(0,len(compass)-1)
    wind = compass[randwind]
    
    if wind == 1:
        x = x
        y = y+1
    elif wind == 2:
        x = x+1
        y = y+1
    elif wind == 3:
        x = x+1
        y = y
    elif wind == 4:
        x = x+1
        y = y-1
    elif wind == 5:
        x = x
        y = y-1
    elif wind == 6:
        x = x-1
        y = y-1
    elif wind == 7:
        x = x-1
        y = y
    elif wind == 8:
        x = x-1
        y = y+1
    
    locale = 'fuck!!'
    for q in mst:
        if q[0] == x and q[1] == y:
            locale = q[2]
    print(len(locale))
    pcd.set_pen(255,255,255)
    fntsz = 3
    if len(locale)>12:
        fntsz = 2
    else:
        fntsz = 3
    #print(width - len(locale))
    print((width/2) - (len(locale)/2))
    #assume at 3 that one char =
    pcd.text(locale, int((width/2) - ((len(locale)*17)/2)), 20, 200,fntsz)
    #pcd.text(locale, 20, 20, 200,3)
    pcd.update()   
    utime.sleep(5)    
    
    
    
