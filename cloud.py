##Adding in blinking... somehow.
##shit... bring in the rainbow
## tiny fucking clouds
## added in to test git

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

#define tiny clouds and set them into list defined x/y/d
class Cloud:
    def __init__(self, x, y, d):
        self.x = x
        self.y = y
        self.d = d

#move tiny clouds
def drcld(x,y):
    pcd.set_pen(200, 200, 200)
    pcd.circle(x, y, 10)
    pcd.circle(x+15, y, 15)
    pcd.circle(x+30, y, 10)

#big cloud. Bring in mood and do blink, colour etc. 
def babyCloud(coreX, coreY, blinkrate):
    xshift = 30
    yshift = 10
    xeye = 11
    yeye = 10
    xmth = 30
    eyeDiameter = 7
    global bk
    bk = blinkrate
    
    pcd.set_pen(250, 250, 250)
    pcd.circle(int(coreX), int(coreY),40)
    pcd.circle(int(coreX) + xshift, int(coreY) + yshift,25)
    pcd.circle(int(coreX) - xshift, int(coreY) + yshift,25)
    # eyes
    pcd.set_pen(0, 0, 0)
    pcd.circle(int(coreX) + xeye, int(coreY) - yeye, eyeDiameter)
    pcd.circle(int(coreX) - xeye, int(coreY) - yeye, eyeDiameter)

    #smile variables
    smiledepth = 0
    smiledepth = int(coreY) + 10
    flip = 0 
    while xmth > 0:
        smilestart = coreX - xmth
        smileend = xmth * 2
        pcd.pixel_span(int(smilestart), int(smiledepth), int(smileend))
        xmth -= int(flip)
        flip = flip + 0.40
        if flip == 3:
            flip = 1
        smiledepth += 1
    #masks
    pcd.set_pen(255, 255, 255)
    bk = bk + random.randint(1,10)
    if bk > 20:
        pcd.rectangle(int(coreX - (xeye*2)), int(coreY - yeye) + 3, int(xeye *4), yeye) 
        pcd.rectangle(int(coreX - (xeye*2)), int(coreY - (yeye*2)), int(xeye *4), yeye-3)
        bk = -20
    # mouth. this is shit as mouth variables are reset by making the mouth. 
    if random.randint(1,100) > 95:
        pcd.set_pen(255, 255, 255)
        pcd.rectangle(int(coreX) - 30, int(coreY) + 15, 60, 10)
    
    
# set rainbow. Rough af but never mind    
def ranbw():
    pcd.set_pen(250, 0, 0)
    pcd.circle(120,135,120)
    pcd.set_pen(255, 126, 0)
    pcd.circle(120,135,110)
    pcd.set_pen(255, 240, 0)
    pcd.circle(120,135,100)
    pcd.set_pen(0, 240, 0)
    pcd.circle(120,135,90)
    pcd.set_pen(0, 0, 200)
    pcd.circle(120,135,80)
    pcd.set_pen(169, 0, 240)
    pcd.circle(120,135,70)
    pcd.set_pen(225, 0, 225)
    pcd.circle(120,135,60)
    pcd.set_pen(140, 190, 242)
    pcd.circle(120,135,50)

def mssg(msgPsh):
    if msgPsh == 1:
        msgTxt = "Hi Gareth!"
    elif msgPsh == 2:
        msgTxt = "You're doing an  awesome \n job!"
    pcd.set_pen(0, 0, 0)
    pcd.rectangle(5,5,230,125)
    pcd.set_pen(255, 255, 255)
    pcd.rectangle(10,10,220,115)
    pcd.set_pen(0, 0, 0)
    pcd.text(msgTxt, 20, 20, 200,3)
    pcd.set_pen(251, 67, 72)
    
    heartx = 180
    hearty = 70
    pcd.circle(heartx, hearty, 10)
    pcd.circle(heartx + 15, hearty,10)
    heartx = heartx - 10
    hearty = hearty + 5
    heartlen = 35
    while heartlen > 0:
        pcd.pixel_span(heartx,hearty,heartlen)
        heartx = heartx + 1
        heartlen = heartlen - 2
        hearty = hearty + 1
    pcd.update()
    utime.sleep(5)   

    
coreX = width/2
coreY = height/2
blinkrate = 0

cld = []
msgPsh = 0

#create tiny clouds
for p in range(0,10):
    px = random.randint(-300,400)
    py = random.randint(0,135)
    pd = random.randint(0,1)
    cld.append(Cloud(px, py, pd))
    
#main loop
while True:
    pcd.set_pen(140, 190, 242)    #sky colour?
    pcd.clear()
    ranbw()
    dr = 1
    
    for q in cld:
        if q.d == 0:
            dr = dr *-1
        if q.x < -40:
            q.x = random.randint(260,400)
            q.y = random.randint(10,120)
        if q.x > 300:
            q.x = random.randint(-100,-40)
            q.y = random.randint(10,120)
        else:
            q.x = q.x - dr
            q.y = q.y + random.randint(-1,1)
        drcld(int(q.x),int(q.y))
        #print(str(q.d))
    babyCloud(coreX, coreY, blinkrate)
    blinkrate = bk
    pcd.update()    
    utime.sleep(0.1)
    if msgPsh > 0:
        mssg(msgPsh)
        msgPsh = 0
    if pcd.is_pressed(pcd.BUTTON_B):
        msgPsh = 1
    if pcd.is_pressed(pcd.BUTTON_A):
        msgPsh = 2
   # if pcd.is_pressed(pcd.BUTTON_B):
   #     pcd.set_pen(0, 0, 0)
   #     pcd.rectangle(10,10,230,120)
   #     utime.sleep(10)
        
        
    
    
    
    


