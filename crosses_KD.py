%matplotlib inline

import numpy as np
from sklearn.cluster import MeanShift
import matplotlib.pyplot as plt
import pandas as pd
import pylab as pl
import seaborn
from sklearn.cluster import KMeans
from sklearn import neighbors
import scipy.spatial as spatial

df = pd.read_csv('/Users/samirakumar/Desktop/Samir/Crosses/crosses_updated.csv')
headers = ["cross_id", "x", "y","pass_end_x", "pass_end_y"]
crosses = pd.DataFrame(df, columns=headers)

points = np.array(crosses[['x','y']])
point_tree = spatial.cKDTree(points)
fig = plt.figure()

pitch = pl.imread('/Users/samirakumar/Desktop/Samir/Passes/base.png')
ax = fig.add_subplot(1,1,1)
ax.imshow(pitch, zorder=0, aspect=None,extent=[-50,105,0,105])

ax.text(-48, 2, '@SamiraK93', fontsize=10)
pl.gca().axison = False


def onclick(event):
    plt.clf()
    global ix, iy
    ix, iy = event.xdata, event.ydata
    global x_test
    ax = fig.add_subplot(1, 1, 1)
    x_test=np.array([ix,iy])
    #x_test1 = np.array([[x_test[0], x_test[1]]])

    ax.scatter(event.xdata, event.ydata, s=40,c='b')
    circle1 = plt.Circle((event.xdata, event.ydata), 2, color='r')
    c=plt.Circle((event.xdata, event.ydata),radius=3,color='g',fill=False,linewidth=2)
    ax.add_patch(c)
    fig.canvas.draw()

    pl.gca().axison = False
    ax.scatter(crosses.pass_end_x[(point_tree.query_ball_point([ix, iy], 3))],
             crosses.pass_end_y[(point_tree.query_ball_point([ix, iy], 3))], s=20,c='red')
    #ax.hexbin(crosses.pass_end_x[(point_tree.query_ball_point([ix, iy], 6))],
     #          crosses.pass_end_y[(point_tree.query_ball_point([ix, iy], 6))], gridsize=20,cmap='inferno',extent='scalar')

    #plt.scatter(x_test[0], x_test[1], s=40,c='b')
    ax = fig.add_subplot(111)
    ax.text(-48, 2, '@SamiraK93', fontsize=10)
    ax.imshow(pitch, zorder=0,aspect=None, extent=[-50, 105, 0, 105])
    pl.gca().axison = False

    return x_test



cid = fig.canvas.mpl_connect('button_press_event', onclick)

plt.show()
