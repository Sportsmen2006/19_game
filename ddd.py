def print_field(field): #Функция для вывода поля
    print("Текущее состояние игрового поля:") #просто вывод текста
    for row in field: #
        print(" ".join(row))
    print()


def is_valid_pair(field, x1, y1, x2, y2):
    if (x1 == x2 and y1 == y2) or field[x1][y1] == 'X' or field[x2][y2] == 'X':
        return False
    # Получаем значения выбранных клеток
    num1 = field[x1][y1]
    num2 = field[x2][y2]
    # Проверяем, являются ли они одинаковыми или дают в сумме 10
    if num1 == num2 or (int(num1) + int(num2) == 10):
        # Проверяем, что клетки рядом по горизонтали или вертикали, либо разделены зачеркнутыми
        if (x1 == x2 and abs(y1 - y2) == 1) or (y1 == y2 and abs(x1 - x2) == 1):
            return True
        # Проверка через зачеркнутые
        if x1 == x2:  # по горизонтали
            for y in range(min(y1, y2) + 1, max(y1, y2)):
                if field[x1][y] != 'X':
                    return False
            return True
        if y1 == y2:  # по вертикали
            for x in range(min(x1, x2) + 1, max(x1, x2)):
                if field[x][y1] != 'X':
                    return False
            return True
    return False

# Функция для получения координат от пользователя
def get_coordinates():
    while True:
        try:
            x1, y1 = map(int, input("Введите координаты первой цифры (через пробел, например: 0 0): ").split())
            x2, y2 = map(int, input("Введите координаты второй цифры (через пробел, например: 0 1): ").split())
            if all(0 <= coord < 3 for coord in [x1, y1, x2, y2]):
                return x1, y1, x2, y2
            else:
                print("Некорректные координаты. Попробуйте снова.")
        except ValueError:
            print("Некорректный ввод. Введите два числа через пробел.")

# Функция для переписывания оставшихся цифр
def rewrite_field(field):
    new_field = []
    for row in field:
        for num in row:
            if num != 'X':
                new_field.append(num)

    # Дописываем оставшиеся цифры в таблицу
    while len(new_field) < 19:
        new_field.append(' ')

    return [new_field[:9], new_field[9:19]]

# Основной игровой цикл
def play_game():
    # Создаем начальное поле с числами от 1 до 19
    field = [
        [str(i) for i in range(1, 10)],
        [str(i) for i in range(10, 19)],
        [' ' for _ in range(9)]  # Заполняем третий ряд пустыми клетками
    ]

    while True:
        print_field(field)

        # Получаем координаты двух чисел от пользователя
        x1, y1, x2, y2 = get_coordinates()

        # Проверяем возможность вычеркнуть выбранные цифры
        if is_valid_pair(field, x1, y1, x2, y2):
            # Зачеркиваем цифры
            field[x1][y1] = 'X'
            field[x2][y2] = 'X'
        else:
            print("Нельзя вычеркнуть эти цифры. Попробуйте снова.")
        field = rewrite_field(field)
        if all(num == 'X' or num == ' ' for row in field for num in row):
            print("Поздравляем! Вы вычеркнули все цифры.")
            break
play_game()
