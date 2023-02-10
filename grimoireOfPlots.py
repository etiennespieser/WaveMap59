import numpy as np
import matplotlib
from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt

#-- below taken from: https://stackoverflow.com/questions/3899980/how-to-change-the-font-size-on-a-matplotlib-plot
SMALL_SIZE = 10
MEDIUM_SIZE = 12
BIGGER_SIZE = 14

plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
#--
#-- below taken from: https://stackoverflow.com/questions/11367736/matplotlib-consistent-font-using-latex (to use LaTex font by default)
#matplotlib.rcParams['mathtext.fontset'] = 'custom'
#matplotlib.rcParams['mathtext.rm'] = 'Bitstream Vera Sans'
#matplotlib.rcParams['mathtext.it'] = 'Bitstream Vera Sans:italic'
#matplotlib.rcParams['mathtext.bf'] = 'Bitstream Vera Sans:bold'
matplotlib.rcParams['mathtext.fontset'] = 'stix'
matplotlib.rcParams['font.family'] = 'STIXGeneral'
#--
matplotlib.rcParams["figure.dpi"] = 200.0 # change the picture resolution
matplotlib.rcParams['axes.linewidth'] = 0.75
#--
plt.tick_params(
	direction='out',   # specification for the tick direction
	length=3,          # tick length
	width=0.75,        # tick width
	axis='x',          # changes apply to the x-axis
	which='both',      # both major and minor ticks are affected
	bottom=True,       # ticks along the bottom edge are on
	top=False,         # ticks along the top edge are off
	labelbottom=True)  # labels along the bottom edge are on

plt.tick_params(
	direction='out',   # specification for the tick direction
	length=3,          # tick length
	width=0.75,        # tick width
	axis='y',          # changes apply to the x-axis
	which='both',      # both major and minor ticks are affected
	left=True,         # ticks along the bottom edge are on
	right=False,       # ticks along the top edge are off
	labelbottom=True)  # labels along the bottom edge are on
#-------------------------------------------------------------------
plt.close() # for an unknown reason, lines above prompt a window..
#-------------------------------------------------------------------

def createPaintingFrame(windowsWidth, xmin, xmax, ymin, ymax, axisEqual, HV_ratio):
	x_extent = xmax-xmin
	y_extent = ymax-ymin
	
	
	fig = plt.figure()
	
	if axisEqual:
		fix_axes_size_incm(windowsWidth,windowsWidth*float(y_extent)/float(x_extent))
	else:
		fix_axes_size_incm(windowsWidth,windowsWidth*HV_ratio)
	
	ax = plt.gca()
	
	fig.frameon = False
	
	ax.set_xlim(xmin, xmax)
	ax.set_ylim(ymin, ymax)

	
	return fig, ax
	#******************************************************************************
	# Online ressources:
	#******************************************************************************
	# general customisation for figure can be found at:
	# https://matplotlib.org/3.3.2/tutorials/introductory/customizing.html
	# https://www.tutorialspoint.com/matplotlib/matplotlib_quick_guide.htm
	# https://www.tutorialspoint.com/matplotlib/matplotlib_transforms.htm
	# http://www.python-simple.com/python-matplotlib/configuration-axes.php
	# https://stackoverflow.com/questions/44970010/axes-class-set-explicitly-size-width-height-of-axes-in-given-units
	#******************************************************************************

# RQ: 1cm measured at the screen does not correspond to 1cm of printed picture (compare A4 format...) 


