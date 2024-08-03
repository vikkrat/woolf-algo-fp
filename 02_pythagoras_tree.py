import turtle

def draw_branch(branch_length, depth):
    if depth == 0:
        return

    turtle.forward(branch_length)
    turtle.left(45)
    draw_branch(branch_length * 0.7, depth - 1)
    turtle.right(90)
    draw_branch(branch_length * 0.7, depth - 1)
    turtle.left(45)
    turtle.backward(branch_length)

def draw_pythagoras_tree(level):
    turtle.speed("fastest")
    turtle.left(90)
    turtle.up()
    turtle.backward(200)
    turtle.down()
    turtle.color("brown")

    draw_branch(100, level)
    turtle.done()

if __name__ == "__main__":
    level = int(input("Введіть рівень рекурсії для дерева Піфагора: "))
    draw_pythagoras_tree(level)
