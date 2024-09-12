n = int(input("ВВедите номер месяца: "))


def month_to_season(n):
    if n == 12 or 0 < n < 3:
        print("Winter")
    elif 2 < n < 6:
        print("Spring")
    elif 5 < n < 9:
        print("Summer")
    elif 8 < n < 12:
        print("Autumn")
    else:
        print('Возможно, Земля сошла с орбиты')


month_to_season(n)
