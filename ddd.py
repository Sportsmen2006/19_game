# Инициализация начального состояния игры
def init_game():
    # Генерируем цифры от 1 до 19
    numbers = [int(digit) for digit in "123456789123456789"]
    return numbers


# Функция для отображения игрового поля
def display_board(board):
    print("\nИгровое поле:")
    for i in range(0, len(board), 9):
        print(' '.join(str(board[j]) if board[j] != 'X' else 'X' for j in range(i, min(i + 9, len(board)))))
    print()


# Проверка, что пара может быть зачеркнута
def is_valid_pair(board, first, second):
    if board[first] == 'X' or board[second] == 'X':
        return False
    if board[first] == board[second] or board[first] + board[second] == 10:
        return True
    return False


# Проверка соседних клеток (горизонтальных и вертикальных) для выбора пары
def are_adjacent(first, second):
    # Соседи по горизонтали или вертикали
    if first == second + 1 or first == second - 1:  # Горизонталь
        return True
    if first == second + 9 or first == second - 9:  # Вертикаль
        return True
    return False


# Получение координат от пользователя
def get_coordinates(board):
    while True:
        try:
            first = int(input("Введите номер первой цифры (от 1 до 19): ")) - 1
            second = int(input("Введите номер второй цифры (от 1 до 19): ")) - 1
            if first < 0 or first >= len(board) or second < 0 or second >= len(board):
                print("Ошибка: указаны неверные позиции.")
            elif not are_adjacent(first, second):
                print("Ошибка: цифры не находятся рядом.")
            elif not is_valid_pair(board, first, second):
                print("Ошибка: цифры не образуют пару.")
            else:
                return first, second
        except ValueError:
            print("Ошибка ввода: введите корректные числа.")


# Обновление игрового поля (зачеркивание выбранной пары)
def update_board(board, first, second):
    board[first] = 'X'
    board[second] = 'X'


# Убираем все "X" и формируем новое игровое поле
def collapse_board(board):
    new_board = [digit for digit in board if digit != 'X']
    while len(new_board) < len(board):
        new_board.append('X')
    return new_board


# Основная игровая функция
def play_game():
    board = init_game()
    display_board(board)

    while 'X' not in board or len(set(board)) > 1:
        first, second = get_coordinates(board)
        update_board(board, first, second)
        board = collapse_board(board)
        display_board(board)

        if board.count('X') == 18:  # Если осталась только одна цифра
            print("Партия окончена! Осталась последняя цифра:", [digit for digit in board if digit != 'X'][0])
            break


if __name__ == "__main__":
    play_game()
