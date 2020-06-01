import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from copy import copy

file = 'core_sources.csv'

df = pd.read_csv('core_sources.csv')

# print(df.head())

# mars = df.loc[df['object'] == 'mars']

# print(mars)

# depths = mars['depth'].values
# depth_from_center = mars['depth_from_center'].values
# radius = depth_from_center[-1]
# zorders = mars['depth_order'].values[::-1]
# colors = mars['color'].values
# layers = mars['name'].values

# fig = plt.figure(num=1, figsize=(5,5))
# ax = plt.subplot()
# mars_toScale = []

# for i in range(len(mars)):
#     height = depth_from_center[i]/radius
#     circle = Circle((0, 0), height, color=colors[i], zorder=zorders[i], label=layers[i])
#     ax.add_artist(circle)
#     mars_toScale.append(circle)

# ax.set_xlim(-1.4, 1.4)
# ax.set_ylim(-1.4, 1.4)
# ax.set_aspect('equal')
# ax.axis('off')
# ax.legend(mars_toScale, layers, loc='upper center', bbox_to_anchor=(0.525, 0.1), ncol=2, frameon=False)

# fig2 = plt.figure(num=2, figsize=(5,5))
# ax = plt.subplot()
# mars_adjusted = []

# prev_alt = 0

# for i in range(len(mars)):
#     depth = depths[i]
#     from_center = depth_from_center[i]
#     if prev_alt != 0:
#         from_center += prev_alt
#     if depth < 100:
#         height = (100-depth+from_center)/radius
#         prev_alt += 100-depth
#     else:
#         height = from_center/radius
#     circle = Circle((0, 0), height, color=colors[i], zorder=zorders[i], label=layers[i])
#     ax.add_artist(circle)
#     mars_adjusted.append(circle)

# ax.set_xlim(-1.4, 1.4)
# ax.set_ylim(-1.4, 1.4)
# ax.set_aspect('equal')
# ax.axis('off')

# fig3 = plt.figure(num=3, figsize=(5, 5))
# ax1 = fig3.add_subplot(121)
# ax2 = fig3.add_subplot(122)

# for circle in mars_toScale:
#     new_circle = copy(circle)
#     new_circle.axes = None
#     new_circle.figure = None
#     new_circle.set_transform(ax1.transData)
#     ax1.add_patch(new_circle)
# for circle in mars_adjusted:
#     new_circle = copy(circle)
#     new_circle.axes = None
#     new_circle.figure = None
#     new_circle.set_transform(ax2.transData)
#     ax2.add_patch(new_circle)

# ax1.set_xlim(-1.4, 0)
# ax1.set_ylim(-1.4, 1.4)
# ax1.set_aspect('equal')
# ax1.axis('off')
# ax2.set_xlim(0, 1.4)
# ax2.set_ylim(-1.4, 1.4)
# ax2.set_aspect('equal')
# ax2.axis('off')

# ax1.legend(loc='upper center', bbox_to_anchor=(1.1, 0.1), ncol=2, frameon=False)

# fig3.subplots_adjust(wspace=0, hspace=0)

# plt.show()

