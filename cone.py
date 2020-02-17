import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib
matplotlib.use('TkAgg') # <-- THIS MAKES IT FAST!
import numpy as np


def f(x, y):
    return np.sqrt((x*x + y*y)/((0.5*.5)/(65*65)))



def drawCone():
    x = np.linspace(-1.5, 1.5, 100)
    y = np.linspace(-1.5, 1.5, 100)

    X, Y = np.meshgrid(x, y)

    Z = f(X, Y) - 130
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    #ax.contour3D(X, Y, Z, 100, cmap='binary')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z');


    xx, yy = np.meshgrid(range(10), range(10))
    xx = xx - 5;
    yy = yy - 5;
    normal = np.array([0, 0, 1])
    d = -5;
    zz = (-normal[0] * xx - normal[1] * yy - d) * 1. /normal[2];

    d = -70;
    zz2 = (-normal[0] * xx - normal[1] * yy - d) * 1. /normal[2];


    ax.plot_surface(X, Y, Z,alpha=1)
    ax.plot_surface(xx, yy, zz,alpha=.3)
    ax.plot_surface(xx, yy, zz2,alpha=.3)



    voxelsx,voxelsy,voxelsz = make3DVoxelSpace();
    dist=calculateDistance(voxelsx,voxelsy,voxelsz)
    for i in range(len(voxelsx)):
        dist.append([255,0,0]);

    ax.scatter(voxelsx,voxelsy,voxelsz,s=.5);
    # for i in range(len(voxelsx)):
    #     ax.scatter(voxelsx[i],voxelsy[i],voxelsz[i],s=.5)

    plt.show()

    pass;


def make3DVoxelSpace():
    dimx = int(2.5/.5);
    dimy = int(2.5/.5);
    dimz = int(80/.5);
    x = []
    y = []
    z = []

    for a in range(dimx):
        for b in range(dimy):
            for c in range(dimz):
                x.append(a-2);
                y.append(b-2);
                z.append(c-40);

    return x,y,z




def calculateDistance(xlist,ylist,zlist):
    colorList = [];

    return colorList;


def distance2color(dist):
    return 0;

def zone2color(xlist,ylist,zlist):
    colorList = [];

    return colorList;


drawCone();
