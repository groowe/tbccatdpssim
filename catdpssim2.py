# simulation of catdps
# counting how much dps it does
# recording best one and showing it as replay during next (or just replay)




import pygame
import time

def gettime():
    s = time.time() * 1000
    return s

def printtext(string = '0',x =0 ,y = 0):
    if type(num) != str:
        num = str(num)
    if type(x) != int:
        x = int(x)
    if type(y) != int:
        y = int(y)

    textsurface = myfont.render(num,False,white)
    gameDisplay.blit(textsurface,(x,y))


def printdmg(num = '0'):
    if type(num) != str:
        num = str(num)
    printtext(num,0,0)
#    textsurface = myfont.render(num,False,white)
#    gameDisplay.blit(textsurface,(0,0))

def printtotal(num = '0'):
    if type(num) != str:
        num = str(num)
#    textsurface = myfont.render(num,False,white)
    y = 0
    x = display_width - (20 * len(num))
    printtext(num,x,y)
#    gameDisplay.blit(textsurface,(x,y))


def printdps(num = '0'):
    global dmgstarted
    global currentdps
    now = time.time
    if type(num) != str:
        num = str(num)
    if lastdmg != 0 and (lastdmg + 5) < time.time():
        num = str(currentdps)
    elif dmgstarted != 0:
        now = time.time()
        timed = (now - dmgstarted)
        dps = int((totaldmg / timed) *100)
        currentdps = dps/100
        num= str(currentdps)
    print((lastdmg+5)<time.time())
#    textsurface = myfont.render(num,False,white)
    y = 30
    x = display_width - (20 * len(num))
    printtext(num,x.y)
#    gameDisplay.blit(textsurface,(x,y))

def damage(name = None):
    global totaldmg
    global lastdmg
    global ripticking
    global autostart
    global autoattackswing
    mangle()
    dmg = 0
    if name == "rip":
        rip(True)
    if name == "mangle":
        mangle(True)
    dmg+=rip()
    if dmg != 0:
        lastdmg = time.time()
        autostart = lastdmg
    if lastdmg+5<= time.time():
        totaldmg = 0
        dmgstarted = time.time()
    if 0 < autostart and 1 < autoattackswing +1<=time.time():
        dmg +=300
        autoattackswing = time.time()
        print(True) 
    totaldmg += dmg
    return dmg


def mangle(applied = False):
    global mangleapplied
    global mangletime
    global totaldmg
    global lastdmg
    global dmgstarted
    if applied == True:
        if mangletime+1 <= time.time():
            mangleapplied = True
            mangletime = time.time()
            lastdmg = mangletime
            if dmgstarted+5<=lastdmg:
                dmgstarted = lastdmg
            mangledmg = 1000
            totaldmg += mangledmg

    if mangletime+6 < time.time():
        mangleapplied = False


def rip(applied = False):
    global ripticking
    global ripapplied
    global riptick
    global riptickm
    global dmgstarted
    global mangleapplied
    dmg = 0
    if applied == True:
        ripticking = True
        ripapplied = time.time()
        if lastdmg+5<= ripapplied:
            dmgstarted = ripapplied
        riptickm = 1
    x = time.time() - ripapplied
    if ripticking == True:
        if  x >= riptick*riptickm:
            dmg+=300
            riptickm+=1
        if riptickm > 6:
            ripticking = False
            riptickm = 1
    if mangleapplied:
        dmg = dmg*1.3
    return dmg


if __name__ == "__main__":
    pygame.init()

    # graphical variables

    display_width = 1067
    display_height = 600
    disp = (display_width,display_height)
    gameDisplay = pygame.display.set_mode(disp)
    backgroundpic = "1067x600arch.jpg"
    backg = pygame.image.load(backgroundpic).convert_alpha()

    black = (0,0,0)
    white = (255,255,255)
    red = (255,0,0)
    green = (0,255,0)
    blue = (0,0,255)
    gold = (212,175,55)

    # font

    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS',30)

    ### combat variables ###
    combatstart = 0 # dmgstarted
    combatend = 0 # lastdmg
    
    currentdps = 0

    totaldmg = 0
    
    # autoattack
    attackswing = 0

    # rip
    ripticking = False
    ripapplied = 0
    riptick = 2
    riptickm = 1

    # mangle

    mangledebuff = False
    manlgemultibleed = 1.3
    mangletime = 0

    clock = pygame.time.Clock()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    # rip
                    pass
                if event.key == pygame.K_w:
                    # mangle
                    pass
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        clock.tick(10)
    
    pygame.quit()
    quit()
# map:
# 