def gen_plots(planet_name):
    '''
    Takes a planets name from the csv (lowercase) and makes three plots
    1) A semicircle of the layers and a legend
    2) An adjusted version of 1 without a legend
    3) 1 and 2 shown as quarters next to each other with a legend 
    '''
    planet = df.loc[df['object'] == planet_name]
    depths =planet['depth'].values
    depth_from_center = planet['depth_from_center'].values
    radius = depth_from_center[-1]
    zorders = planet['depth_order'].values[::-1]
    colors = planet['color'].values
    layers = planet['name'].values
    y_name = 0.65
    x_name = 0.51
    fig = plt.figure(num=1, figsize=(5,5))
    ax = plt.subplot()
    ax.text(x_name, y_name, planet_name, transform=fig.transFigure, color='grey', ha='center')
    planet_toScale = []
    for i in range(len(planet)):
        height = depth_from_center[i]/radius
        circle = Circle((0, 0), height, color=colors[i], zorder=zorders[i], label=layers[i])
        ax.add_artist(circle)
        planet_toScale.append(circle)
    ax.set_xlim(-1.4, 1.4)
    ax.set_ylim(0, 1.4)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.legend(planet_toScale, layers, loc='upper center', bbox_to_anchor=(0.525, -0.05), ncol=2, frameon=False)
    fig2 = plt.figure(num=2, figsize=(5,5))
    ax = plt.subplot()
    ax.text(x_name, y_name, planet_name, transform=fig.transFigure, color='grey', ha='center')
    planet_adjusted = []
    prev_alt = 0
    for i in range(len(planet)):
        depth = depths[i]
        from_center = depth_from_center[i]
        if prev_alt != 0:
            from_center += prev_alt
        if depth < 100:
            height = (100-depth+from_center)/radius
            prev_alt += 100-depth
        else:
            height = from_center/radius
        circle = Circle((0, 0), height, color=colors[i], zorder=zorders[i], label=layers[i])
        ax.add_artist(circle)
        planet_adjusted.append(circle)
    ax.set_xlim(-1.4, 1.4)
    ax.set_ylim(0, 1.4)
    ax.set_aspect('equal')
    ax.axis('off')
    fig3 = plt.figure(num=3, figsize=(5, 5))
    ax1 = fig3.add_subplot(121)
    ax2 = fig3.add_subplot(122)
    ax1.text(x_name, y_name, planet_name, transform=fig.transFigure, color='grey', ha='center')
    for circle in planet_toScale:
        new_circle = copy(circle)
        new_circle.axes = None
        new_circle.figure = None
        new_circle.set_transform(ax1.transData)
        ax1.add_patch(new_circle)
    for circle in planet_adjusted:
        new_circle = copy(circle)
        new_circle.axes = None
        new_circle.figure = None
        new_circle.set_transform(ax2.transData)
        ax2.add_patch(new_circle)
    ax1.set_xlim(-1.4, 0)
    ax1.set_ylim(0, 1.4)
    ax1.set_aspect('equal')
    ax1.axis('off')
    ax2.set_xlim(0, 1.4)
    ax2.set_ylim(0, 1.4)
    ax2.set_aspect('equal')
    ax2.axis('off')
    ax1.legend(loc='upper center', bbox_to_anchor=(1.1, -0.05), ncol=2, frameon=False)
    fig3.subplots_adjust(wspace=0.02, hspace=0)
    fig.savefig('./figures/'+planet_name+'_interior.png', dpi=200)
    fig2.savefig('./figures/'+planet_name+'_interior_adjusted.png', dpi=200)
    fig3.savefig('./figures/'+planet_name+'_interior_both.png', dpi=200)
    plt.close('all')

# planet_names = np.unique(df['object'].values)
# for planet in planet_names:
#     gen_plots(planet)

