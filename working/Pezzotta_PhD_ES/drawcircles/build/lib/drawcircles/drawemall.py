import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter, AutoMinorLocator)

def draw_circle(R, N_points):
    if R is None or N_points is None or R<=0 or N_points<=0:
        raise ValueError("Please insert positive values for the radius and the number of points for the circle.")
    
    theta = np.linspace(0, 2*np.pi, N_points)
    x = R*np.cos(theta)
    y = R*np.sin(theta)
    fig, (ax, ax1) = plt.subplots(1,2,figsize=(12,6))

    # Define major ticks separation on x axis
    xindex_ticks = R
    ax.xaxis.set_major_locator(MultipleLocator(xindex_ticks))
    ax.xaxis.set_minor_locator(MultipleLocator(xindex_ticks/2))

    # Define major ticks separation on y axis
    yindex_ticks = R
    ax.yaxis.set_major_locator(MultipleLocator(yindex_ticks))
    ax.yaxis.set_minor_locator(MultipleLocator(yindex_ticks/2))

    # Ticks' style
    ax.tick_params(which='major',axis='both',right=True,top=True, labelsize=14, pad=7,width=2.5, length=6,direction='in',color='k')
    ax.tick_params(which='minor',axis='both',right=True,top=True, labelsize=14, pad=7,width=1.5, length=4,direction='in',color='k')

    ax.plot(x, y)
    ax.set_xlabel('R', size=18)
    ax.set_ylabel('R', size=18)

    ax.set_title('Empty Circle', size=25)

    # Define major ticks separation on x axis
    xindex_ticks = R
    ax1.xaxis.set_major_locator(MultipleLocator(xindex_ticks))
    ax1.xaxis.set_minor_locator(MultipleLocator(xindex_ticks/2))

    # Define major ticks separation on y axis
    yindex_ticks = R
    ax1.yaxis.set_major_locator(MultipleLocator(yindex_ticks))
    ax1.yaxis.set_minor_locator(MultipleLocator(yindex_ticks/2))

    # Ticks' style
    ax1.tick_params(which='major',axis='both',right=True,top=True, labelsize=14, pad=7,width=2.5, length=6,direction='in',color='k')
    ax1.tick_params(which='minor',axis='both',right=True,top=True, labelsize=14, pad=7,width=1.5, length=4,direction='in',color='k')

    ax1.fill(x, y, c='lightsteelblue', edgecolor='darkblue', linewidth=2)
    ax1.set_xlabel('R', size=18)
    ax1.set_ylabel('R', size=18)

    ax1.set_title('Filled Circle', size=25)
    #plt.legend()
    plt.tight_layout()
    
    return fig

