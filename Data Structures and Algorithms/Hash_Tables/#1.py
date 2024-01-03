"""Hash Tables"""
# Хэш-таблица — это структура данных,
# предназначенная для эффективного хранения пар "ключ-значение".
# Основной принцип: использование хэш-функции для преобразования ключа в индекс массива,
# где хранится значение.
''''Основные операции:'''

class HashTable:
    """Создание хеш-таблиц"""
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return hash(key) % self.size

    '''Добавление элементов в хеш-таблицы'''
    def insert(self, key, value):
        index = self.hash_function(key)
        while self.table[index] is not None:
            stored_key, _ = self.table[index]
            if stored_key == key:
                self.table[index] = (key, value)
                return
            index = (index + 1) % self.size
        self.table[index] = (key, value)
    ''' Поиск элементов в хеш-таблицах'''
    def get(self, key):
        index = self.hash_function(key)
        while self.table[index] is not None:
            stored_key, value = self.table[index]
            if stored_key == key:
                return value
            index = (index + 1) % self.size
        raise KeyError(key)

    ''' Удаление элементов из хеш-таблиц '''
    def remove(self, key):
        index = self.hash_function(key)
        while self.table[index] is not None:
            stored_key, _ = self.table[index]
            if stored_key == key:
                self.table[index] = None
                return
            index = (index + 1) % self.size
        raise KeyError(key)

    ''' Обход хеш-таблиц'''
    def traverse(self):
        for entry in self.table:
            if entry is not None:
                key, value = entry
                print(f"Key: {key}, Value: {value}")

# Пример использования
hash_table = HashTable(5);print(f"1->{hash_table.table}")
# Добавление элемента
hash_table.insert("name", "John")
hash_table.insert("age", 25)
hash_table.insert("city", "New York")
print(f"table->{hash_table.traverse()}")
# Удаление элемента
hash_table.remove("name");print(f"2->{hash_table.table}")
# Поиск элемента
key_to_find = "age"
try:
    value = hash_table.get(key_to_find);print(f"The value for key '{key_to_find}' is {value}.")
except KeyError:
    print(f"Element with key '{key_to_find}' not found.")
# Обход и вывод элементов
hash_table.traverse()

# Дополнения:
"""
1. Хеш-функции:
   - Хеш-функции преобразуют ключ в числовой хэш-код.
   - Обеспечивают равномерное распределение ключей.
   - Примеры: встроенная `hash()`, кастомные функции.

2. Разрешение коллизий:
   - Методы разрешения коллизий, такие как линейное пробирование, квадратичное пробирование и метод цепочек.
   - Коллизии возникают, когда разные ключи получают одинаковый хеш.

3. Преимущества и недостатки:
   - Преимущества: эффективность операций в среднем случае, O(1) для поиска.
   - Недостатки: возможные коллизии, занимаемое пространство.

4. Кастомные хеш-функции:
   - Возможность создавать собственные хеш-функции для специфических типов данных.

5. Работа с коллизиями:
   - Объяснение того, как обрабатываются коллизии, включая линейное пробирование.

6. Отображение и использование в Python:
   - Применение хеш-таблиц в Python, включая встроенные структуры данных, такие как словари.

7. Примеры с кастомными хеш-функциями:
   - Дополнительные примеры кастомных хеш-функций для более сложных сценариев.
"""