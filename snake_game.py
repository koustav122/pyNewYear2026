
import curses
import time
import random

# Initialize screen
screen = curses.initscr()
curses.curs_set(0)
screen_height, screen_width = screen.getmaxyx()
window = curses.newwin(screen_height, screen_width, 0, 0)
window.keypad(1)
window.timeout(100)

# Snake and food
snake_x = screen_width // 4
snake_y = screen_height // 2
snake = [
    [snake_y, snake_x],
    [snake_y, snake_x - 1],
    [snake_y, snake_x - 2]
]

food = [random.randint(1, screen_height - 2),
        random.randint(1, screen_width - 2)]
window.addch(food[0], food[1], curses.ACS_PI)

key = curses.KEY_RIGHT
score = 0

while True:
    window.border(0)
    window.addstr(0, 2, f" Score: {score} ")

    next_key = window.getch()
    key = key if next_key == -1 else next_key

    # Calculate new head
    new_head = snake[0].copy()
    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1

    # Game over conditions
    if (new_head[0] in [0, screen_height - 1] or
        new_head[1] in [0, screen_width - 1] or
        new_head in snake):
        curses.endwin()
        print("💀 GAME OVER")
        print("Final Score:", score)
        break

    snake.insert(0, new_head)

    # Eat food
    if new_head == food:
        score += 1
        food = [random.randint(1, screen_height - 2),
                random.randint(1, screen_width - 2)]
        window.addch(food[0], food[1], curses.ACS_PI)
    else:
        tail = snake.pop()
        window.addch(tail[0], tail[1], ' ')

    window.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)
