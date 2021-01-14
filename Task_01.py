# 1. Написать модуль, содержащий 12 функций по переводу:
# Примечание: функция принимает на вход число и возвращает конвертированное
# число
# 1.1.Дюймы в сантиметры
# 1.2.Сантиметры в дюймы
# 1.3.Мили в километры
# 1.4.Километры в мили
# 1.5.Фунты в килограммы
# 1.6.Килограммы в фунты
# 1.7.Унции в граммы
# 1.8.Граммы в унции
# 1.9.Галлон в литры
# 1.10.Литры в галлоны
# 1.11.Пинты в литры
# 1.12.Литры в пинты

def inchToSm(value: int) -> float:
    return value * 2.54
def smToInch(value: int) -> float:
    return value * 0.39
def mileToKm(value: int) -> float:
    return value * 1.69
def kmToMile(value: int) -> float:
    return value * 0.6214
def poundToKg(value: int) -> float:
    return value * 0.454
def kgToPound(value: int) -> float:
    return value * 2.2
def ounceToGr(value: int) -> float:
    return value * 28.349
def grToOunce(value: int) -> float:
    return value * 0.0352739982605
def gallonToLiter(value: int) -> float:
    return value * 3.785
def literToGallon(value: int) -> float:
    return value * 0.26417
def pintToLiter(value: int) -> float:
    return value * 0,473176
def literToPint(value: int) -> float:
    return value * 1.7597539863927

# Написать программу, со следующим интерфейсом: пользователю предоставляется
# на выбор 12 вариантов перевода(описанных в первой задаче).
# Пользователь вводит цифру от одного до двенадцати.
# После программа запрашивает ввести численное значение.
# Затем программа выдает конвертированный результат.
# Использовать функции из первого задания.
# Программа должна быть в бесконечном цикле. Код выхода из программы - “0.

def Main():
    i = 1
    while i > 0:
        n = int(input('Введите выбранную цифру для начала конвертации: '))
        if n == 1:
            value = int(input('Введите количество дюймов: '))
            print(inchToSm(value), 'см')
        elif n == 2:
            value = int(input('Введите количество сантиметров: '))
            print(smToInch(value), 'дюймов')
        elif n == 3:
            value = int(input('Введите количество миль: '))
            print(mileToKm(value), 'км')
        elif n == 4:
            value = int(input('Введите количество километров: '))
            print(kmToMile(value), 'миль')
        elif n == 5:
            value = int(input('Введите количество фунтов: '))
            print(poundToKg(value), 'кг')
        elif n == 6:
            value = int(input('Введите количество килограммов: '))
            print(kgToPound(value), 'фунтов')
        elif n == 7:
            value = int(input('Введите количество унций: '))
            print(ounceToGr(value), 'гр')
        elif n == 8:
            value = int(input('Введите количество граммов: '))
            print(grToOunce(value), 'унций')
        elif n == 9:
            value = int(input('Введите количество галлонов: '))
            print(gallonToLiter(value), 'литров')
        elif n == 10:
            value = int(input('Введите количество литров: '))
            print(literToGallon(value), 'галлонов')
        elif n == 11:
            value = int(input('Введите количество пинт: '))
            print(pintToLiter(value), 'литров')
        elif n == 12:
            value = int(input('Введите количество литров: '))
            print(literToPint(value), 'пинт')
        elif n > 12:
            print('Введите число от 1 до 12 или 0, что бы остановить конверер')
            continue
        elif n == 0:
            print('Конвертер остановлен')
            break

if __name__ == '__main__':
    Main()
