
tmp = []

for n1 in range(2, 10, 2):
    for n2 in range(1, 10):
        for n3 in range(1, 10):
            for n4 in range(1, 5):
                if n1 + n2 + n3 + n4 == 21:
                    tmp.append(f"{n1}{n2}{n3}{n4}")

print(tmp)
