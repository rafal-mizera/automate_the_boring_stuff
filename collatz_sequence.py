def collatz(number):
    if number % 2 == 0:
        x = number // 2
        print(x)
    else:
        x  = 3 * number + 1
        print(x)
    return x


try:
    number = int(input("Podaj liczbę: "))
    x = collatz(number)

    while x != 1:
        x = collatz(x)
except ValueError:
    print("Podaj liczbę!!!")



