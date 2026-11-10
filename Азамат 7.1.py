import math
import turtle as tr


def calculate_function(x):
    if -10 <= x <= -8:
        return -3.0
    elif -8 < x <= -3:
        return 0.6 * x + 1.8
    elif -3 < x <= 3:
        return -math.sqrt(9 - x ** 2)
    elif 3 < x <= 5:
        return x - 3
    elif 5 < x <= 8:
        return 3.0
    else:
        return None


def draw_axes(x_min, x_max, y_min, y_max):
    tr.pencolor("black")
    tr.pensize(2)

    # Ось X
    tr.penup()
    tr.goto(x_min, 0)
    tr.pendown()
    tr.goto(x_max, 0)
    # Стрелка на оси X
    tr.stamp()  # Используем стандартную стрелку

    # Ось Y
    tr.penup()
    tr.goto(0, y_min)
    tr.pendown()
    tr.goto(0, y_max)
    tr.stamp()

    # Деления и подписи на оси X
    tr.pensize(1)
    tr.penup()
    for i in range(int(x_min), int(x_max) + 1):
        if i == 0: continue
        tr.goto(i, 0)
        tr.pendown()
        tr.goto(i, y_max * 0.02)  # Длина деления
        tr.penup()
        tr.goto(i, y_max * 0.03)
        tr.write(str(i), align="center", font=("Arial", 8, "normal"))

    # Деления и подписи на оси Y
    for i in range(int(y_min), int(y_max) + 1):
        if i == 0: continue
        tr.goto(0, i)
        tr.pendown()
        tr.goto(x_max * 0.02, i)
        tr.penup()
        tr.goto(x_max * 0.03, i - 0.5)
        tr.write(str(i), align="left", font=("Arial", 8, "normal"))


def main():
    # 1. Настройка экрана
    tr.setup(width=800, height=600)
    tr.title("Лабораторная №7. Задание 1: График функции")
    tr.bgcolor("white")

    # Настройка системы координат (чтобы не думать о пикселях)
    # Задаем диапазоны так, чтобы было немного отступа от краев
    x_min, x_max = -12, 10
    y_min, y_max = -6, 6
    tr.setworldcoordinates(x_min, y_min, x_max, y_max)

    # Настройки скорости и формы
    tr.speed(0)  # Максимальная скорость
    tr.shape("arrow")
    tr.shapesize(0.5)
    tr.ht()  # Скрываем саму "черепашку"

    # 2. Рисуем оси
    draw_axes(x_min, x_max, y_min, y_max)

    # 3. Рисуем график
    tr.penup()
    tr.pencolor("blue")
    tr.pensize(2)

    x = -10.0
    step = 0.05  # Мелкий шаг для плавности
    first_point = True

    while x <= 8.0:
        y = calculate_function(x)
        if y is not None:
            tr.goto(x, y)
            if first_point:
                tr.pendown()
                first_point = False
        else:
            tr.penup()
            first_point = True  # Если вышли за пределы, при следующем заходе нужно снова опустить перо
        x += step

    tr.penup()
    tr.goto(-12, 5)
    tr.write("График функции (Лаба 3 №1)", font=("Arial", 14, "bold"))

    tr.done()


if __name__ == "__main__":
    main()
