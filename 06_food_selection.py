import random
import pandas as pd
from tabulate import tabulate
from termcolor import colored

def greedy_algorithm(items, budget):
    items_sorted = sorted(items.items(), key=lambda item: item[1]['calories'] / item[1]['cost'], reverse=True)
    total_cost = 0
    total_calories = 0
    chosen_items = []

    for item, details in items_sorted:
        if total_cost + details['cost'] <= budget:
            chosen_items.append(item)
            total_cost += details['cost']
            total_calories += details['calories']

    return chosen_items, total_calories, total_cost

def dynamic_programming(items, budget):
    item_list = list(items.items())
    n = len(item_list)
    
    dp = [[0] * (budget + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        item_name, item_details = item_list[i - 1]
        item_cost = item_details['cost']
        item_calories = item_details['calories']
        
        for w in range(budget + 1):
            if item_cost <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - item_cost] + item_calories)
            else:
                dp[i][w] = dp[i - 1][w]
    
    chosen_items = []
    w = budget
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            item_name = item_list[i - 1][0]
            chosen_items.append(item_name)
            w -= item_list[i - 1][1]['cost']
    
    chosen_items.reverse()
    total_calories = dp[n][budget]
    total_cost = sum(items[item]['cost'] for item in chosen_items)
    
    return chosen_items, total_calories, total_cost

if __name__ == "__main__":
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350}
    }

    budgets = [random.randint(50, 150) for _ in range(2)]

    data = {
        "Budget": [],
        "Greedy Items": [],
        "Greedy Calories": [],
        "Greedy Cost": [],
        "DP Items": [],
        "DP Calories": [],
        "DP Cost": []
    }

    for budget in budgets:
        g_items, g_calories, g_cost = greedy_algorithm(items, budget)
        dp_items, dp_calories, dp_cost = dynamic_programming(items, budget)

        data["Budget"].append(budget)
        data["Greedy Items"].append(", ".join(g_items))
        data["Greedy Calories"].append(g_calories)
        data["Greedy Cost"].append(g_cost)
        data["DP Items"].append(", ".join(dp_items))
        data["DP Calories"].append(dp_calories)
        data["DP Cost"].append(dp_cost)

    df = pd.DataFrame(data)

    # Для кольорового виведення в термінал
    print()
    print(colored("Greedy Algorithm", "cyan"))
    print(tabulate(df[["Budget", "Greedy Items", "Greedy Calories", "Greedy Cost"]], headers='keys', tablefmt='pretty', showindex=False, colalign=["center"] * 4))

    print()
    print(colored("Dynamic Programming", "green"))
    print(tabulate(df[["Budget", "DP Items", "DP Calories", "DP Cost"]], headers='keys', tablefmt='pretty', showindex=False, colalign=["center"] * 4))
