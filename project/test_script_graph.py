import numpy as np
import matplotlib.pyplot as plt
import random

# Кол-во условий торговли
trade_condition = 1

# Параметры
num_people = 10000
initial_balance = 100
num_days_list = [1, 100, 1000, 2000, 3000, 20000]

# Функция для симуляции торговли
def simulate_trading(num_days):
    balances = np.full(num_people, initial_balance)  # Начальные балансы

    for day in range(num_days):
        # Определяем процент людей, которые будут торговать (от 0% до 30%)
        trade_percentage = np.random.uniform(0.25, 0.35)
        num_trade = int(num_people * trade_percentage)

        # Генерируем случайные индексы для торговли
        traders = np.random.choice(num_people, size=num_trade, replace=False)
        other_people = []
        all_people = np.array([i for i in np.arange(num_people)])
        random.shuffle(all_people)
        for i in all_people:
            if i not in traders: other_people.append(i)
        buyers = [other_people[i] for i in np.arange(num_trade)]
        
        balances = trade(buyers, traders, balances, num_trade, trade_condition)
        # for i in np.arange(num_trade):
        #     if balances[buyers[i]] > 0:
        #         cash_in_trade = 1
        #         if random.randrange(100) == 1: # ошибка терминала
        #             if random.randrange(2) == 1: cash_in_trade -= 1
        #             else: cash_in_trade += 1
                
        #         if np.random.rand() < 0.5:  # 50% шанс на прибыль или убыток
        #             balances[trader] += trade_amount  # Прибыль
        #         else:
        #             balances[trader] -= trade_amount  # Убыток

    return balances

# Функция для построения графиков
def plot_balances(ax, balances, day):
    unique_balances, counts = np.unique(balances, return_counts=True)
    ax.bar(unique_balances, counts, width=1.0, color = "black")
    ax.set_title(f'Распределение балансов после {day} дня(ей)')
    ax.set_xlabel('Баланс (руб.)')
    ax.set_ylabel('Количество людей')
    ax.set_xlim(left=0)  # Ограничиваем ось X от 0
    ax.grid(axis='y')

# Трейд
def trade(buyers, traders, balanc, num_trade, get_condition):
    match get_condition:
        case 0:
            for i in np.arange(num_trade):
                if balanc[buyers[i]] == 0: continue
                
                cash_in_trade = 1
                if random.randrange(100) == 1 and balanc[buyers[i]] > 1: # Ошибка терминала
                    cash_in_trade += 1 
                
                balanc[buyers[i]] -= cash_in_trade
                balanc[traders[i]] += cash_in_trade
        
        case 1:
            for i in np.arange(num_trade):
                if balanc[buyers[i]] == 0: 
                    continue
                elif balanc[buyers[i]] > 3:
                    cash_in_trade = round(balanc[buyers[i]] * np.random.uniform(0.51)) # Сумма перевода от 0 до 51 % баланса
                elif balanc[buyers[i]] <= 3:
                    cash_in_trade = random.randrange(1, 3)
                
                balanc[buyers[i]] -= cash_in_trade
                balanc[traders[i]] += cash_in_trade

    return balanc

# Создаем фигуру и подграфики
fig, axs = plt.subplots(2, 3) #figsize=(15, 12)
axs = axs.flatten()  # Преобразуем в одномерный массив для удобства

# Основной цикл по количеству дней
for i, num_days in enumerate(num_days_list):
    final_balances = simulate_trading(num_days)
    plot_balances(axs[i], final_balances, num_days)
    print(num_days)

# Настраиваем макет и показываем графики
plt.tight_layout()
plt.show()