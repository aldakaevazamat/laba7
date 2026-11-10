import math
import turtle as tr


def draw_axes(x_min, x_max, y_min, y_max):
    tr.pencolor("black")
    tr.pensize(2)
    # Ось X
    tr.penup();
    tr.goto(x_min, 0);
    tr.pendown();
    tr.goto(x_max, 0);
    tr.stamp()
    # Ось Y
    tr.penup();
    tr.goto(0, y_min);
    tr.pendown();
    tr.goto(0, y_max);
    tr.stamp()


def main():
    # Ввод данных (упрощенный)
    x_start = -2.0
    x_end = 3.0
    dx = 0.5
    eps = 0.0001

    # Настройка окна
    tr.setup(width=800, height=600)
    tr.title("Лабораторная №7. Задание 3: Ряд Тейлора")
    tr.setworldcoordinates(x_start - 1, -1, x_end + 1, math.exp(-x_start) + 2)

    tr.speed(0)
    tr.ht()

    # Рисуем оси
    draw_axes(x_start - 1, x_end + 1, -1, math.exp(-x_start) + 2)

    # --- 1. Рисуем точную функцию (гладкая линия) ---
    tr.penup()
    tr.pencolor("blue")
    tr.pensize(2)
    x_plot = x_start
    while x_plot <= x_end:
        y_plot = math.exp(-x_plot)
        tr.goto(x_plot, y_plot)
        tr.pendown()
        x_plot += 0.05
    tr.penup()

    # --- 2. Рисуем точки, вычисленные Рядом Тейлора ---
    tr.pencolor("red")
    tr.shape("circle")
    tr.shapesize(0.5)  # Чтобы точки были заметны

    x = x_start
    while x <= x_end:
        n = 0
        current_term = 1.0
        sum_y = 0.0

        # Вычисление ряда
        while abs(current_term) > eps:
            sum_y += current_term
            n += 1
            current_term *= -x / n

        # Ставим точку
        tr.goto(x, sum_y)
        tr.stamp()

        # Подписываем значения по X
        tr.goto(x, -0.5)
        tr.pencolor("black")
        tr.write(f"{x:.1f}", align="center", font=("Arial", 10, "normal"))
        tr.pencolor("red")

        x += dx

    # Легенда
    tr.goto(-1.5, 5)
    tr.pencolor("blue")
    tr.write("Точная функция e^(-x)", font=("Arial", 12, "bold"))
    tr.goto(-1.5, 4.5)
    tr.pencolor("red")
    tr.write("Точки ряда Тейлора", font=("Arial", 12, "bold"))

    tr.done()


if __name__ == "__main__":
    main()