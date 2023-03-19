'''
What is Matplotlib ?
Ans: You can easily understand data by visualize it with matplotlib
you can generate histogram,bar,chart, just in few line

'''

import numpy as np


import matplotlib.pylab as plt
print(plt.__version__)

# use numpy to create random data
x= np.linspace(0,10,25)
y=x*x+2
a=plt.plot(x,y,'r') # r is stand for red
#plt.show() # for output visual er jonno eita show use korte hobe
plt.subplot(1,2,1)
plt.plot(x,y,'r--') # r-- means color and line style
plt.subplot(1,2,2)
plt.plot(y,x,'g--')
#plt.show()

fig,axes=plt.subplots(dpi=500)
axes.plot(x,x**2,'r',alpha=.5) # jodi onk line jai tahole alpha diya color kom kora jai
axes.plot(x,x+2,'g')
axes.plot(x,x+3,'b') # we can also use color hex code
#plt.show()
fig,axes=plt.subplots(dpi=500)
axes.plot(x,x+1,'r',linewidth=.5,linestyle='-')
axes.plot(x,x+2,'g',lw=2,linestyle=':') # lw stand for linewidth r line style diye curve er design kora hoi
axes.plot(x,x+3,'b' ,lw=2, linestyle='-.')
line,=axes.plot(x,x+4,color='black' ,lw=2)
line.set_dashes([5,10,15,10])
line,=axes.plot(x,x+5,color='black' ,lw=2)
line.set_dashes([5,10,15,3]) # plot er modde space add kore
#plt.show()

fig,axes=plt.subplots(dpi=500)
axes.plot(x,x+1,'blue',marker='o')  # diffrent type shape add korte chaile
axes.plot(x,x+2,'blue',marker='+',markersize=5)
axes.plot(x,x+3,'blue',marker='s',markerfacecolor="red")
#plt.show()

# set the canvas grid and axis range

fig,axes=plt.subplots(1,2,figsize=(10,5))
axes[0].plot(x,x**2,x**3,lw=2)
axes[0].grid(True) # grid box add kore
axes[1].plot(x,x**2,x**3,lw=2)
axes[1].set_ylim([0,60]) # set limit of y and x axis khota theke suru sesh
axes[1].set_xlim([2,5])

# 2D graphics
n=np.array([0,1,2,3,4,5])
fig,axes= plt.subplots(1,4,figsize=(16,5))
axes[0].set_title("scatter")
axes[0].scatter(x,x+0.25*np.random.rand(len(x)))
axes[1].set_title("step")
axes[1].step(n,n**2,lw=2)
axes[2].set_title("bar")
axes[2].bar(n,n**2,align="center",width=0.5,alpha=0.5)
axes[3].set_title("Fill Between")
axes[3].fill_between(x,x**2,x**3,color="green",alpha=0.5)

# radar chart use in business and data science

fig=plt.figure(figsize=(6,6))
ax=fig.add_axes([0.0,0.0,0.6,0.6,] ,polar=True)
t=np.linspace(0,2*np.pi,100)
ax.plot(t,t,color="blue",lw=2)

# Histogram

n=np.random.rand(100000)
fig,axes=plt.subplots(1,2,figsize=(10,4))
axes[0].set_title("Default Histogram")
axes[0].hist(n)
axes[1].set_title("Cumulative Histogram")
axes[1].hist(n,cumulative=True,bins=5)
# draw  contour image
import matplotlib
import matplotlib.cm as cm # cm= colormap

delta = 0.025
x=np.arange(-3.0,3.0,delta)
y=np.arange(-2.0,2.0,delta)
X,Y=np.meshgrid(x,y)
Z1=np.exp(-X**2,-Y**2)
Z2=np.exp(-(X-1)**2-(Y-1)**2)
Z=(Z1-Z2)*2

fig,ax=plt.subplots()
Cs=ax.contour(X,Y,Z)
ax.clabel(Cs,inline=1,fontsize=10)
ax.set_title("contour map")





plt.show()






