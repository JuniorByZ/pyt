# Errors and Exceptions
from os import system
system("cls")
print("...LAMBDA...")
print("-"*15)

# Syntax Error
# x = -5
# if x < 0:
#    raise Exception('x should be positive') """
#""" assert(x >= 0) """
""" try:
    a = 5/1
    b = a + 10
# except Exception as e:
#    print(e, "error !...")

except ZeroDivisionError as e:
    print(e)
    print('Sayı 0\'a bölünemez!...')
except TypeError as e:
    print(e)
    print('Sayı ile String Toplanamaz !...')
else:
    print('Herşey Kontrol Edildi !...')
    print('Sorun Bulunamadı !...')
finally:
    print('Gerekli Düzenlemeler Yapılıyor !...') """


class ValueTooHighError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value


class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value


def test_value(x):
    if x > 100:
        raise ValueTooHighError('Value is too big', x)
    if x < 5:
        raise ValueTooSmallError('Value is too small', x)


try:
    test_value(4)
except ValueTooHighError as e:
    print(e.message, e.value)
except ValueTooSmallError as e:
    print(e.message, e.value)
