## Coding created by Samira Kumar 2018.

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')
import pandas as pd
import pylab as pl

import scipy.spatial as spatial
color_map = plt.cm.copper
df = pd.read_csv('insert location of crosses data file')
headers = ["cross_id", "x", "y","pass_end_x", "pass_end_y"]
crosses = pd.DataFrame(df, columns=headers)

points = np.array(crosses[['x','y']])
point_tree = spatial.cKDTree(points)
fig = plt.figure()


pitch = pl.imread('insert location of football pitch')
ax = fig.add_subplot(1,1,1)
ax.imshow(pitch, zorder=0, aspect=None,extent=[-50,105,0,105])

ax.text(-48, 2, '@SamiraK93', fontsize=10)
pl.gca().axison = False

#On click event to plot dynamic graph based on user mouse clicks.

def onclick(event):
    plt.clf()
    global ix, iy

    ix, iy = event.xdata, event.ydata

    global x_test
    ax = fig.add_subplot(1, 1, 1)
    x_test=np.array([ix,iy])

    #Plots the user click as a blue circle
    ax.scatter(event.xdata, event.ydata, s=40,c='b')
    
    #Plots the range of nearest neighbour search as a outer circle with red color
    circle1 = plt.Circle((event.xdata, event.ydata), 2, color='r')
    c=plt.Circle((event.xdata, event.ydata),radius=6,color='g',fill=False,linewidth=2)
    #radius is defined from search range from below line. I.e- 6
    
    ax.add_patch(c)
    fig.canvas.draw()

    pl.gca().axison = False
    plt.hexbin(crosses.pass_end_x[(point_tree.query_ball_point([ix, iy], 6))],
              crosses.pass_end_y[(point_tree.query_ball_point([ix, iy], 6))],extent=[-50, 105, 0, 105],linewidths=0.5,edgecolors='white', gridsize=40,cmap=color_map,mincnt=2)
    
    # 6 represents finding points within 6 unit of cross start location
    
    ax = fig.add_subplot(111)
    ax.text(-48, 2, '@SamiraK93', fontsize=10)

    ax.imshow(pitch, zorder=0,aspect=None, extent=[-50, 105, 0, 105])
    pl.gca().axison = False
    fig.canvas.draw()

    return x_test



cid = fig.canvas.mpl_connect('button_press_event', onclick)

plt.show()
