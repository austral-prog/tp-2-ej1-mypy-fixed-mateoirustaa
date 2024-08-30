def is_leap_year() -> bool:

    year: int = int(input('Ingrese un año: '))
    if (year % 4 == 0 and year % 100 != 0) or (year % 100 == 0 and year % 400 ==0):
        print(f'el año {year} es biciesto')
        return True
    else:
        print(f'el año {year} no es biciesto')
        return False

is_leap_year()



