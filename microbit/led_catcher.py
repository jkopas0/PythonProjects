
playerPos = [2, 4]

items = [[randint(1, 3), -5]]

score = 0

death = False
misses = 0

scoreLeds = [
    [0, 0],
    [0, 1],
    [0, 2],
    [0, 3],
    [0, 4],
    [4, 0],
    [4, 1],
    [4, 2],
    [4, 3],
    [4, 4],
]

deathScoreLeds = [
    [0, 1],
    [1, 1],
    [2, 1],
    [3, 1],
    [4, 1],
    [0, 2],
    [1, 2],
    [2, 2],
    [3, 2],
    [4, 2],
]

def render():
    if death:
        basic.pause(1000)
        return
    
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
        
    tmp = []
    tmpScore = score

    if tmpScore >= 1024:
        tmpScore = 1023

    while tmpScore > 0:
        tmp.append(tmpScore % 2)
        tmpScore = tmpScore //2
        
    while len(tmp) < 10:
        tmp.append(0)

    tmp.reverse()

    for i in range(len(tmp)):
        if tmp[i] == 1:
            led.plot(scoreLeds[i][0], scoreLeds[i][1])

    basic.pause(10)

def itemLogic():
    global items, score, death, misses

    if death:
        basic.pause(1000)
        return

    if misses >= 3:
        death = True
    
    for item in items:
        if item[1] < 4:
            item[1] += 1
        else:
            items.pop(items.index(item))
            misses += 1
            continue

        if item[0] == playerPos[0] and item[1] == playerPos[1]:
            score += 1
            items.pop(items.index(item))
            continue

    basic.pause(200)

def spawnItem():
    global items

    if death:
        basic.pause(1000)
        return

    spawnPos = randint(1, 3)

    basic.pause(1000)

    items.append([spawnPos, -5])

def deathScreen():
    if not death:
        basic.pause(10)
        return

    if score >= 1024:
        basic.plot_leds("""
        . . . . .
        . # . # .
        . . . . .
        # . . . #
        . # # # .
        """)
    else:
        basic.plot_leds("""
        # # # # #
        . . . . .
        . . . . .
        . . . . .
        # # # # #
        """)

        tmp = []
        tmpScore = score

        while tmpScore > 0:
            tmp.append(tmpScore % 2)
            tmpScore = tmpScore //2

        while len(tmp) < 10:
            tmp.append(0)

        tmp.reverse()

        for i in range(len(tmp)):
            if tmp[i] == 1:
                led.plot(deathScoreLeds[i][0], deathScoreLeds[i][1])

    basic.pause(1000)

def on_button_pressed_a():
    global playerPos

    if playerPos[0] > 1:
        playerPos[0] -= 1
    
def on_button_pressed_b():
    global playerPos

    if playerPos[0] < 3:
        playerPos[0] += 1
    
input.on_button_pressed(Button.A, on_button_pressed_a)
input.on_button_pressed(Button.B, on_button_pressed_b)

forever(render)
forever(itemLogic)
forever(spawnItem)
forever(deathScreen)
