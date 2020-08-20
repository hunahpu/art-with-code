def setup():
    size(800,800,P2D)
    strokeWeight(2.3)

n = 8 #number of squares
t = 0 #time
recording = False;

def draw():
    global t
    global recording 
    background(255)
    stroke(0)
    k = 8 # number of lines per small square
    for i in range(0,k//2):
        for j in range(0,k//2):
            cuadrado(width/k*(i*2+1)+1*1,height/k*(j*2+1)+1*1,width/k,height/k,8)
    t+=0.02
    if(recording and t<PI):
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
