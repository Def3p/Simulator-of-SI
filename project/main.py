import matplotlib.pyplot as plt
import numpy as np
import random

# population
population_list = []
get_mixing_list = []
current_population = int(input("Кол-во людей в городе: "))

# error
cash_error = 1

def InitPopulation():
    while(len(population_list) < current_population):
        population_list.append(100)

def ChanceOfError(): 
    return random.randrange(101)

def MixingPopulation():
    while(len(get_mixing_list) < current_population):
        get_mix = random.randrange(0, current_population - 1)
        while(len(get_mixing_list) == get_mix): 
            get_mix = random.randrange(0, current_population - 1)
        get_mixing_list.append(get_mix)
            

# Init population
InitPopulation()

MixingPopulation()

print(get_mixing_list)
print(len(population_list))
# fig, ax = plt.subplots()             # Create a figure containing a single Axes.
# ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the Axes.
# plt.show()                           # Show the figure.