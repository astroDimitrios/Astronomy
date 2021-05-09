import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import imageio

class CA:
    """ Creates the CA
    """

    def __init__(self, grid, edge_rule, verbose=False, plot=False, gif=False, **kwargs):
        """ Initialises the CA
        """
        self.grid_edge(grid, edge_rule)
        self.t = 0
        self.verbose = verbose
        if gif:
            self.gif = gif
            self.filenames = [] # only need this if giffing!!!!!
        if plot:
            self.plot = plot
            self.plot_setup(kwargs)
            self.plot_state(self.cmap, self.fp, self.verbose, self.gif)

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
                    new_grid[i, j] = rule(val, self.get_neighbours(i, j, 1), **kwargs)
        self.grid = new_grid
        self.t += 1

    def mevolve(self, rule, steps, **kwargs):
        ''' Evolve n steps using the evolve() function above
        '''
        for i in range(steps):
            self.evolve(rule, **kwargs)
            if self.plot:
                self.plot_state(self.cmap, self.fp, self.verbose, self.gif)
        

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
            print(f"Files saving to - {file_path}/")
        Path(self.fp).mkdir(parents=True, exist_ok=True)

    def plot_state(self, colours, file_path, verbose, gif):
        ''' Plot the current state
        '''
        fig = plt.figure(num=self.t, figsize=(10, 10))
        ax = fig.add_subplot(111, label="ax")
        ax.imshow(self.state(), cmap=colours, norm=norm, interpolation='nearest', origin='lower')
        ax.axis('off')
        if verbose:
            print(f'Saving figure for timestep - {self.t:>4}')
        image_path = file_path+f'/{self.t}.png'
        if gif:
            self.filenames.append(image_path)
        plt.savefig(image_path)
        plt.close()

    def make_gif(self):
        ''' Makes a gif with all plotted states
        '''
        gif_path = self.fp+'/'+self.fp.split('/')[-1]+'.gif'
        if self.verbose:
            print(f'Saving gif to - {gif_path}')
        with imageio.get_writer(gif_path, mode='I') as writer:
            for filename in self.filenames:
                image = imageio.imread(filename)
                writer.append_data(image)

# custom fire rule
def fire_rule_1(val, n, **kwargs):
    """ Fire rule

    0 - alive chance of lightning or burn due to neighbours
    1 - turn to dead (2)
    2 - dead and stay dead
    """
    p_burn, p_lightning = kwargs.values()
    if val == 2:
        return 2 # keep dead tree
    if val == 1:
        return 2 # dead tree
    if random() < p_lightning:
        return 1 # burning
    _, counts = np.unique(n, return_counts=True) # values, counts
    if len(counts) == 1:
        return 0 # check if surrounded by zeros
    if random() < p_burn*counts[1]:
        return 1 # burning
    return 0 # tree is alive


if __name__ == "__main__":

    from matplotlib.colors import ListedColormap, BoundaryNorm
    from random import seed
    from random import random

    seed(3) # for testing

    # initial array
    size = 50
    initial = np.zeros((size, size))

    # steps to evolve through
    steps = 20

    # set probabilities and update rule
    p_burn, p_lightning = 0.3, 0.001
    rule = fire_rule_1

    # set file path for images
    file_path = f"./Images/{rule.__name__}/s{size}_pb{p_burn}_pl{p_lightning}"
    # setup colourmap and norm for plots
    forest_cmap = ListedColormap(["forestgreen", "orange", "dimgrey"])
    bounds = [0, .5, 1.5, 2.5]
    norm = BoundaryNorm(bounds, forest_cmap.N)

    # start CA
    fire = CA(initial, 'ghost', verbose=True, plot=True, gif=True,
            fp=file_path, cmap=forest_cmap, norm=norm)

    # evolve the CA and plot gif
    fire.mevolve(fire_rule_1, steps, p1=p_burn, p2=p_lightning)
    fire.make_gif()