import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, BoundaryNorm
from random import seed
from random import random
from pathlib import Path
import imageio

class CA:
    """ Creates CA
    """

    def __init__(self, grid, edge_rule):
        """ Initialises grid
        """
        if not edge_rule == 'ghost':
            raise ValueError('Only edge_rule ghost implemented.')
        self.edge_rule = edge_rule
        self.grid = np.pad(grid, (1, 1), 'constant', constant_values=(0,0))
        self.size = len(grid)
        self.t = 0
        self.filenames = [] # only need this if giffing!!!!!

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

    def plot_state(self, colours, file_path, verbose=False, gif=False):
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

    def make_gif(self, file_path):
        gif_path = file_path+'/'+file_path.split('/')[-1]+'.gif'
        print(f'Saving gif to - {gif_path}')
        with imageio.get_writer(gif_path, mode='I') as writer:
            for filename in self.filenames:
                image = imageio.imread(filename)
                writer.append_data(image)

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

    seed(1) # for testing

    # initial array and probabilities
    size = 50
    initial = np.zeros((50, 50))
    p_burn, p_lightning = 0.3, 0.001
    steps = 20

    # start CA
    fire = CA(initial, 'ghost')

    rule = fire_rule_1

    verbose = False
    plot = True
    gif = True

    if plot:
        file_path = f"./Images/{rule.__name__}/s{size}_pb{p_burn}_pl{p_lightning}"
        print(f"Files saving to - {file_path}")
        Path(file_path).mkdir(parents=True, exist_ok=True)
        forest_cmap = ListedColormap(["forestgreen", "orange", "dimgrey"])
        bounds = [0, .5, 1.5, 2.5]
        norm = BoundaryNorm(bounds, forest_cmap.N)

    # these should be class methods?
    if verbose:
        fire.print_state()
    if plot:
        fire.plot_state(forest_cmap, file_path, verbose=True, gif=gif)
    
    for i in range(steps):
        fire.evolve(fire_rule_1, p1=p_burn, p2=p_lightning)
        if verbose:
            fire.print_state()
        if plot:
            fire.plot_state(forest_cmap, file_path, verbose=True, gif=gif)

    if gif:
        fire.make_gif(file_path)