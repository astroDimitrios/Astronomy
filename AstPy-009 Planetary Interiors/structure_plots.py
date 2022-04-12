import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from copy import copy

file = 'structure.csv'

df = pd.read_csv(file)

# print(df.head())

# mars = df.loc[df['object'] == 'mars']

# print(mars)

# mars = mars.loc[mars['layer_type'] == 'compositional']

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

def gen_plots(planet_name, layer_type):
    '''
    Takes a planets name from the csv (lowercase) and makes three plots
    1) A semicircle of the layers and a legend
    2) An adjusted version of 1 without a legend
    3) 1 and 2 shown as quarters next to each other with a legend 

    layer_type parameter specifies whether to plot compositional or mechanical layers
    '''
    # Get data for planet
    planet = df.loc[df['object'] == planet_name]
    planet = planet.loc[planet['layer_type'] == layer_type]
    depths =planet['depth'].values
    depth_from_center = planet['depth_from_center'].values
    radius = depth_from_center[-1]
    zorders = planet['depth_order'].values[::-1]
    colors = planet['color'].values
    layers = planet['name'].values
    # Generic position and size arguments for text
    y_name = 0.65 # title
    x_name = 0.51 # title
    # y_name = 1.62 # title - dpi 500
    # x_name = 1.275 # title - dpi 500
    adjust = 0.02 # under-title
    # adjust = 0.05 # under-title - dpi 500
    layerTextSize = 6 # under-title
    noLayerText = ['venus', 'jupiter', 'saturn', 'uranus', 'neptune']
    # legend positions
    if layer_type == 'compositional':
        xleg1, yleg1 = 0.525, -0.05
        xleg2, yleg2 = 1.1, -0.075
    if layer_type == 'mechanical':
        xleg1, yleg1 = 0.520, -0.05
        xleg2, yleg2 = 1.05, -0.075
    # position for distance from centre values
    htexty = -0.09
    # Figure 1 planet with legend
    fig = plt.figure(num=1, figsize=(5,5))
    ax = plt.subplot()
    ax.text(x_name, y_name, planet_name.capitalize(), transform=fig.transFigure, color='grey', ha='center')
    if planet_name not in noLayerText:
        ax.text(x_name, y_name-adjust, layer_type, transform=fig.transFigure, color='grey', ha='center', fontsize=layerTextSize)
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
    leg1 = ax.legend(planet_toScale, layers, loc='upper center', bbox_to_anchor=(xleg1, yleg1), ncol=2, frameon=False, handlelength=1, handleheight=1)
    plt.setp(leg1.get_texts(), color='grey')
    # Figure 2 planet adjusted no legend
    fig2 = plt.figure(num=2, figsize=(5,5))
    ax = plt.subplot()
    ax.text(x_name, y_name, planet_name.capitalize(), transform=fig.transFigure, color='grey', ha='center')
    if planet_name not in noLayerText:
        ax.text(x_name, y_name-adjust, layer_type, transform=fig.transFigure, color='grey', ha='center', fontsize=layerTextSize)
    planet_adjusted = []
    heights = []
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
        heights.append(height)
        circle = Circle((0, 0), height, color=colors[i], zorder=zorders[i], label=layers[i])
        ax.add_artist(circle)
        planet_adjusted.append(circle)
    ax.set_xlim(-1.4, 1.4)
    ax.set_ylim(0, 1.4)
    ax.set_aspect('equal')
    ax.axis('off')
    # Figure 3 adjusted next to noral with data points and legend
    fig3 = plt.figure(num=3, figsize=(5, 5))
    ax1 = fig3.add_subplot(121)
    ax2 = fig3.add_subplot(122)
    ax1.text(x_name, y_name, planet_name.capitalize(), transform=fig.transFigure, color='grey', ha='center')
    if planet_name not in noLayerText:
        ax1.text(x_name, y_name-adjust, layer_type, transform=fig.transFigure, color='grey', ha='center', fontsize=layerTextSize)
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
    # We won't plot some of the distances for the atmosphere as labels overlap
    if (planet_name=='earth' and layer_type=='mechanical') or (planet_name=='venus'):
        ax1.text(-0.5, htexty, 'values in km\ninter-atmospheric values not shown', fontsize=4, ha='center', va='center', color='grey', alpha=0.5, wrap=True)
    else:
        ax1.text(-0.5, htexty, 'values in km', fontsize=4, ha='center', va='center', color='grey', alpha=0.5)
    texts = []
    # Get heights to plot as text (some are set manually so there is no overlap)
    for i in range(len(heights)):
        longest = len(str(int(depth_from_center[-1])))
        height_label = str(int(depth_from_center[i]))
        if len(height_label) < longest:
            height_label = height_label+(longest-len(height_label))*' '
        # print(height_label)
        if planet_name == 'mars' and layer_type == 'mechanical':
            heights = [0.50, 0.57, 0.7, 0.98, 1.026, 1.07]
        elif planet_name =='earth' and layer_type == 'mechanical':
            heights = [0.17744513878796686, 0.5057404447028048, 0.8212469117860776, 0.90, 0.94, 0.9404156372620258, 0.9549484086615317, 0.9694811800610377, 0.9840139514605435, 1.042145037058567]
        elif planet_name =='earth' and layer_type == 'compositional':
            heights = [0.5057404447028048, 0.90, 0.95, 1.0101729399796542]
        elif planet_name =='jupiter' and layer_type == 'compositional':
            heights = [0.30177514792899407, 0.7514792899408284, 0.95, 1.0]
        elif planet_name =='mars' and layer_type == 'compositional':
            heights = [0.5232558139534884, 0.95, 1.00, 1.05]
        elif planet_name =='saturn' and layer_type == 'compositional':
            heights = [0.36, 0.4125874125874126, 0.5804195804195804, 0.95, 1.0]
        elif planet_name =='venus' and layer_type == 'compositional':
            heights = [0.5067701322353314, 0.932, 0.972, 0.9869348325283078, 1.002771399160662, 1.0285058199382373]
        # If not to stop text plotting of inter-atmospheric distances
        if layer_type == 'mechanical':
            if not (planet_name == 'earth' and (i==5 or i==6 or i==7 or i==8)):
                texts.append(ax2.text(heights[i], htexty, height_label, fontsize=4, ha='center', va='center', color='grey', alpha=0.5, rotation=-90.))
        else:
            if not (planet_name == 'venus' and (i==3 or i==4)):
                texts.append(ax2.text(heights[i], htexty, height_label, fontsize=4, ha='center', va='center', color='grey', alpha=0.5, rotation=-90.))
    leg3 = ax1.legend(loc='upper center', bbox_to_anchor=(xleg2, yleg2), ncol=2, frameon=False, handlelength=1, handleheight=1)
    plt.setp(leg3.get_texts(), color='grey')
    fig3.subplots_adjust(wspace=0.02, hspace=0)
    fig.savefig('./figures/'+layer_type+'/'+planet_name+'_'+layer_type+'_interior.png', dpi=200)
    fig2.savefig('./figures/'+layer_type+'/'+planet_name+'_'+layer_type+'_interior_adjusted.png', dpi=200)
    fig3.savefig('./figures/'+layer_type+'/'+planet_name+'_'+layer_type+'_interior_both.png', dpi=200)
    plt.close('all')

