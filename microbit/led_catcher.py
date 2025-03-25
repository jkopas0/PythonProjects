
playerPos = [2, 4]

items = [[1, -5]]

score = 0

def on_forever():
    basic.plot_leds("""
    . . . . .
    . . . . .
    . . . . .
    . . . . .
    . . . . .
    """)

    led.plot(playerPos[0], playerPos[1])

    for item in items:
        led.plot(item[0], item[1])

def itemLogic():
    global items, score

    for item in items:
        if item[1] < 4:
            item[1] += 1
        else:
            items.pop(items.index(item))
            continue

        if item[0] == playerPos[0] and item[1] == playerPos[1]:
            score += 1
            items.pop(items.index(item))
            continue

    basic.pause(200)

def spawnItem():
    global items

    spawnPos = randint(0, 4)

    basic.pause(1000)

    items.append([spawnPos, -5])

def on_button_pressed_a():
    global playerPos

    if playerPos[0] > 0:
        playerPos[0] -= 1
    
def on_button_pressed_b():
    global playerPos

    if playerPos[0] < 4:
        playerPos[0] += 1
    
input.on_button_pressed(Button.A, on_button_pressed_a)
input.on_button_pressed(Button.B, on_button_pressed_b)

forever(on_forever)
forever(itemLogic)
forever(spawnItem)
