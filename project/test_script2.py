import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Функция для генерации графика
def generate_plot():
    # Здесь вы можете добавить логику для генерации графика
    plt.clf()  # Очистка текущего графика
    x = [1, 2, 3, 4, 5]
    y = [1, 4, 9, 16, 25]
    plt.plot(x, y)
    plt.title("Пример графика")
    plt.xlabel("X")
    plt.ylabel("Y")
    canvas.draw()

# Создание основного окна
app = ctk.CTk()
app.title("Программа с графиком")
app.geometry("800x600")

# Заголовок
header_label = ctk.CTkLabel(app, text="Заголовок программы", font=("Arial", 20))
header_label.pack(pady=10)

# Создание фрейма для input и label
left_frame = ctk.CTkFrame(app)
left_frame.pack(side="left", fill="both", expand=True, padx=30, pady=20)

# Создание input строк с label
for i in range(2):
    label = ctk.CTkLabel(left_frame, text=f"Input {i + 1}:")
    label.pack(pady=(10, 0))
    entry = ctk.CTkEntry(left_frame)
    entry.pack(pady=(0, 10), fill="x")  # Растягиваем по оси X

# Создание ползунка
slider_label = ctk.CTkLabel(left_frame, text="Ползунок (1-9, шаг 3):")
slider_label.pack(pady=(10, 0))
slider = ctk.CTkSlider(left_frame, from_=1, to=9, number_of_steps=3)
slider.pack(pady=(0, 10), fill="x")  # Растягиваем по оси X

# Создание фрейма для графика и кнопки
graph_frame = ctk.CTkFrame(app)
graph_frame.pack(side="right", fill="both", expand=True)

# Создание области для графика с увеличенной высотой
fig, ax = plt.subplots(figsize=(5, 7))  # Увеличена высота графика
canvas = FigureCanvasTkAgg(fig, master=graph_frame)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack(side="top", fill="both", expand=True)

# Кнопка "Генерировать"
generate_button = ctk.CTkButton(graph_frame, text="Генерировать", command=generate_plot)
generate_button.pack(side="bottom", fill="x", expand=True, pady=10)  # Растягиваем по обеим осям

# Запуск основного цикла приложения
app.mainloop()