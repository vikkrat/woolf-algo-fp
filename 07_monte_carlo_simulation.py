import random
import pandas as pd
import matplotlib.pyplot as plt

# Функція для симуляції кидків кубиків
def simulate_dice_throws(num_throws):
    results = [0] * 11  # Суми від 2 до 12 (всього 11 можливих значень)
    
    for _ in range(num_throws):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        sum_dice = die1 + die2
        results[sum_dice - 2] += 1  # Зсув на 2, щоб сумістити з індексом масиву
    
    return results

# Функція для обчислення ймовірностей
def calculate_probabilities(results, num_throws):
    probabilities = [count / num_throws for count in results]
    return probabilities

# Симуляція
num_throws = 1000000
results = simulate_dice_throws(num_throws)
probabilities = calculate_probabilities(results, num_throws)

# Дані для таблиці
sums = list(range(2, 13))
analytical_probabilities = [1/36, 2/36, 3/36, 4/36, 5/36, 6/36, 5/36, 4/36, 3/36, 2/36, 1/36]

data = {
    "Сума": sums,
    "Імовірність (Монте-Карло)": [f"{p:.2%}" for p in probabilities],
    "Аналітична ймовірність": [f"{p:.2%}" for p in analytical_probabilities]
}

df = pd.DataFrame(data)

# Вивід таблиці
print(df)

# Побудова графіка
plt.figure(figsize=(10, 6))
plt.bar(sums, probabilities, color='skyblue', label='Монте-Карло')
plt.plot(sums, analytical_probabilities, color='red', marker='o', linestyle='dashed', label='Аналітична ймовірність')
plt.xlabel('Сума')
plt.ylabel('Імовірність')
plt.title('Ймовірності сум чисел при киданні двох кубиків')
plt.legend()
plt.grid(True)
plt.show()

# Збереження таблиці у файл
df.to_csv("monte_carlo_probabilities.csv", index=False)
