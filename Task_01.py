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