def compare_four(name):
    '''
    This could probably be tidied up with more loops!
    Will produce the 4 quarter comparison of the rocky planets or ice giants
    Rocky planets if name='rocky' and ice if anything else
    Does not use adjusted layers for visibility

    Use the _simp columns to simplify the legend for rocky planets
    Has no effect on the ice giants figure
    Lines where _simp is used are marked #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    for easy reversion
    '''
    if name == 'rocky':
        p1, p2, p3, p4 = 'venus', 'earth', 'mercury', 'mars'
    else:
        p1, p2, p3, p4 = 'jupiter', 'saturn', 'neptune', 'uranus'
    planet1 = df.loc[df['object'] == p1]
    depth_from_center1 = planet1['depth_from_center'].values
    radius1 = depth_from_center1[-1]
    zorders1 = planet1['depth_order'].values[::-1]
    colors1 = planet1['color_simp'].values #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    layers1 = planet1['name_simp'].values #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    planet2 = df.loc[df['object'] == p2] ########
    depth_from_center2 = planet2['depth_from_center'].values
    radius2 = depth_from_center2[-1]
    zorders2 = planet2['depth_order'].values[::-1]
    colors2 = planet2['color_simp'].values #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    layers2 = planet2['name_simp'].values #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    planet3 = df.loc[df['object'] == p3] ########
    depth_from_center3 = planet3['depth_from_center'].values
    radius3 = depth_from_center3[-1]
    zorders3 = planet3['depth_order'].values[::-1]
    colors3 = planet3['color_simp'].values #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    layers3 = planet3['name_simp'].values #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    planet4 = df.loc[df['object'] == p4] ########
    depth_from_center4 = planet4['depth_from_center'].values
    radius4 = depth_from_center4[-1]
    zorders4 = planet4['depth_order'].values[::-1]
    colors4 = planet4['color_simp'].values #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    layers4 = planet4['name_simp'].values #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    planet = [planet1, planet2, planet3, planet4] ########
    depth_from_center = [depth_from_center1, depth_from_center2, depth_from_center3, depth_from_center4]
    radius = [radius1, radius2, radius3, radius4]
    zorders = [zorders1, zorders2, zorders3, zorders4]
    colors = [colors1, colors2, colors3, colors4]
    layers = [layers1, layers2, layers3, layers4]
    largest = max(radius)
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
    axes = [ax1, ax2, ax3, ax4]
    for_legend = {}
    for j in range(len(axes)):
        # Levels so we don't plot atmospheres for Venus, Earth, and Mars
        if j == 0:
            # no Venus atm
            levels = 2
        elif j == 1:
            # no Earth atm
            levels = 6
        elif j == 3:
            # no Mars atm
            levels = 3
        else:
            levels = len(planet[j])
        for i in range(levels):
            scaling = radius[j]/largest
            from_center = depth_from_center[j][i]
            height = from_center/radius[j]*scaling
            circle = Circle((0, 0), height, color=colors[j][i], zorder=zorders[j][i], label=layers[j][i])
            axes[j].add_artist(circle)
            for_legend[layers[j][i]] = circle
        if j == 0:
            axes[j].set_xlim(-1.4, 0)
            axes[j].set_ylim(0, 1.4)
            # Ice Giants 0.2, 0.7
            axes[j].text(0.2, 0.7, p1, transform=fig.transFigure, color='grey')
        elif j == 1:
            axes[j].set_xlim(0, 1.4)
            axes[j].set_ylim(0, 1.4)
            # Ice Giants 0.7, 0.7
            if name == 'rocky':
                x, y = 0.75, 0.7
            else:
                x, y = 0.7, 0.7
            axes[j].text(x, y, p2, transform=fig.transFigure, color='grey')
        elif j ==3:
            axes[j].set_xlim(0, 1.4)
            axes[j].set_ylim(-1.4, 0)
            # Ice Giants 0.325, 0.4
            if name == 'rocky':
                x, y = 0.3, 0.4
            else:
                x, y = 0.325, 0.4
            axes[j].text(x, y, p3, transform=fig.transFigure, color='grey')
        else:
            axes[j].set_xlim(-1.4, 0)
            axes[j].set_ylim(-1.4, 0)
            # Ice Giants 0.6, 0.4
            if name == 'rocky':
                x, y = 0.675, 0.4
            else:
                x, y = 0.6, 0.4
            axes[j].text(x, y, p4, transform=fig.transFigure, color='grey')
        axes[j].set_aspect('equal')
        axes[j].axis('off')
    leg_labels = [*for_legend]
    leg_patches = [*for_legend.values()]
    # Ice Giants 0.525, 0.3, ncol=2
    if name == 'rocky':
        lgd = fig.legend(leg_patches, leg_labels, loc='upper center', bbox_to_anchor=(0.53, 0.2), ncol=4, frameon=False)
    else:
        lgd = fig.legend(leg_patches, leg_labels, loc='upper center', bbox_to_anchor=(0.525, 0.3), ncol=2, frameon=False)
    fig.subplots_adjust(wspace=0.01, hspace=0.02)
    fig.set_size_inches(6,6)
    if name == 'rocky':
        fig.savefig('./figures/rocky_interiors_simpLegend.png', dpi=200, bbox_extra_artists=(lgd,))
    else:
        fig.savefig('./figures/ice_giant_interiors.png', dpi=200)
    # plt.show()

# compare_four('rocky')
# compare_four('ice')