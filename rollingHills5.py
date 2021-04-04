
import utime
import random
import picodisplay as pcd

width = pcd.get_width()
height = pcd.get_height()

display_buffer = bytearray(width * height * 2)  # 2-bytes per pixel (RGB565)
pcd.init(display_buffer)

pcd.set_backlight(1.0)

pcd.set_pen(77, 83, 135)    
pcd.clear()

pcd.set_pen(0, 255, 0)    
pcd.rectangle(0,110,240,25)

"""Ok what the hell do I want to do here? """

mnds = []

px0 = 30
while px0 < 360:
    py0 = 120
    #px0 = 60
    xwidth = 60
    ymax = 100
    xstart = px0 - random.randrange(int((xwidth/2)*0.75),int(xwidth/2))
    xend = (px0 - xstart) + random.randrange(int((xwidth/2)*0.75),int(xwidth/2))
    mnds.append([px0,py0,ymax,xstart,xend])
    
    while ymax > 0 and xend > 0:
        i = 1
        while i < 2:
            ymax = ymax - 1
            py0 = py0 - 1
            mnds.append([px0,py0,ymax,xstart,xend])
            i = i+1
        diff = random.randrange(0,2)
        xstart = xstart + diff
        xend = xend - (diff + (random.randrange(0,2)))
        
    px0 = px0 + 50
x=0
while True:
    pcd.set_pen(77, 83, 135)    
    pcd.clear()
    pcd.set_pen(0, 255, 0)    
    pcd.rectangle(0,110,240,25)
    mnds2 = []
    for q in (mnds):
        
        px0 = q[0]
        py0 = q[1]
        ymax = q[2]
        
         
        xstart = q[3]
        xend = q[4]
        if xstart == -60:
            xstart = 300        
        if ymax < 60:
            pcd.set_pen(255, 255, 255)  #snow effects
        else:
            pcd.set_pen(0, 255, 0) #greeny green            
        pcd.pixel_span(xstart,py0,xend)
        mnds2.append([px0,py0,ymax,xstart-1,xend])
        
    mnds.clear()    
    mnds = mnds2
    utime.sleep(0.01)
    x=x+1
    pcd.update()
#