# planet_names = np.unique(df['object'].values)
# for planet in planet_names:
#     gen_plots(planet, 'compositional')

# for planet in ['earth', 'mars', 'mercury', 'moon']:
#     gen_plots(planet, 'mechanical')

for planet in ['mars']:
    gen_plots(planet, 'mechanical')

def compare_four(name, layer_type='compositional'):
    '''
    This could probably be tidied up with more loops!
    Will produce the 4 quarter comparison of the rocky planets or ice giants
    Rocky planets if name='rocky' and ice if anything else
    Does not use adjusted layers for visibility

    Use the _simp columns to simplify the legend for rocky planets
    Has no effect on the ice giants figure
    Lines where _simp is used are marked #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    for easy reversion

    Setup not to plot atmospheres
    Cannot plot mechanical data since it's missing for Venus and Gas Giants
    '''
    if name == 'rocky':
        p1, p2, p3, p4 = 'venus', 'earth', 'mercury', 'mars'
    else:
        p1, p2, p3, p4 = 'jupiter', 'saturn', 'neptune', 'uranus'
    planet1 = df.loc[df['object'] == p1]
    planet1 = planet1.loc[planet1['layer_type'] == layer_type]
    if name == 'rocky':
        planet1 = planet1.loc[planet1['atm'] == 'n']
    depth_from_center1 = planet1['depth_from_center'].values
    radius1 = depth_from_center1[-1]
    zorders1 = planet1['depth_order'].values[::-1]
    colors1 = planet1['color_simp'].values #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    layers1 = planet1['name_simp'].values #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    planet2 = df.loc[df['object'] == p2] ########
    planet2 = planet2.loc[planet2['layer_type'] == layer_type]
    if name == 'rocky':
        planet2 = planet2.loc[planet2['atm'] == 'n']
    depth_from_center2 = planet2['depth_from_center'].values
    radius2 = depth_from_center2[-1]
    zorders2 = planet2['depth_order'].values[::-1]
    colors2 = planet2['color_simp'].values #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    layers2 = planet2['name_simp'].values #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    planet3 = df.loc[df['object'] == p3] ########
    planet3 = planet3.loc[planet3['layer_type'] == layer_type]
    if name == 'rocky':
        planet3 = planet3.loc[planet3['atm'] == 'n']
    depth_from_center3 = planet3['depth_from_center'].values
    radius3 = depth_from_center3[-1]
    zorders3 = planet3['depth_order'].values[::-1]
    colors3 = planet3['color_simp'].values #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    layers3 = planet3['name_simp'].values #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    planet4 = df.loc[df['object'] == p4] ########
    planet4 = planet4.loc[planet4['layer_type'] == layer_type]
    if name == 'rocky':
        planet4 = planet4.loc[planet4['atm'] == 'n']
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
        for i in range(len(planet[j])):
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
            axes[j].text(0.2, 0.7, p1.capitalize(), transform=fig.transFigure, color='grey')
        elif j == 1:
            axes[j].set_xlim(0, 1.4)
            axes[j].set_ylim(0, 1.4)
            # Ice Giants 0.7, 0.7
            if name == 'rocky':
                x, y = 0.75, 0.7
            else:
                x, y = 0.7, 0.7
            axes[j].text(x, y, p2.capitalize(), transform=fig.transFigure, color='grey')
        elif j ==3:
            axes[j].set_xlim(0, 1.4)
            axes[j].set_ylim(-1.4, 0)
            # Ice Giants 0.325, 0.4
            if name == 'rocky':
                x, y = 0.3, 0.4
            else:
                x, y = 0.325, 0.4
            axes[j].text(x, y, p3.capitalize(), transform=fig.transFigure, color='grey')
        else:
            axes[j].set_xlim(-1.4, 0)
            axes[j].set_ylim(-1.4, 0)
            # Ice Giants 0.6, 0.4
            if name == 'rocky':
                x, y = 0.675, 0.4
            else:
                x, y = 0.6, 0.4
            axes[j].text(x, y, p4.capitalize(), transform=fig.transFigure, color='grey')
        axes[j].set_aspect('equal')
        axes[j].axis('off')
    leg_labels = [*for_legend]
    leg_patches = [*for_legend.values()]
    # Ice Giants 0.525, 0.3, ncol=2
    if name == 'rocky':
        lgd = fig.legend(leg_patches, leg_labels, loc='upper center', bbox_to_anchor=(0.53, 0.3), ncol=4, frameon=False, handlelength=1, handleheight=1)
    else:
        lgd = fig.legend(leg_patches, leg_labels, loc='upper center', bbox_to_anchor=(0.525, 0.35), ncol=2, frameon=False, handlelength=1, handleheight=1)
    plt.setp(lgd.get_texts(), color='grey')
    fig.subplots_adjust(wspace=0.01, hspace=0.02)
    fig.set_size_inches(6,6)
    if name == 'rocky':
        fig.savefig('./figures/rocky_interiors_'+layer_type+'_simpLegend.png', dpi=800, bbox_extra_artists=(lgd,))
    else:
        fig.savefig('./figures/ice_giant_interiors_'+layer_type+'.png', dpi=800)

