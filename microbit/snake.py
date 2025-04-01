
snake = [2, 2]
snakeHist = [snake]
snakeDir = 0

item = [randint(0, 4), randint(0, 4)]

score = 0

def render():
    basic.clear_screen()

    led.plot(snake[0], snake[1])
    led.plot_brightness(item[0], item[1], 32)

    pause(10)

def movement():
    global snake

    if snakeDir == 0:
        snake[1] -= 1
    elif snakeDir == 1:
        snake[0] += 1
    elif snakeDir == 2:
        snake[1] += 1
    elif snakeDir == 3:
        snake[0] -= 1
        
    if snake[0] < 0:
        snake[0] = 4
    elif snake[0] > 4:
        snake[0] = 0
    if snake[1] < 0:
        snake[1] = 4
    elif snake[1] > 4:
        snake[1] = 0

    pause(500)

def items():
    global item, score

    if snake[0] == item[0] and snake[1] == item[1]:
        score += 1

    while snake[0] == item[0] and snake[1] == item[1]:
        item = [randint(0, 4), randint(0, 4)]

    pause(500)


def on_button_pressed_a():
    global snakeDir

    if snakeDir != 0:
        snakeDir -= 1
    else:
        snakeDir = 3

def on_button_pressed_b():
    global snakeDir

    if snakeDir != 3:
        snakeDir += 1
    else:
        snakeDir = 0
        
input.on_button_pressed(Button.A, on_button_pressed_a)
input.on_button_pressed(Button.B, on_button_pressed_b)

forever(render)
forever(movement)
forever(items)
