n = int(input("Введите число: "))
f = "Fizz"
b = "Buzz"
c = f+b


def FizzBuzz(n):
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            print(c)
        elif i % 3 == 0:
            print(f)
        elif i % 5 == 0:
            print(b)
        else:
            print(i)


FizzBuzz(n)
