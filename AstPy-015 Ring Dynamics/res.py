import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 

saturn_moons = pd.read_csv('saturn_moons.csv')
print(saturn_moons.head())

moon_names = saturn_moons['Name'].values
moon_res = pd.DataFrame({}, columns=moon_names)
# print(moon_res)

for i in moon_names:
    this_moon_period = saturn_moons.loc[saturn_moons['Name'] == i, 'Period'].values[0]
    res = []
    for j in moon_names:
        period_ratio = saturn_moons.loc[saturn_moons['Name'] == j, 'Period'].values[0]/this_moon_period
        res.append(period_ratio)
    this_row = pd.DataFrame([res], index=[i], columns=moon_names)
    moon_res = pd.concat([moon_res, this_row])

print(moon_res)

mimas_radius = saturn_moons.loc[saturn_moons['Name'] == 'Mimas', 'Semimajor Axis'].values[0]
mimas_period = saturn_moons.loc[saturn_moons['Name'] == 'Mimas', 'Period'].values[0]
print('Mimas a = {:6.0f} km'.format(mimas_radius))
print('Mimas T = {:6.2f} days'.format(mimas_period))

const = mimas_radius**3 / mimas_period**2 # km^3 / days^2

mimas_2_1_period = mimas_period/2
mimas_2_1_radius = (const*mimas_2_1_period**2)**(1/3)
print('Mimas 2:1 res a = {:6.0f} km'.format(mimas_2_1_radius))
print('Mimas 2:1 res T = {:6.2f} days'.format(mimas_2_1_period))

def locate_res(moon_name, order):
    '''
    Takes the name of a moon of saturn as a string and returns the resonant periods and locations
    '''
    moon_radius = saturn_moons.loc[saturn_moons['Name'] == moon_name, 'Semimajor Axis'].values[0]
    moon_period = saturn_moons.loc[saturn_moons['Name'] == moon_name, 'Period'].values[0]
    print(moon_name+' a = {:6.0f} km'.format(moon_radius))
    print(moon_name+' T = {:6.2f} days'.format(moon_period))
    this_const = moon_radius**3 / moon_period**2 # km^3 / days^2
    res_no = [2, 3, 4, 5, 6, 7]
    for i in res_no:
        this_res_period = moon_period/i*(i-order)
        this_res_radius = (this_const*this_res_period**2)**(1/3)
        print(moon_name+' '+str(i)+':'+str(i-order)+' a = {:6.0f} km'.format(this_res_radius))
        print(moon_name+' '+str(i)+':'+str(i-order)+' T = {:6.2f} days'.format(this_res_period))

locate_res('Janus', 1)
locate_res('Mimas', 2)