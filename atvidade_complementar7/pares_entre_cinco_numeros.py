nums = int(input())
cont = 0

for i in range(4):
    nums = int(input())
    if nums % 2 == 0:
        cont += 1

print(f"{cont} valores pares")