from mpl_toolkits.axes_grid1 import Divider, Size
def fix_axes_size_incm(axew, axeh):
    axew = axew/2.54
    axeh = axeh/2.54

    #lets use the tight layout function to get a good padding size for our axes labels.
    fig = plt.gcf()
    ax = plt.gca()
    # fig.tight_layout()
    #obtain the current ratio values for padding and fix size
    oldw, oldh = fig.get_size_inches()
    l = ax.figure.subplotpars.left
    r = ax.figure.subplotpars.right
    t = ax.figure.subplotpars.top
    b = ax.figure.subplotpars.bottom

    #work out what the new  ratio values for padding are, and the new fig size.
    neww = axew+oldw*(1-r+l)
    newh = axeh+oldh*(1-t+b)
    newr = r*oldw/neww
    newl = l*oldw/neww
    newt = t*oldh/newh
    newb = b*oldh/newh

    #right(top) padding, fixed axes size, left(bottom) pading
    hori = [Size.Scaled(newr), Size.Fixed(axew), Size.Scaled(newl)]
    vert = [Size.Scaled(newt), Size.Fixed(axeh), Size.Scaled(newb)]

    divider = Divider(fig, (0.0, 0.0, 1., 1.), hori, vert, aspect=False)
    # the width and height of the rectangle is ignored.

    ax.set_axes_locator(divider.new_locator(nx=1, ny=1))

    #we need to resize the figure now, as we have may have made our axes bigger than in.
    fig.set_size_inches(neww,newh)
    # https://stackoverflow.com/questions/44970010/axes-class-set-explicitly-size-width-height-of-axes-in-given-units 
    

def colorMap():
    # colormap
    def step(x):  # numpy.heaviside is defined from version 1.13.0 of numpy only
        return 1 * (x > 0) + 0.5 * (x == 0)

    m_vec = np.linspace(0, 1, 10000)

    sigma_white = 0.022;  # controls the sharpness of the transition fom yellow to blue,
    sigma_color = 0.15;  # controls the amount of purple and the fading from yellow to blue
    fpos = 1. / 5;

    red_line = step(1. / 3 - m_vec) * (0.3 + 0.7 * 3 * m_vec) + step(m_vec - 1. / 3) - step(m_vec - 1. / 2) + step(
        m_vec - 1. / 2) * np.exp(-(m_vec - 1. / 2) ** 2 / (2. * sigma_white ** 2)) + 0.45 * step(
        1. - fpos - m_vec) * np.exp(-(m_vec - 1. + fpos) ** 2 / (2. * sigma_color ** 2)) + 0.45 * step(
        m_vec - 1. + fpos) * np.exp(-(m_vec - 1. + fpos) ** 2 / (2. * sigma_color ** 2))
    green_line = step(1. / 2 - m_vec) * np.exp(-(m_vec - 1. / 2) ** 2 / (2 * sigma_color ** 2)) + step(
        m_vec - 1. / 2) * np.exp(-(m_vec - 1. / 2) ** 2 / (2 * sigma_color ** 2))
    blue_line = step(1. / 2 - m_vec) * np.exp(-(m_vec - 1. / 2) ** 2 / (2 * sigma_white ** 2)) + step(
        m_vec - 1. / 2) - step(m_vec - 2. / 3) + step(m_vec - 2. / 3) * (1 + 3 * 0.7 * (2. / 3 - m_vec))
    transparency = np.array(np.ones([10000, ]))

    TheseColorsDontRun = np.clip(np.flipud(np.transpose([red_line, green_line, blue_line, transparency])), 0, 1)

    ### Regular wave_map
    wave_map = ListedColormap(TheseColorsDontRun, name='wave_map')

    ### Cold wave_map
    wave_map_cold = ListedColormap(np.flipud(TheseColorsDontRun[:5000, :]), name='wave_map_cold')
    
    ### Cold wave_map_reversed
    wave_map_cold_reversed = ListedColormap(np.flipud(TheseColorsDontRun[:5000, :]), name='wave_map_cold_reversed')

    ### Warm wave_map
    wave_map_warm = ListedColormap(TheseColorsDontRun[5000:, :], name='wave_map_warm')
    
    ### Warm wave_map (reversed)
    wave_map_warm_reversed = ListedColormap(TheseColorsDontRun[5000:, :], name='wave_map_warm_reversed')

    return wave_map, wave_map_cold, wave_map_warm, wave_map_cold_reversed, wave_map_warm_reversed
