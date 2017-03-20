import matplotlib.pyplot as plt
from matplotlib import style
import matplotlib.animation as animation

style.use("ggplot")
fig=plt.figure()
ax=fig.add_subplot(1,1,1)

def animate(i):
    doc_sent=open("/Twitter_Sentiment_Analysis/output/twitter-out.txt").read()
    alltweet_sent=doc_sent.split("\n")
    
    xplot=[]
    yplot=[]
    
    x=0
    y=0
    
    for sent in alltweet_sent[-200:]:
        x=x+1
        if sent=="positive":
            y=y+1
        elif sent=="negative":
            y=y-0.3
        
        xplot.append(x)
        yplot.append(y)
    ax.clear()
    plt.plot(xplot,yplot)
    
ani=animation.FuncAnimation(fig,animate,interval=1000)
plt.show()