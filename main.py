import re


def to_camel_case(text: str) -> str:
    split_text = re.split(r'[_-]', text)
    return split_text[0] + ''.join(word.title() for word in split_text[1:])


class SingletonMeta(type):  # Паттерны проектирования и мета классы как-то выбиваются из общего уровня остальных заданий

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super(SingletonMeta, cls).__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


count_bits = lambda n: bin(n).count('1')  # тут просто поправил отсутствие аргумента у lamda
count_bits2 = lambda n: len(bin(n))-2  # хотя исходя из смысла имени должно быть как-то так


def count_bits3(n: int) -> int:
    """
    Ну а вообще PEP8 ругается на присвоение переменной lamda функции,
    так как не для того она придумана и все это усложняет чтение кода.
    """
    return len(bin(n))-2


def digital_root(n: int) -> int:
    return n if n < 10 else digital_root(sum(map(int, str(n))))
# тут главное помнить об ограничение глубины рекурсии хотя тут оно явно не грозит,
# но вот просто так на всякий случай версия без рекурсии.


def digital_root2(n: int) -> int:
    while n > 10:
        n = sum(map(int, str(n)))
    return n


even_or_odd = lambda number: "Even" if number % 2 == 0 else "Odd"
even_or_odd2 = lambda number: "Odd" if number % 2 else "Even"


def even_or_odd3(number: int) -> str: return "Odd" if number % 2 else "Even"  # если очень хочется одной строкой


print(to_camel_case('text1_text2-text3-text4__text5'))

nn = 10
print(bin(nn))
print(count_bits(nn))
print(count_bits2(nn))
print(count_bits3(nn))


nnn = (2**64)**(2**7)+1

print(digital_root(nnn))
print(digital_root2(nnn))

print(even_or_odd(nnn))
print(even_or_odd2(nnn))


