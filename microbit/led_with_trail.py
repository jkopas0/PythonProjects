
grid = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]
pos = [0, 0]
direction = 1

def on_forever():
    global grid, pos
    if direction:
        if pos[0] == 4:
            pos[0] = 0
            if pos[1] == 4:
                pos[1] = 0
            else:
                pos[1] += 1
        else:
            pos[0] += 1
    else:
        if pos[0] == 0:
            pos[0] = 4
            if pos[1] == 0:
                pos[1] = 4
            else:
                pos[1] -= 1
        else:
            pos[0] -= 1

    for y in range(5):
        for x in range(5):
            if grid[y][x] > 0:
                grid[y][x] -= 15

    grid[pos[1]][pos[0]] = 255

    for y in range(5):
        for x in range(5):
            led.plot_brightness(x, y, grid[y][x])

def on_button_pressed_a():
    global direction
    direction = 1

def on_button_pressed_b():
    global direction
    direction = 0
    
input.on_button_pressed(Button.A, on_button_pressed_a)
input.on_button_pressed(Button.B, on_button_pressed_b)

grid[0][0] = 255
led.plot_brightness(0, 0, 255)

basic.forever(on_forever)
