import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Функция для создания графика
def create_plot():
    try:
        # Получаем значения из полей ввода
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        num3 = float(slider.get())
        
        plt.style.use('ggplot')# Стиль

 # Создаем график

        fig.clear()  # Очищаем предыдущий график

        # Создаем 6 подграфиков
        ax1 = fig.add_subplot(2, 3, 1)
        ax2 = fig.add_subplot(2, 3, 2)
        ax3 = fig.add_subplot(2, 3, 3)
        ax4 = fig.add_subplot(2, 3, 4)
        ax5 = fig.add_subplot(2, 3, 5)
        ax6 = fig.add_subplot(2, 3, 6)

        # Пример данных для подграфиков
        data = [num1, num2, num3]

        # Заполняем подграфики
        ax1.bar(['Input 1'], [num1], color='blue')
        ax1.set_title('Input 1')

        ax2.bar(['Input 2'], [num2], color='green')
        ax2.set_title('Input 2')

        ax3.bar(['Input 3'], [num3], color='red')
        ax3.set_title('Input 3')

        ax4.bar(['Input 1', 'Input 2', 'Input 3'], data, color='purple')
        # ax4.set_title('Combined Inputs')

        ax5.plot([1, 2, 3], [num1, num2, num3], marker='o', color='orange')
        # ax5.set_title('Line Plot of Inputs')

        ax6.pie(data, labels=['Input 1', 'Input 2', 'Input 3'], autopct='%1.1f%%')
        # ax6.set_title('Pie Chart of Inputs')

        # Обновляем график

        plt.tight_layout()  # Уплотняем подграфики
        canvas.draw()
    except ValueError:
        print("Пожалуйста, введите корректные числа.")

# Создаем главное окно
app = ctk.CTk()
app.title("Simulator of Social Inequality")
app.geometry("800x400")

# Устанавливаем системную тему
ctk.set_appearance_mode("System")

# Заголовок
header_label = ctk.CTkLabel(app, text="Симулятор социального неравенства", font=("Arial", 20))
header_label.pack(pady=10)

# Фрейм для центрирования
center_frame = ctk.CTkFrame(app)
center_frame.pack(expand=True, fill="both")

# Фрейм для полей ввода
input_frame = ctk.CTkFrame(center_frame, width=200)  # Ширина фрейма для ввода
input_frame.pack(side="left", padx=15, pady=20, fill="both")

# Метки и поля ввода
label1 = ctk.CTkLabel(input_frame, text="Количество людей:")
label1.pack(pady=5)

entry1 = ctk.CTkEntry(input_frame, placeholder_text="Рекомендуем от 6000 до 10000")
entry1.pack(pady=5, fill="x")

label2 = ctk.CTkLabel(input_frame, text="Количество дней:")
label2.pack(pady=5)

entry2 = ctk.CTkEntry(input_frame, placeholder_text="Рекомундуем от 100 до 15000")
entry2.pack(pady=5, fill="x")

slider_label = ctk.CTkLabel(input_frame, text="Количество графиков (от 1 до 9):")
slider_label.pack(pady=5)

slider = ctk.CTkSlider(input_frame, from_=1, to=9, number_of_steps=3)
slider.set(1)
slider.pack(pady=5, fill="x")  # Растягиваем по оси X

# Создаем область для графика и кнопки
plot_frame = ctk.CTkFrame(center_frame)
plot_frame.pack(side="left", padx=20, pady=20, fill="both", expand=True)

# Создаем область для графика
fig = plt.Figure(figsize=(5, 3), dpi=100)
canvas = FigureCanvasTkAgg(fig, master=plot_frame)
canvas.get_tk_widget().pack(fill="both", expand=True)

# Кнопка для создания графика
create_button = ctk.CTkButton(plot_frame, text="Генерировать графики", command=create_plot)
create_button.pack(fill="both")  # Размещаем кнопку под графиком

# Запускаем главный цикл приложения
app.mainloop()