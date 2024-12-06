import matplotlib.pyplot as plt
import numpy as np
import random

# Input переменные
max_population = int(input("Кол-во людей в городе: "))

# Общество
population_list = []
get_mixing_list = []

# Выгода торговли
trading_error = 1

def InitPopulation(list):
    while(len(list) < max_population):
        list.append(100)
    return list

def ChanceOfError(percent): 
    return random.randrange(percent) / 100

# def ShuffleList():
#     shuffle_list = random.shuffle(population_list)
#     get_list = []
#     for i in range(1, int(current_population / 2)):
#         get_list.append(shuffle_list[i])
#     return get_list
    
def MixingPopulation():
    get_list = []
    for i in range(int(max_population * ChanceOfError(30))):
        get_list.append(i)
    random.shuffle(get_list)
    return get_list

    # while(len(get_mixing_list) < current_population):
    #     get_mix = random.randrange(0, current_population - 1)
    #     while(len(get_mixing_list) == get_mix): 
    #         get_mix = random.randrange(0, current_population - 1)
    #     get_mixing_list.append(get_mix)

print(MixingPopulation())
print(int(max_population * ChanceOfError(30)))
get_mixing_list = MixingPopulation()

# Создание общества
population_list = InitPopulation(population_list)

# Графики

plt.style.use('ggplot') # Стиль

fig, axes = plt.subplots(2, 2) # Разметка окна

x1 = range(200)
y1 = range(200)

# График 1
axes[0, 0].set_title("День 1", fontsize = 15)

axes[0, 0].set_xlim(0, 200)
axes[0, 0].set_ylim(0, 5000)

axes[0, 0].set_xticks(np.arange(0, 200, 50))
axes[0, 0].set_yticks(np.arange(0, 5000, 1000))

axes[0, 0].grid()

axes[0, 0].bar(x1, y1, color = "black")

# График 2


# График 3


# График 4

plt.show() # Открыть окно