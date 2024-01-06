'''Iterators'''
# Iterators - это объекты, которые позволяют получать элементы коллекции один за другим,
# без необходимости знать внутреннюю структуру данных. Iterators являются основой для
# реализации цикла for в Python и предоставляют удобный и эффективный способ работы с данными.

''' Протокол итератора:'''
# Метод __iter__() возвращает сам объект итератора.
# Метод __next__() возвращает следующий элемент в последовательности,
#                   генерируя StopIteration при достижении конца.
class SimpleIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1


'''Генераторы'''
# Генератор (Generator): Специальный тип итератора, создаваемый с использованием ключевого слова yield
def simple_generator(start, end):
    current = start
    while current < end:
        yield current
        current += 1

'''Встроенные функции'''
# iter() и next(): Встроенные функции для работы с итераторами.
iterator = iter([1, 2, 3, 4, 5])
element = next(iterator)