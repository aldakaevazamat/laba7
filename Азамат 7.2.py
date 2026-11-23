import random
import math
import turtle as tr


def draw_dashed_line(x1, y1, x2, y2, dashes=15):
    """Рисует пунктирную линию от (x1, y1) до (x2, y2)."""
    tr.penup()
    for i in range(dashes):
        t1 = i / dashes
        t2 = (i + 0.5) / dashes
        tr.goto(x1 + (x2 - x1) * t1, y1 + (y2 - y1) * t1)
        tr.pendown()
        tr.goto(x1 + (x2 - x1) * t2, y1 + (y2 - y1) * t2)
        tr.penup()


def main():
    # 1. Настройка графического окна
    tr.setup(width=800, height=800)
    tr.title("Метод Монте-Карло: Фигура №2")
    tr.bgcolor("white")
    tr.tracer(0)

    # Задаем радиус R
    R = 15.0

    # Масштаб окна [-R - margin, R + margin]
    margin = 5
    tr.setworldcoordinates(-R - margin, -R - margin, R + margin, R + margin)

    tr.ht()
    tr.penup()

    # 2. Рисуем оси координат
    tr.pencolor("black")
    tr.pensize(2)

    # Ось X
    tr.goto(-R - 2, 0)
    tr.pendown()
    tr.goto(R + 2, 0)
    tr.penup()
    tr.goto(R + 2.5, -0.5)
    tr.write("X", font=("Arial", 12, "bold"))

    # Ось Y
    tr.goto(0, -R - 2)
    tr.pendown()
    tr.goto(0, R + 2)
    tr.penup()
    tr.goto(0.5, R + 2)
    tr.write("Y", font=("Arial", 12, "bold"))

    # 3. Метод Монте-Карло
    shots_count = 20000
    hits = 0

    for i in range(1, shots_count + 1):
        x = random.uniform(-R, R)
        y = random.uniform(-R, R)

        # Условие 1: Четверть круга во II четверти (x <= 0, y >= 0, x^2 + y^2 <= R^2)
        in_sector = (x <= 0) and (y >= 0) and (x ** 2 + y ** 2 <= R ** 2)

        # Условие 2: Треугольник в IV четверти с вершинами (0,0), (R,0), (R/2, -R)
        # Левая сторона: y >= -2x (при 0 <= x <= R/2)
        # Правая сторона: y >= 2x - 2R (при R/2 <= x <= R)
        in_triangle = (0 <= x <= R) and (y <= 0) and (y >= -2 * x) and (y >= 2 * x - 2 * R)

        is_hit = in_sector or in_triangle

        tr.goto(x, y)
        if is_hit:
            tr.dot(3, "dimgray")
            hits += 1
        else:
            tr.dot(3, "lightgray")

        if i % 1000 == 0:
            tr.update()

    # 4. Рисуем контуры фигуры поверх точек
    tr.pencolor("black")
    tr.pensize(2)

    # Контур квадрата выборки [-R, R] (тонкой рамкой для наглядности)
    tr.pencolor("gray")
    tr.pensize(1)
    tr.goto(-R, -R)
    tr.pendown()
    tr.goto(R, -R)
    tr.goto(R, R)
    tr.goto(-R, R)
    tr.goto(-R, -R)
    tr.penup()

    # Контур четверти круга во II четверти
    tr.pencolor("black")
    tr.pensize(2)
    tr.goto(0, 0)
    tr.pendown()
    tr.goto(0, R)
    tr.setheading(180)
    tr.circle(R, 90)
    tr.goto(0, 0)
    tr.penup()

    # Контур треугольника в IV четверти
    tr.goto(0, 0)
    tr.pendown()
    tr.goto(R, 0)
    tr.goto(R / 2, -R)
    tr.goto(0, 0)
    tr.penup()

    # Вспомогательные пунктирные линии и подписи как на чертеже
    tr.pencolor("black")
    tr.pensize(1)
    draw_dashed_line(R / 2, 0, R / 2, -R, dashes=12)
    draw_dashed_line(0, -R, R / 2, -R, dashes=8)

    tr.goto(R / 2 - 0.8, 0.5)
    tr.write("R/2", font=("Arial", 10, "bold"))
    tr.goto(R - 0.3, 0.5)
    tr.write("R", font=("Arial", 10, "bold"))
    tr.goto(-1.8, -R - 0.4)
    tr.write("-R", font=("Arial", 10, "bold"))

    # 5. Расчет и вывод результатов
    S_square = (2 * R) ** 2
    S_mc = S_square * (hits / shots_count)

    # Точная площадь: четверть круга (pi * R^2 / 4) + треугольник (0.5 * R * R)
    S_real = (math.pi * R ** 2) / 4 + 0.5 * R ** 2
    error_percent = abs(S_real - S_mc) / S_real * 100

    # Вывод текста в свободном правом верхнем углу (I четверть)
    text_x = 1.5
    tr.goto(text_x, R - 1.5)
    tr.pencolor("black")
    tr.write(f"Выстрелов: {shots_count}", font=("Arial", 10, "bold"))

    tr.goto(text_x, R - 3.0)
    tr.write(f"Попаданий: {hits}", font=("Arial", 10, "bold"))

    tr.goto(text_x, R - 4.5)
    tr.pencolor("darkgreen")
    tr.write(f"S (MC): {S_mc:.2f}", font=("Arial", 10, "bold"))

    tr.goto(text_x, R - 6.0)
    tr.pencolor("blue")
    tr.write(f"S (Точная): {S_real:.2f}", font=("Arial", 10, "bold"))

    tr.goto(text_x, R - 7.5)
    tr.pencolor("red")
    tr.write(f"Погрешность: {error_percent:.2f}%", font=("Arial", 10, "bold"))

    tr.update()

    print("--- Метод Монте-Карло для фигуры №2 ---")
    print(f"Радиус R = {R}")
    print(f"Всего точек: {shots_count}")
    print(f"Попаданий: {hits}")
    print(f"Площадь (Монте-Карло): {S_mc:.4f}")
    print(f"Точная площадь: {S_real:.4f}")
    print(f"Погрешность: {error_percent:.2f}%")

    tr.done()


if __name__ == "__main__":
    main()
