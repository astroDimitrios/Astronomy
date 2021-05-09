import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from pathlib import Path
import imageio

class CA:
    """ Creates the CA
    """

    def __init__(self, grid, edge_rule, verbose=False, plot=False, plot3D=False, 
                gif=False, gif3D=False, dpi=100, history=False, **kwargs):
        """ Initialises the CA
        """
        self.grid_edge(grid, edge_rule)
        self.t = 0
        self.verbose = verbose
        if plot:
            self.plot = plot
            self.dpi = dpi
            self.plot_setup(kwargs)
            self.gif = gif
            if gif:
                self.filenames = [] # only need this if giffing!!!!!
            self.plot_state(self.cmap, self.norm, self.verbose, self.gif)
        else:
            gif = False # sanity check make gif false
        if plot3D:
            self.plot3D = plot3D
            self.dpi = dpi
            self.plot_setup3D(kwargs)
            self.gif3D = gif3D
            self.Z = kwargs['Z'] 
            if gif:
                self.filenames3D = []
            self.plot_state3D(self.plot_func3D, self.verbose, self.gif3D)
        else:
            gif3D = False
        if history:
            self.past = True
            self.history = np.zeros(self.grid.shape)

    def grid_edge(self, grid, edge_rule):
        ''' Adds the edge to the grid
            using the defined boundary rule

            Only ghost cells of 0 are currently implemented
        '''
        if not edge_rule == 'ghost':
            raise ValueError('Only edge_rule ghost implemented.')
        self.edge_rule = edge_rule
        self.grid = np.pad(grid, (1, 1), 'constant', constant_values=(0,0))
        self.size = len(grid)

    def state(self):
        """ Return grid - no edge
        """
        return self.grid[1:self.size+1, 1:self.size+1]

    def print_state(self):
        """ Print current state
        """
        print(f"Timestep - {self.t:>4}")
        print(self.grid[1:self.size+1, 1:self.size+1])

    def print_full_state(self):
        """ Print current state with edge cells
        """
        print(f"Timestep - {self.t:>4}")
        print(self.grid)

    def get_neighbours(self, i, j, d):
        """ Get neighbours of i, j within d index away
        """
        n = self.grid[i-d:i+d+1, j-d:j+d+1].flatten()
        n = np.hstack((n[:len(n)//2],n[len(n)//2+1:] ))
        return n

    def evolve(self, rule, **kwargs):
        """ Move forward one timestep
        """
        new_grid = np.zeros_like(self.grid)
        if self.edge_rule == 'ghost':
            for index, val in np.ndenumerate(self.grid):
                i, j = index
                if 0 not in index and self.size+1 not in index:
                    new_grid[i, j] = rule(i, j, val, self.get_neighbours(i, j, 1), self.history, **kwargs)
        new_history = np.where(new_grid==self.grid, self.history+1, 1)
        self.grid = new_grid
        self.history = new_history
        self.t += 1

    def mevolve(self, rule, steps, **kwargs):
        ''' Evolve n steps using the evolve() function above
        '''
        for i in range(steps):
            self.evolve(rule, **kwargs)
            if self.plot:
                self.plot_state(self.cmap, self.norm, self.verbose, self.gif)
            if self.plot3D:
                self.plot_state3D(self.plot_func3D, self.verbose, self.gif3D)
        

    def plot_setup(self, kwargs):
        ''' Sets up directory for saving images
            Ensures colourmap and norm exist
        '''
        if not all (key in kwargs for key in ('fp', 'cmap', 'norm')):
            raise NameError('Plot is True but the filepath, colourmap, or norm have not been defined.')
        if not isinstance(kwargs['fp'], str):
            raise ValueError('File path for saving plots must be a string')
        self.fp = kwargs['fp']
        self.cmap = kwargs['cmap']
        self.norm = kwargs['norm']
        if self.verbose:
            print(f"Files saving to - {self.fp}/")
        Path(self.fp).mkdir(parents=True, exist_ok=True)

    def plot_setup3D(self, kwargs):
        ''' Sets up directory for saving 3D images
            Ensures colourmap and norm exist
        '''
        if not all (key in kwargs for key in ('fp', 'colors3D', 'plot_func3D')):
            raise NameError('Plot3D is True but the filepath, colors3D, or 3D plot function have not been defined.')
        if not isinstance(kwargs['fp'], str):
            raise ValueError('File path for saving 3D plots must be a string')
        # need check for colours being list of strings
        self.fp3D = kwargs['fp']+'/3D'
        if self.verbose:
            print(f"Files saving to - {self.fp3D}/")
        Path(self.fp3D).mkdir(parents=True, exist_ok=True)
        self.colors3D = kwargs['colors3D']
        self.plot_func3D = kwargs['plot_func3D']

    def plot_state(self, colours, norm, verbose, gif):
        ''' Plot the current state
        '''
        fig = plt.figure(num=self.t, figsize=(10, 10))
        ax = fig.add_subplot(111, label="ax")
        ax.imshow(self.state(), cmap=colours, norm=norm, interpolation='nearest', origin='lower')
        ax.axis('off')
        if verbose:
            print(f'Saving figure for timestep - {self.t:>4}')
        image_path = self.fp+f'/{self.t}.png'
        if gif:
            self.filenames.append(image_path)
        plt.savefig(image_path, dpi=self.dpi)
        plt.close()

    def plot_state3D(self, plot_func3D, verbose, gif3D):
        ''' Plot the current state 3D
        '''
        if verbose:
            print(f'Saving 3D figure for timestep - {self.t:>4}')
        image_path = plot_func3D(self.t, self.state(), self.Z[1:ln+1, 1:ln+1], self.colors3D, self.fp3D, self.dpi)
        if gif3D:
            self.filenames3D.append(image_path)

    def make_gif(self):
        ''' Makes a gif with all plotted states
        '''
        if self.gif:
            gif_path = self.fp+'/'+self.fp.split('/')[-1]+'.gif'
            if self.verbose:
                print(f'Saving gif to - {gif_path}')
            with imageio.get_writer(gif_path, mode='I') as writer:
                for filename in self.filenames:
                    image = imageio.imread(filename)
                    writer.append_data(image)
        else:
            raise ValueError('CA initiated with gif=False (default)')

    def make_gif3D(self):
        ''' Makes a 3D gif with all plotted states
        '''
        if self.gif3D:
            gif_path = self.fp+'/3D/'+self.fp.split('/')[-1]+'-3D.gif'
            if self.verbose:
                print(f'Saving 3D gif to - {gif_path}')
            with imageio.get_writer(gif_path, mode='I') as writer:
                for filename in self.filenames3D:
                    image = imageio.imread(filename)
                    writer.append_data(image)
        else:
            raise ValueError('CA initiated with gif3D=False (default)')

# custom fire rule
def fire_rule_Z_snow(i, j, val, n, history, **kwargs):
    """ Fire rule

    0 - alive chance of lightning or burn due to neighbours
    1 - turn to dead (2)
    2 - dead and stay dead
    """
    p_burn, p_lightning, terrain, d, p_water, s_level, p_snow, p_born = kwargs.values()
    if val == -2:
        return -2 # keep snow
    if val == -1:
        return -1 # if it's water keep water
    if val == 2:
        if np.any(n==1):
            return 2 # if neighbours burning keep dead
        elif history[i][j] > 12 and random() < p_born:
            return 0 # a tree is born with p_born after 12 dead timesteps
        else:
            return 2 # keep dead tree
    if val == 1:
        return 2 # dead tree
    if random() < p_lightning:
        return 1 # burning
    # vals, counts = np.unique(n, return_counts=True) # values, counts
    nw = terrain[i-d:i+d+1, j-d:j+d+1].flatten()
    water = np.count_nonzero(nw == 0)
    d = int(d*1.3)
    nw = terrain[i-d:i+d+1, j-d:j+d+1].flatten()
    snow = np.count_nonzero(nw > s_level)
    opts = {-2: snow,
            -1: water}
    for i in [0, 1, 2]:
        opts[i] = np.count_nonzero(n == i)
    # print(opts)
    if not opts[-1]:
        w_supress = 1
    else:
        w_supress = opts[-1]*p_water
    if not opts[-2]:
        s_supress = 1
    else:
        s_supress = opts[-2]*p_snow
    if random() < p_burn*opts[1]/w_supress/s_supress:
        return 1 # burning
    return 0 # tree is alive

def forest_3D(t, state, terrain, colours, file_path, dpi):
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.azim = -60-t # def -60
    ax.dist = 7.5 # def 10
    ax.elev = 30+t # def 30
    lX = state.shape[0]
    X = np.arange(lX)
    Y = np.arange(lX)
    X, Y = np.meshgrid(X, Y)
    color_map = np.empty(X.shape, dtype=np.dtype('U20'))
    for index, _ in np.ndenumerate(color_map):
        i, j = index
        if state[i][j] == -2:
            color_map[i][j] = colours[0]
        elif state[i][j] == -1:
            color_map[i][j] = colours[1]
        elif state[i][j] == 0:
            color_map[i][j] = colours[2]
        elif state[i][j] == 1:
            color_map[i][j] = colours[3]
        else:
            color_map[i][j] = colours[4]
    ax.plot_surface(X, Y, terrain, facecolors=color_map, edgecolor='none', alpha=.7, rcount=lX, ccount=lX)
    ax.axis('off')
    image_path = file_path+f'/{t}-3D.png'
    plt.savefig(image_path, dpi=dpi)
    plt.close()
    return image_path

if __name__ == "__main__":

    from matplotlib.colors import ListedColormap, BoundaryNorm
    from random import seed
    from random import random

    seed(3) # for testing

    # initial array
    size = 100
    initial = np.zeros((size, size))

    # steps to evolve through
    steps = 20

    # set probabilities and update rule
    p_burn, p_lightning = 0.3, 0.00005
    d_water, p_water = 8, 0.02
    rule = fire_rule_Z_snow
    p_born = 0.01

    # set file path for images
    file_path = f"./Images/{rule.__name__}/s{size}_pb{p_burn}_pl{p_lightning}"
    # setup colourmap and norm for plots
    forest_colours = ["snow", "dodgerblue", "forestgreen", "orange", "dimgrey"]
    forest_colours = ['#EAF2EF', '#27187E', '#1E3F20', '#FF8600', '#1A1F16']
    forest_colours = ['#EAF2EF', '#758BFD', '#519E8A', '#FF8600', '#1A1F16']
    forest_cmap = ListedColormap(forest_colours)
    bounds = [-2, -1, -0.5, .5, 1.5, 2.5]
    norm = BoundaryNorm(bounds, forest_cmap.N)

    # create random noise map
    from opensimplex import OpenSimplex
    tmp = OpenSimplex()
    terrain_pad = np.zeros((size+1, size+1))
    fudge = size/2
    for index, val in np.ndenumerate(terrain_pad):
        i, j = index
        n = tmp.noise2d(x=i/fudge, y=j/fudge) + .5
        if n < 0:
            n = 0
        terrain_pad[i][j] = n
    top = np.max(terrain_pad)
    snow = 0.1
    s_level = top-snow
    p_snow = 0.4

    # terrain map - one with edge pad
    ln = len(terrain_pad)
    terrain = terrain_pad[1:ln+1, 1:ln+1]

    # where terrain is 0 set initial to -1 for water
    initial = np.where(terrain==0, -1, initial)
    # where terrain is top-snow val set to -2 for snow
    initial = np.where(terrain > s_level, -2, initial)

    # start CA
    fire = CA(initial, 'ghost', verbose=True, plot=True, plot3D=True, gif=True, gif3D=True,
            dpi=100, history=True, fp=file_path, cmap=forest_cmap, norm=norm,
            Z=terrain_pad, plot_func3D=forest_3D, colors3D=forest_colours)

    # evolve the CA and plot gif
    fire.mevolve(fire_rule_Z_snow, steps, p1=p_burn, p2=p_lightning,
                  Z=terrain_pad, d=d_water, p3=p_water,
                  s_level=s_level, p_snow=p_snow, p_born=p_born)
    fire.make_gif()
    fire.make_gif3D()