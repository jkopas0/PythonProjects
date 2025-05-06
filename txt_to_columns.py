from math import floor, ceil

def txt_to_columns(txt:str) -> None:
    tmp = []
    sizeX = floor(len(txt) ** 0.5)
    sizeY = ceil(len(txt) ** 0.5)

    for x in range(sizeX):
        tmp.append([])
        for y in range(sizeY):
            tmp[x].append(" ")

    i = 0

    for x in range(sizeX - 1, -1, -1):
        for y in range(sizeY):
            if i < len(txt):
                tmp[x][y] = txt[i]
                i += 1

    for y in range(sizeY):
        for x in range(sizeX):
            print(tmp[x][y], end='')
        print()

if __name__ == "__main__":
    txt_to_columns("Sample text")