import matplotlib.pyplot as plt

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

def draw_tree(tree_root):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_aspect('equal')
    ax.axis('off')

    plot_tree(tree_root, ax)
    plt.show()

if __name__ == "__main__":
    # Приклад масиву, що представляє бінарну купу
    heap_array = [0, 4, 1, 5, 10, 3]

    # Перетворення масиву в дерево
    heap_tree_root = array_to_tree(heap_array)

    # Відображення дерева
    draw_tree(heap_tree_root)
