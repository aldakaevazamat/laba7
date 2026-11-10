import random
import turtle as tr


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
    tr.goto(0, -R)
    tr.pendown()
    tr.pencolor("gray")
    tr.circle(R)
    tr.penup()


def main():
    # Настройка окна
    tr.setup(width=700, height=700)
    tr.title("Лабораторная №7. Задание 2: Мишень Монте-Карло")

    # Вводим радиус
    R = 10.0  # Зададим жестко для красоты, можете поменять

    # Масштабируем график
    margin = 2
    tr.setworldcoordinates(-R - margin, -R - margin, R + margin, R + margin)

    tr.speed(0)
    tr.ht()
    tr.shape("circle")
    tr.shapesize(0.2)  # Делаем точки маленькими
    tr.penup()

    # Рисуем оси и контур
    draw_target_axes(R)

    shots_count = 10000  # В задании просят до 10000
    hits = 0

    for i in range(shots_count):
        # Генерируем точку
        x = random.uniform(-R, R)
        y = random.uniform(-R, R)

        is_hit = False
        # Условия попадания из вашего кода
        if x <= 0 and y >= 0 and (x ** 2 + y ** 2) <= R ** 2:
            is_hit = True
        elif x >= 0 and y <= 0 and x <= R and y >= (x - R):
            is_hit = True

        # Отрисовка
        tr.goto(x, y)
        if is_hit:
            tr.dot(4, "green")  # Попадание
            hits += 1
        else:
            tr.dot(2, "lightgray")  # Промах

    # Вывод результатов
    tr.goto(-R, R + 1)
    tr.pencolor("black")
    tr.write(f"Выстрелов: {shots_count}. Попаданий: {hits}", font=("Arial", 14, "bold"))

    # Оценка площади (S_мишени = S_квадрата * (hits/N))
    S_square = (2 * R) ** 2
    S_target = S_square * (hits / shots_count)

    tr.goto(-R, R - 0.5)
    tr.write(f"Оценка площади Монте-Карло: {S_target:.2f}", font=("Arial", 12, "normal"))

    print(f"--- Завершено ---")
    print(f"Точек: {shots_count}, Попаданий: {hits}")
    print(f"Площадь мишени (Монте-Карло): {S_target:.4f}")

    tr.done()


if __name__ == "__main__":
    main()