# compare_four('rocky', 'compositional')
# compare_four('ice', 'compositional')

def comp_vs_mechan(planet_name):
    '''
    Takes a planet name and plots their compositional and mechanical layers next to each other

    Options:
    earth
    mars
    moon
    mercury
    '''
    planet = df.loc[df['object'] == planet_name]
    planet = planet.loc[planet['atm'] == 'n']
    planet_comp = planet.loc[planet['layer_type'] == 'compositional']
    depth_from_center_comp = planet_comp['depth_from_center'].values
    radius_comp = depth_from_center_comp[-1]
    zorders_comp = planet_comp['depth_order'].values[::-1]
    colors_comp = planet_comp['color'].values
    layers_comp = planet_comp['name'].values
    # Mechan
    planet_mech = planet.loc[planet['layer_type'] == 'mechanical']
    depth_from_center_mech = planet_mech['depth_from_center'].values
    radius_mech = depth_from_center_mech[-1]
    zorders_mech = planet_mech['depth_order'].values[::-1]
    colors_mech = planet_mech['color'].values
    layers_mech = planet_mech['name'].values
    # Generic position and size arguments for text
    y_name = 0.7 # title
    x_name = 0.51 # title
    htexty = -0.09
    # Figure 1 planet with legend
    fig = plt.figure(num=1, figsize=(10,5))
    ax1 = fig.add_subplot(121)
    ax2 = fig.add_subplot(122)
    ax1.text(x_name, y_name, planet_name.capitalize(), fontsize=14, transform=fig.transFigure, color='grey', ha='center')
    heights1 = []
    legpatch1 = []
    leglabel1 = []
    for i in range(len(planet_comp)):
        height = depth_from_center_comp[i]/radius_comp
        circle = Circle((0, 0), height, color=colors_comp[i], zorder=zorders_comp[i], label=layers_comp[i])
        ax1.add_artist(circle)
        heights1.append(height)
        legpatch1.append(circle)
        leglabel1.append(layers_comp[i])
    heights2 = []
    legpatch2 = []
    leglabel2 = []
    for i in range(len(planet_mech)):
        height = depth_from_center_mech[i]/radius_mech
        circle = Circle((0, 0), height, color=colors_mech[i], zorder=zorders_mech[i], label=layers_mech[i])
        ax2.add_artist(circle)
        heights2.append(height)
        legpatch2.append(circle)
        leglabel2.append(layers_mech[i])
    # Add labels
    if planet_name=='earth':
        heights1 = [0.5436650523355726, 0.96, 1.01]
        heights2 = [0.1907514450867052, 0.5436650523355726, 0.8828308076862991, 0.945, 0.985, 1.025]
    if planet_name=='mars':
        heights1 = [0.5309734513274337, 0.97, 1.01]
        heights2 = [0.50, 0.54, 0.6932153392330384, 0.97, 1.01]
    if planet_name=='mercury':
        heights2 = [0.5012126111560227, 0.8383185125303153, 0.9009700889248181, 0.97, 1.01]
    for i in range(len(heights1)):
        longest = len(str(int(depth_from_center_comp[-1])))
        height_label = str(int(depth_from_center_comp[i]))
        if len(height_label) < longest:
            height_label = height_label+(longest-len(height_label))*' '
        ax1.text(-heights1[i], htexty, height_label, fontsize=8, ha='center', va='center', color='grey', alpha=0.5, rotation=90.)
    for i in range(len(heights2)):
        longest = len(str(int(depth_from_center_mech[-1])))
        height_label = str(int(depth_from_center_mech[i]))
        if len(height_label) < longest:
            height_label = height_label+(longest-len(height_label))*' '
        ax2.text(heights2[i], htexty, height_label, fontsize=8, ha='center', va='center', color='grey', alpha=0.5, rotation=-90.)
    ax1.set_xlim(-1.4, 0)
    ax1.set_ylim(0, 1.4)
    ax2.set_xlim(0, 1.4)
    ax2.set_ylim(0, 1.4)
    ax1.set_aspect('equal')
    ax1.axis('off')
    ax2.set_aspect('equal')
    ax2.axis('off')
    htextx = -0.15
    if planet_name=='moon':
        htextx = -0.5
    ax1.text(-0.5, -0.21, 'compositional', ha='center', va='center', color='grey', alpha=1.0)
    ax1.text(htextx, htexty, 'values in km', fontsize=8, ha='center', va='center', color='grey', alpha=0.5)
    ax2.text(0.5, -0.21, 'mechanical', ha='center', va='center', color='grey', alpha=1.0)
    leg1 = ax1.legend(legpatch1, leglabel1, loc='upper center', bbox_to_anchor=(0.625, -0.17), ncol=1, frameon=False, handlelength=1, handleheight=1)
    plt.setp(leg1.get_texts(), color='grey')
    leg2 = ax2.legend(legpatch2, leglabel2, loc='upper center', bbox_to_anchor=(0.375, -0.17), ncol=2, frameon=False, handlelength=1, handleheight=1)
    plt.setp(leg2.get_texts(), color='grey')
    fig.subplots_adjust(wspace=0.02, hspace=0)
    fig.savefig('./figures/comp_vs_mech/'+planet_name+'_comp_vs_mech.png', dpi=800, bbox_inches='tight')

# comp_vs_mechan('earth')
# comp_vs_mechan('mars')
# comp_vs_mechan('moon')
# comp_vs_mechan('mercury')