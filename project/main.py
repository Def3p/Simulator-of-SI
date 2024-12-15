import customtkinter as CTk
import matplotlib.pyplot as plt
import numpy as np
import random
import time

start = time.time()

max_population = 10000
trading_error = 1
calculation_list = []
get_mixing_list = []


def InitPopulation(): # Создание общества
    get_list = np.array([100 for i in np.arange(max_population)])
    return get_list


def RandPercent(percent): # Процент от.. до
    return random.randrange(1, percent) / 100
    
    
def MixingPopulation():
    get_people = np.array([i for i in np.arange(max_population)]) # всего людей
    seller_counter = int(max_population * (random.randrange(23, 34) / 100)) # кол-во продавцов
    shuffle_list = get_people 
    random.shuffle(shuffle_list) # мешаем список
    get_buyer = [shuffle_list[i] for i in np.arange(seller_counter)] # список покупателей
    get_buyer = np.array(get_buyer)
    shuffle_buyers = []
    for i in shuffle_list: 
        if i not in get_buyer and population_list[i] > 0: shuffle_buyers.append(i)
    shuffle_buyers = np.array(shuffle_buyers)
    random.shuffle(shuffle_buyers)
    get_seller = np.array([shuffle_buyers[i] for i in np.arange(seller_counter)])
    get_list = np.array([[get_buyer[i], get_seller[i]] for i in np.arange(get_buyer.size)])
    return get_list


def Trading():
    for people in get_mixing_list: # все трейды
        cash_in_trade = 1 # сумма

        if random.randrange(100) == 1: # ошибка терминала
            if random.randrange(2) == 1: cash_in_trade -= 1
            else: cash_in_trade += 1

        if population_list[people[0]] > 0:
            population_list[people[0]] -= cash_in_trade # - к покупателю
            population_list[people[1]] += cash_in_trade # + к продавцу


def Calculation(scale):
    calculation_list = np.array([0 for i in np.arange(scale)])
    for i in population_list:
        if i < scale:
            calculation_list[i] += 1
    return calculation_list

CTk.set_appearance_mode("System")
CTk.set_default_color_theme("blue")

class App(CTk.CTk):
    def __init__(self):
        super().__init__()

if __name__ == "__main__":
    app = App()
    app.mainloop()

# population_list = InitPopulation()
# print(f"Популяция: {max_population}")


# get_mixing_list = MixingPopulation()
# Trading()

# # Графики

plt.style.use('ggplot')# Стиль


fig, axes = plt.subplots(2, 3) # Разметка окна

# x1 = range(5000)
# y1 = Calculation(5000)

# # График 1
# axes[0, 0].set_title("День 1", fontsize = 15)

# axes[0, 0].set_xlim(0, 200)
# axes[0, 0].set_ylim(0, 5000)

# axes[0, 0].set_xticks(np.arange(0, 200, 50))
# axes[0, 0].set_yticks(np.arange(0, 5000, 1000))

# axes[0, 0].grid()

# axes[0, 0].bar(x1, y1, color = "black", width = 1.0)

# for i in range(99):
#     get_mixing_list = MixingPopulation()
#     Trading()

# x1 = range(700)
# y1 = Calculation(700)

# # График 2
# axes[0, 1].set_title("День 100", fontsize = 15)

# axes[0, 1].set_xlim(0, 200)
# axes[0, 1].set_ylim(0, 700)

# axes[0, 1].set_xticks(np.arange(0, 200, 50))
# axes[0, 1].set_yticks(np.arange(0, 700, 100))

# axes[0, 1].grid()

# axes[0, 1].bar(x1, y1, color = "black", width = 1.0)

# for i in range(900):
#     get_mixing_list = MixingPopulation()
#     Trading()

# x1 = range(300)
# y1 = Calculation(300)

# # # График 3
# axes[0, 2].set_title("День 1000", fontsize = 15)

# axes[0, 2].set_xlim(0, 300)
# axes[0, 2].set_ylim(0, 200)

# axes[0, 2].set_xticks(np.arange(0, 300, 50))
# axes[0, 2].set_yticks(np.arange(0, 200, 50))

# axes[0, 2].grid()

# axes[0, 2].bar(x1, y1, color = "black", width = 1.0)

# for i in range(1000):
#     get_mixing_list = MixingPopulation()
#     Trading()

# x1 = range(300)
# y1 = Calculation(300)

# # График 4
# axes[1, 0].set_title("День 2000", fontsize = 15)

# axes[1, 0].set_xlim(0, 300)
# axes[1, 0].set_ylim(0, 200)

# axes[1, 0].set_xticks(np.arange(0, 300, 50))
# axes[1, 0].set_yticks(np.arange(0, 200, 50))

# axes[1, 0].grid()

# axes[1, 0].bar(x1, y1, color = "black", width = 1.0)

# for i in range(1000):
#     get_mixing_list = MixingPopulation()
#     Trading()

# x1 = range(400)
# y1 = Calculation(400)

# # График 5
# axes[1, 1].set_title("День 3000", fontsize = 15)

# axes[1, 1].set_xlim(0, 400)
# axes[1, 1].set_ylim(0, 125)

# axes[1, 1].set_xticks(np.arange(0, 400, 50))
# axes[1, 1].set_yticks(np.arange(0, 125, 25))

# axes[1, 1].grid()

# axes[1, 1].bar(x1, y1, color = "black", width = 1.0)

# for i in range(17000):
#     get_mixing_list = MixingPopulation()
#     Trading()

# x1 = range(500)
# y1 = Calculation(500)

# # График 6
# axes[1, 2].set_title("День 20000", fontsize = 15)

# axes[1, 2].set_xlim(0, 500)
# axes[1, 2].set_ylim(0, 100)

# axes[1, 2].set_xticks(np.arange(0, 500, 50))
# axes[1, 2].set_yticks(np.arange(0, 100, 25))

# axes[1, 2].grid()

# axes[1, 2].bar(x1, y1, color = "black", width = 1.0)

# end = time.time()
# print(f"Затраченное время: {end - start} секунд")
# plt.show() # Открыть окно