def setup():
    global chormatic
    size(800,800,P2D)
    strokeWeight(2.3)
    if(chromatic):
        blendMode(ADD)

n = 8
t = 0 #time
chromatic = False
def draw():
    global t
    global chromatic
    background(255)
    ##translate(width/2,height/2)
    stroke(0)
    k = 8
    if(chromatic):
        fr=[color(255,0,0),color(0,255,0),color(0,0,255)]
        for l in range(3):
            stroke(fr[l])
            for i in range(0,k//2):
                for j in range(0,k//2):
                    cuadrado(width/k*(i*2+1)+1*1,height/k*(j*2+1)+1*1,width/k,height/k,8)
    else:
        for i in range(0,k//2):
            for j in range(0,k//2):
                cuadrado(width/k*(i*2+1)+1*1,height/k*(j*2+1)+1*1,width/k,height/k,8)
    t+=0.02
    if(t<PI):
        saveFrame("frame###.png")
    
def cuadrado(x,y,w,h,n):
    global t
    push()
    translate(x,y)
    for i in range(n+1):
        line(-i*w/n,-h+sin(t+0.05*i)*sin(t+0.05*i)*h,-i*w/n,+sin(t+0.05*i)*sin(t+0.05*i)*h)
        line(i*w/n,h-sin(t+0.05*i)*sin(t+0.05*i)*h,i*w/n,-sin(t+0.05*i)*sin(t+0.05*i)*h)
        line(-w+sin(t+0.05*i)*sin(t+0.05*i)*h,-h/n*i,+sin(t+0.05*i)*sin(t+0.05*i)*h,-h/n*i)
        line(w -sin(t+0.05*i)*sin(t+0.05*i)*h,h/n*i,-sin(t+0.05*i)*sin(t+0.05*i)*h,h/n*i)
    pop()
