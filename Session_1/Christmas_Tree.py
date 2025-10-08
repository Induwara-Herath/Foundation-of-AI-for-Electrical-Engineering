def draw_christmas_tree(n):
    for i in range(n):
        print(" " * (n - i - 1) + "*" * (2 * i + 1))

draw_christmas_tree(5)