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

# def ShuffleList():
#     shuffle_list = random.shuffle(population_list)
#     get_list = []
#     for i in range(1, int(current_population / 2)):
#         get_list.append(shuffle_list[i])
#     return get_list
    
def MixingPopulation():
    get_list = []
    for i in range(1, int(current_population / 2) + 1):
        get_list.append(i)
    random.shuffle(get_list)
    return get_list

    # while(len(get_mixing_list) < current_population):
    #     get_mix = random.randrange(0, current_population - 1)
    #     while(len(get_mixing_list) == get_mix): 
    #         get_mix = random.randrange(0, current_population - 1)
    #     get_mixing_list.append(get_mix)
            

# Init population
InitPopulation()

get_mixing_list = MixingPopulation()

print(get_mixing_list)
print(population_list)

# fig, ax = plt.subplots()             # Create a figure containing a single Axes.
# ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the Axes.
# plt.show()                           # Show the figure.