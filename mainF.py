#task1
# def gcd(a, b):
#     if b == 0:
#         return a
#     else:
#         return gcd(b, a % b)

# num1 = 48
# num2 = 18
# result = gcd(num1, num2)
# print("Найбільший спільний дільник чисел {} і {}: {}".format(num1, num2, result))

#task2
# import random

# def generate_secret_number():
#     digits = list(range(10))
#     random.shuffle(digits)
#     return ''.join(map(str, digits[:4]))

# def count_bulls_and_cows(secret, guess):
#     bulls = sum(s == g for s, g in zip(secret, guess))
#     cows = sum((min(secret.count(d), guess.count(d)) for d in set(guess))) - bulls
#     return bulls, cows

# def play_game(secret, attempts=0):
#     guess = input("Введіть ваше число (4 різні цифри): ")
#     if not guess.isdigit() or len(guess) != 4 or len(set(guess)) != 4:
#         print("Введіть коректне 4-значне число з різними цифрами.")
#         return play_game(secret, attempts)
    
#     attempts += 1
#     bulls, cows = count_bulls_and_cows(secret, guess)
#     print(f"Бики: {bulls}, Корови: {cows}")

#     if bulls == 4:
#         print(f"Ви виграли! Відгадане число: {secret}. Кількість спроб: {attempts}")
#         return
#     else:
#         return play_game(secret, attempts)

# def main():
#     secret_number = generate_secret_number()
#     play_game(secret_number)

# if __name__ == "__main__":
#     main()

#task3
# def is_valid_move(x, y, board):
#     return 0 <= x < len(board) and 0 <= y < len(board) and board[x][y] == -1

# def print_board(board):
#     for row in board:
#         print(' '.join(f'{cell:2}' for cell in row))
#     print()

# def solve_knights_tour(n, start_x, start_y):
 
#     board = [[-1 for _ in range(n)] for _ in range(n)]


#     moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]

  
#     board[start_x][start_y] = 0

#     def solve(x, y, move_i):
#         if move_i == n * n:
#             return True

#         for move in moves:
#             next_x, next_y = x + move[0], y + move[1]
#             if is_valid_move(next_x, next_y, board):
#                 board[next_x][next_y] = move_i
#                 if solve(next_x, next_y, move_i + 1):
#                     return True
#                 board[next_x][next_y] = -1

#         return False

#     if solve(start_x, start_y, 1):
#         print_board(board)
#     else:
#         print("Немає рішення для даної початкової позиції.")

# def main():
#     n = 6 
#     start_x = int(input("Введіть початкову координату x (0-5): "))
#     start_y = int(input("Введіть початкову координату y (0-5): "))
#     solve_knights_tour(n, start_x, start_y)

# if __name__ == "__main__":
#     main()

#task4
# import random

# def create_board():
#     numbers = list(range(1, 16))
#     numbers.append(None)
#     random.shuffle(numbers)
#     board = [numbers[i:i+4] for i in range(0, 16, 4)]
#     return board

# def print_board(board):
#     for row in board:
#         print(' '.join(f'{num:2}' if num else ' .' for num in row))
#     print()

# def find_empty(board):
#     for i, row in enumerate(board):
#         for j, num in enumerate(row):
#             if num is None:
#                 return i, j

# def move_tile(board, direction):
#     empty_x, empty_y = find_empty(board)
#     if direction == 'w' and empty_x < 3:
#         board[empty_x][empty_y], board[empty_x+1][empty_y] = board[empty_x+1][empty_y], board[empty_x][empty_y]
#     elif direction == 's' and empty_x > 0:
#         board[empty_x][empty_y], board[empty_x-1][empty_y] = board[empty_x-1][empty_y], board[empty_x][empty_y]
#     elif direction == 'a' and empty_y < 3:
#         board[empty_x][empty_y], board[empty_x][empty_y+1] = board[empty_x][empty_y+1], board[empty_x][empty_y]
#     elif direction == 'd' and empty_y > 0:
#         board[empty_x][empty_y], board[empty_x][empty_y-1] = board[empty_x][empty_y-1], board[empty_x][empty_y]

# def is_solved(board):
#     solution = list(range(1, 16))
#     solution.append(None)
#     flat_board = [num for row in board for num in row]
#     return flat_board == solution

# def main():
#     board = create_board()
#     while not is_solved(board):
#         print_board(board)
#         move = input("Введіть напрямок (w: вгору, s: вниз, a: вліво, d: вправо): ")
#         move_tile(board, move)
#     print("Вітаємо! Ви вирішили головоломку.")
#     print_board(board)

# if __name__ == "__main__":
#     main()
