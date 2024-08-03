import matplotlib.pyplot as plt
import colorsys

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.pos = (0, 0)  # Позиція вузла на графіку

def array_to_tree(array, i=0, x=0, y=0, dx=1):
    if i >= len(array) or array[i] is None:
        return None

    node = Node(array[i])
    node.pos = (x, y)

    left_index = 2 * i + 1
    right_index = 2 * i + 2

    node.left = array_to_tree(array, left_index, x - dx, y - 1, dx / 2)
    node.right = array_to_tree(array, right_index, x + dx, y - 1, dx / 2)

    return node

def plot_tree(node, ax):
    if node is not None:
        x, y = node.pos
        ax.scatter(x, y, color=node.color, s=1000, zorder=2)
        ax.text(x, y, node.val, ha='center', va='center', fontsize=12, zorder=3)
        
        if node.left:
            lx, ly = node.left.pos
            ax.plot([x, lx], [y, ly], color='black', zorder=1)
            plot_tree(node.left, ax)
        
        if node.right:
            rx, ry = node.right.pos
            ax.plot([x, rx], [y, ry], color='black', zorder=1)
            plot_tree(node.right, ax)

def draw_tree(tree_root, traversal_type):
    plt.close('all')  # Закриваємо всі попередні вікна
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_aspect('equal')
    ax.axis('off')
    
    ax.set_title(f'Traversal Type: {traversal_type}', fontsize=16)

    plot_tree(tree_root, ax)
    plt.draw()  # Малюємо оновлений графік
    plt.pause(1)  # Додаємо паузу, щоб бачити зміни

def get_color(index, total):
    hue = index / total
    lightness = 0.3 + 0.6 * (index / total)  # Від темного до світлого
    rgb = colorsys.hls_to_rgb(hue, lightness, 1.0)
    hex_color = '#{:02x}{:02x}{:02x}'.format(int(rgb[0] * 255), int(rgb[1] * 255), int(rgb[2] * 255))
    return hex_color

def bfs(tree_root):
    plt.ion()  # Включаємо інтерактивний режим
    queue = [tree_root]
    order = 0
    nodes_count = count_nodes(tree_root)
    
    while queue:
        current = queue.pop(0)
        current.color = get_color(order, nodes_count)
        order += 1
        
        draw_tree(tree_root, 'BFS')
        
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    plt.ioff()  # Вимикаємо інтерактивний режим
    plt.show()  # Відображаємо остаточний графік

def dfs(tree_root):
    plt.ion()  # Включаємо інтерактивний режим
    stack = [tree_root]
    order = 0
    nodes_count = count_nodes(tree_root)
    
    while stack:
        current = stack.pop()
        current.color = get_color(order, nodes_count)
        order += 1
        
        draw_tree(tree_root, 'DFS')
        
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)

    plt.ioff()  # Вимикаємо інтерактивний режим
    plt.show()  # Відображаємо остаточний графік

def count_nodes(node):
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)

if __name__ == "__main__":
    # Приклад масиву, що представляє бінарну купу
    heap_array = [0, 4, 1, 5, 10, 3]

    # Перетворення масиву в дерево
    heap_tree_root = array_to_tree(heap_array)

    print("BFS (обхід в ширину):")
    bfs(heap_tree_root)

    # Перетворення масиву в дерево знову для DFS, щоб почати з чистого дерева
    heap_tree_root = array_to_tree(heap_array)

    print("DFS (обхід в глибину):")
    dfs(heap_tree_root)
