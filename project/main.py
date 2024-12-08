import matplotlib.pyplot as plt
import numpy as np
import random
import time

start = time.time()
# Input переменные
max_population = 10000

# Общество
get_mixing_list = []

# Выгода торговли
trading_error = 1

# Подсчеты
calculation_list = []

def InitPopulation():
    get_list = np.array([100 for i in np.arange(max_population)])
    return get_list

def RandPercent(percent): 
    return random.randrange(1, percent) / 100
    
def MixingPopulation():
    get_people = np.array([i for i in np.arange(max_population)])
    seller_counter = int(max_population * (random.randrange(23, 34) / 100))
    shuffle_list = get_people
    random.shuffle(shuffle_list)
    get_seller = [shuffle_list[i] for i in np.arange(seller_counter)]
    get_seller = np.array(get_seller)
    shuffle_buyers = []
    for i in shuffle_list: 
        if i not in get_seller and population_list[i] > 0: shuffle_buyers.append(i)
    shuffle_buyers = np.array(shuffle_buyers)
    random.shuffle(shuffle_buyers)
    get_buyer = np.array([shuffle_buyers[i] for i in np.arange(seller_counter)])
    get_list = np.array([[get_seller[i], get_buyer[i]] for i in np.arange(get_seller.size)])
    return get_list

    # while(len(get_mixing_list) < current_population):
    #     get_mix = random.randrange(0, current_population - 1)
    #     while(len(get_mixing_list) == get_mix): 
    #         get_mix = random.randrange(0, current_population - 1)
    #     get_mixing_list.append(get_mix)

def Trading():
    for people in get_mixing_list: # все трейды
        cash_in_trade = 1 #random.randrange(1, 2)  #int(population_list[get_list[people]] * get_trade)

        if random.randrange(100) == 1: # ошибка терминала
            if random.randrange(2) == 1: cash_in_trade -= 1
            else: cash_in_trade += 1

        population_list[people[0]] += cash_in_trade 
        population_list[people[1]] -= cash_in_trade


def Calculation(scale):
    calculation_list = np.array([0 for i in np.arange(scale)])
    # for i in range(scale):
    #     calculation_list.append(0)
    for i in population_list:
        if i < scale:
            calculation_list[i] += 1
    return calculation_list

population_list = InitPopulation()
print(f"Популяция: {max_population}")

# Создание общества


get_mixing_list = MixingPopulation()
Trading()

# Графики

plt.style.use('ggplot')# Стиль


fig, axes = plt.subplots(2, 3) # Разметка окна

x1 = range(5000)
y1 = Calculation(5000)

# График 1
axes[0, 0].set_title("День 1", fontsize = 15)

axes[0, 0].set_xlim(0, 200)
axes[0, 0].set_ylim(0, 5000)

axes[0, 0].set_xticks(np.arange(0, 200, 50))
axes[0, 0].set_yticks(np.arange(0, 5000, 1000))

axes[0, 0].grid()

axes[0, 0].bar(x1, y1, color = "black")

for i in range(99):
    get_mixing_list = MixingPopulation()
    Trading()

x1 = range(1000)
y1 = Calculation(1000)

# График 2
axes[0, 1].set_title("День 100", fontsize = 15)

axes[0, 1].set_xlim(0, 200)
axes[0, 1].set_ylim(0, 1000)

axes[0, 1].set_xticks(np.arange(0, 200, 50))
axes[0, 1].set_yticks(np.arange(0, 1000, 200))

axes[0, 1].grid()

axes[0, 1].bar(x1, y1, color = "black")

for i in range(900):
    get_mixing_list = MixingPopulation()
    Trading()

x1 = range(300)
y1 = Calculation(300)

# # График 3
axes[0, 2].set_title("День 1000", fontsize = 15)

axes[0, 2].set_xlim(0, 300)
axes[0, 2].set_ylim(0, 200)

axes[0, 2].set_xticks(np.arange(0, 300, 50))
axes[0, 2].set_yticks(np.arange(0, 200, 50))

axes[0, 2].grid()

axes[0, 2].bar(x1, y1, color = "black")

for i in range(1000):
    get_mixing_list = MixingPopulation()
    Trading()

x1 = range(300)
y1 = Calculation(300)

# График 4
axes[1, 0].set_title("День 2000", fontsize = 15)

axes[1, 0].set_xlim(0, 300)
axes[1, 0].set_ylim(0, 200)

axes[1, 0].set_xticks(np.arange(0, 300, 50))
axes[1, 0].set_yticks(np.arange(0, 200, 50))

axes[1, 0].grid()

axes[1, 0].bar(x1, y1, color = "black")

for i in range(1000):
    get_mixing_list = MixingPopulation()
    Trading()

x1 = range(400)
y1 = Calculation(400)

# График 5
axes[1, 1].set_title("День 3000", fontsize = 15)

axes[1, 1].set_xlim(0, 400)
axes[1, 1].set_ylim(0, 125)

axes[1, 1].set_xticks(np.arange(0, 400, 50))
axes[1, 1].set_yticks(np.arange(0, 125, 25))

axes[1, 1].grid()

axes[1, 1].bar(x1, y1, color = "black")

for i in range(17000):
    get_mixing_list = MixingPopulation()
    Trading()

x1 = range(500)
y1 = Calculation(500)

# График 6
axes[1, 2].set_title("День 3000", fontsize = 15)

axes[1, 2].set_xlim(0, 500)
axes[1, 2].set_ylim(0, 100)

axes[1, 2].set_xticks(np.arange(0, 500, 50))
axes[1, 2].set_yticks(np.arange(0, 100, 25))

axes[1, 2].grid()

axes[1, 2].bar(x1, y1, color = "black")

end = time.time()
print(f"Затраченное время: {end - start}")
plt.show() # Открыть окно