import random
import turtle as tr
import math


def draw_target_axes(R):
    tr.pencolor("black")
    tr.pensize(2)

    # Ось X
    tr.penup()
    tr.goto(-R, 0)
    tr.pendown()
    tr.goto(R, 0)
    tr.stamp()

    # Ось Y
    tr.penup()
    tr.goto(0, -R)
    tr.pendown()
    tr.goto(0, R)
    tr.stamp()

    # Контур мишени (для наглядности)
    tr.penup()
    tr.pencolor("gray")
    tr.pensize(1)

    # 1. Четверть круга в левой верхней части
    tr.goto(0, -R)  # Начинаем с нижней точки, чтобы turtle правильно нарисовал дугу
    tr.pendown()
    tr.circle(R,
              90)  # Рисуем дугу от (0,-R) до (-R,0)?? На самом деле turtle.circle(R, 90) от (0,-R) нарисует от (0,-R) до (-R,0)

    # Для точности нарисуем дугу от (0,0) влево-вверх:
    tr.penup()
    tr.goto(0, 0)
    tr.setheading(180)  # Смотрим влево
    tr.pendown()
    tr.circle(R, -90)  # Рисуем дугу влево-вверх (отрицательный угол для правильного направления)

    # 2. Треугольник в правой нижней части
    tr.penup()
    tr.goto(0, 0)
    tr.pendown()
    tr.goto(R, 0)  # Верхняя правая вершина
    tr.goto(R / 2, -R)  # Нижняя вершина (по рисунку)
    tr.goto(0, 0)  # Возвращаемся в центр

    tr.penup()


def main():
    # Настройка окна
    tr.setup(width=700, height=700)
    tr.title("Лабораторная №7. Задание 2: Мишень Монте-Карло")

    # Вводим радиус
    R = 10.0

    # Масштабируем график (добавим отступ, чтобы все влезло)
    margin = 2
    tr.setworldcoordinates(-R - margin, -R - margin, R + margin, R + margin)

    tr.speed(0)
    tr.ht()
    tr.shape("circle")
    tr.shapesize(0.2)
    tr.penup()

    # Рисуем оси и контур
    draw_target_axes(R)

    shots_count = 10000
    hits = 0

    for i in range(shots_count):
        # Генерируем точку
        x = random.uniform(-R, R)
        y = random.uniform(-R, R)

        is_hit = False

        # Проверка для левой верхней четверти (Круг)
        if x <= 0 and y >= 0 and (x ** 2 + y ** 2) <= R ** 2:
            is_hit = True

        # Проверка для правого нижнего треугольника
        # Уравнения сторон треугольника: y = -2x (левая сторона от (0,0) до (R/2,-R))
        #                               y = 2x - 2R (правая сторона от (R,0) до (R/2,-R))
        elif x >= 0 and y <= 0:
            if y >= -2 * x and y >= 2 * x - 2 * R:
                is_hit = True

        # Отрисовка
        tr.goto(x, y)
        if is_hit:
            tr.dot(4, "green")
            hits += 1
        else:
            tr.dot(2, "lightgray")

    # Вывод результатов
    tr.goto(-R, R + 1)
    tr.pencolor("black")
    tr.write(f"Выстрелов: {shots_count}. Попаданий: {hits}", font=("Arial", 14, "bold"))

    # Оценка площади (S_мишени = S_квадрата * (hits/N))
    S_square = (2 * R) ** 2
    S_target = S_square * (hits / shots_count)

    # Точная аналитическая площадь (для сравнения)
    S_exact = R ** 2 * (math.pi / 4 + 0.5)

    tr.goto(-R, R - 0.8)
    tr.write(f"Оценка площади: {S_target:.2f}", font=("Arial", 12, "normal"))
    tr.goto(-R, R - 1.6)
    tr.write(f"Точная площадь: {S_exact:.2f}", font=("Arial", 12, "normal"))

    print(f"--- Завершено ---")
    print(f"Точек: {shots_count}, Попаданий: {hits}")
    print(f"Площадь мишени (Монте-Карло): {S_target:.4f}")
    print(f"Точная площадь: {S_exact:.4f}")

    tr.done()


if __name__ == "__main__":
    main()
