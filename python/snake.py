import curses
import random
import time


def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(True)
    stdscr.timeout(100)

    sh, sw = stdscr.getmaxyx()
    win = curses.newwin(sh, sw, 0, 0)
    win.keypad(1)

    snake = [(sh // 2, sw // 2), (sh // 2, sw // 2 - 1), (sh // 2, sw // 2 - 2)]
    direction = 1  # 1 = right, 2 = left, 3 = up, 4 = down
    score = 0

    def generate_food():
        while True:
            food = (random.randint(1, sh - 2), random.randint(1, sw - 2))
            if food not in snake:
                return food

    food = generate_food()

    while True:
        key = win.getch()
        if key in (curses.KEY_RIGHT, ord('d')) and direction != 2:
            direction = 1
        elif key in (curses.KEY_LEFT, ord('a')) and direction != 1:
            direction = 2
        elif key in (curses.KEY_UP, ord('w')) and direction != 4:
            direction = 3
        elif key in (curses.KEY_DOWN, ord('s')) and direction != 3:
            direction = 4
        elif key in (ord('q'), 27):
            break

        head_y, head_x = snake[0]
        if direction == 1:
            new_head = (head_y, head_x + 1)
        elif direction == 2:
            new_head = (head_y, head_x - 1)
        elif direction == 3:
            new_head = (head_y - 1, head_x)
        else:
            new_head = (head_y + 1, head_x)

        if (new_head[0] in (0, sh - 1) or new_head[1] in (0, sw - 1) or new_head in snake):
            break

        snake.insert(0, new_head)
        if new_head == food:
            score += 1
            food = generate_food()
        else:
            snake.pop()

        win.erase()
        win.addstr(0, 2, f"Snake (q to quit)  Score: {score}")
        for y, x in snake:
            win.addch(y, x, 'O')
        win.addch(food[0], food[1], '*')
        win.border()
        win.refresh()
        time.sleep(0.08)

    win.erase()
    win.addstr(sh // 2, max(0, sw // 2 - 8), "Game Over! Press q to exit.")
    win.refresh()
    time.sleep(1.5)


if __name__ == "__main__":
    curses.wrapper(main)