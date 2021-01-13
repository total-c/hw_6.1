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

def inchToSm(value):
    result = value * 2.54
    return result
def smToInch(value):
    result = value * 0.39
    return result
def mileToKm(value):
    result = value * 1.69
    return result
def kmToMile(value):
    result = value * 0.6214
    return result
def poundToKg(value):
    result = value * 0.454
    return result
def kgToPound(value):
    result = value * 2.2
    return result
def ounceToGr(value):
    result = value * 28.349
    return result
def grToOunce(value):
    result = value * 0.0352739982605
    return result
def gallonToLiter(value):
    result = value * 3.785
    return result
def literToGallon(value):
    result = value * 0.26417
    return result
def pintToLiter(value):
    result = value * 0,473176
    return result
def literToPint(value):
    result = value * 1.7597539863927
    return result

# Написать программу, со следующим интерфейсом: пользователю предоставляется
# на выбор 12 вариантов перевода(описанных в первой задаче).
# Пользователь вводит цифру от одного до двенадцати.
# После программа запрашивает ввести численное значение.
# Затем программа выдает конвертированный результат.
# Использовать функции из первого задания.
# Программа должна быть в бесконечном цикле. Код выхода из программы - “0.

i = 1
while i > 0:
    n = int(input('Введите выбранную цифру для начала конвертации: '))
    if n == 1:
        value = int(input('Введите количество дюймов: '))
        if __name__ == '__main__':
            result = inchToSm(value)
            print(result, 'см')
    elif n == 2:
        value = int(input('Введите количество сантиметров: '))
        if __name__ == '__main__':
            result = smToInch(value)
            print(result, 'дюймов')
    elif n == 3:
        value = int(input('Введите количество миль: '))
        if __name__ == '__main__':
            result = mileToKm(value)
            print(result, 'км')
    elif n == 4:
        value = int(input('Введите количество километров: '))
        if __name__ == '__main__':
            result = kmToMile(value)
            print(result, 'миль')
    elif n == 5:
        value = int(input('Введите количество фунтов: '))
        if __name__ == '__main__':
            result = poundToKg(value)
            print(result, 'кг')
    elif n == 6:
        value = int(input('Введите количество килограммов: '))
        if __name__ == '__main__':
            result = kgToPound(value)
            print(result, 'фунтов')
    elif n == 7:
        value = int(input('Введите количество унций: '))
        if __name__ == '__main__':
            result = ounceToGr(value)
            print(result, 'гр')
    elif n == 8:
        value = int(input('Введите количество граммов: '))
        if __name__ == '__main__':
            result = grToOunce(value)
            print(result, 'унций')
    elif n == 9:
        value = int(input('Введите количество галлонов: '))
        if __name__ == '__main__':
            result = gallonToLiter(value)
            print(result, 'литров')
    elif n == 10:
        value = int(input('Введите количество литров: '))
        if __name__ == '__main__':
            result = literToGallon(value)
            print(result, 'галлонов')
    elif n == 11:
        value = int(input('Введите количество пинт: '))
        if __name__ == '__main__':
            result = pintToLiter(value)
            print(result, 'литров')
    elif n == 12:
        value = int(input('Введите количество литров: '))
        if __name__ == '__main__':
            result = literToPint(value)
            print(result)
    elif n > 12:
            print('Введите число от 1 до 12 или 0, что бы остановить конверер')
            continue
    elif n == 0:
            print('Конвертер остановлен')
            break
