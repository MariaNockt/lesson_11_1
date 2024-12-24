import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Часть 1: Анализ данных с помощью Pandas
data = pd.read_excel('Книга1.xlsx')
print("Первые 5 строк данных:")
print(data.head())

average_age = data['Age'].mean()
average_salary = data['Salary'].mean()
print(f"\nСредний возраст: {average_age}")
print(f"Средняя зарплата: {average_salary}")

# Часть 2: Математические операции с помощью NumPy
numbers = np.array([1, 2, 3, 4, 5])
sum_numbers = np.sum(numbers)
mean_numbers = np.mean(numbers)
std_numbers = np.std(numbers)

print("\nРезультаты математических операций с массивом:")
print(f"Сумма: {sum_numbers}")
print(f"Среднее: {mean_numbers}")
print(f"Стандартное отклонение: {std_numbers}")

# Часть 3: Визуализация данных с помощью Matplotlib
plt.style.use('ggplot')  # Используем стиль ggplot

plt.figure(figsize=(10, 6))

# Используем более приятные оттенки
colors = plt.cm.plasma(np.linspace(0, 1, len(data['Name'])))
bars = plt.bar(data['Name'], data['Salary'], color=colors, edgecolor='black', linewidth=1.2)
# Добавляем аннотации на столбцы
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, f'{yval}', ha='center', va='bottom', fontsize=10, color='black')

plt.title('Зарплата сотрудников', fontsize=18, fontweight='bold')
plt.xlabel('Имя', fontsize=14)
plt.ylabel('Зарплата', fontsize=14)
plt.axhline(average_salary, color='red', linestyle='--', label='Средняя зарплата', linewidth=2)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)  # Добавляем сетку для лучшей читаемости
plt.xticks(rotation=45)  # Поворачиваем подписи по оси X для лучшей читаемости
plt.tight_layout()  # Автоматически подгоняем параметры графика
plt.show()