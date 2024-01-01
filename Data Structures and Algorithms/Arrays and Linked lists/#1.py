"""'Массивы и Связанные списки (Arrays and Linked lists)"""


'''Массивы (Arrays):'''
# Массив - это структура данных, которая представляет собой упорядоченный
# набор элементов одного типа.
# В Python массивы могут быть представлены с использованием встроенного
# типа данных list или библиотеки array.

# Создание массива:
array_example = [1, 2, 3, 4, 5]
# Доступ к элементам:
first_element = array_example[0]
# Изменение элементов:
array_example[1] = 10
# Длина массива:
length = len(array_example)
# Операции над массивами:
# Срезы: array_example[start:stop]
subset = array_example[1:4]  # Получить подмножество [2, 3, 4]
# Объединение массивов: concatenated_array = array1 + array2
array1 = [1, 2, 3]
array2 = [4, 5, 6]
concatenated_array = array1 + array2  # Получить [1, 2, 3, 4, 5, 6]
# Повторение: repeated_array = array_example * 3
array_example = [1, 2, 3]
repeated_array = array_example * 3  # Получить [1, 2, 3, 1, 2, 3, 1, 2, 3]
#------------------------------------------------------------------------------------
# Связанные списки (Linked Lists):
# Связанный список представляет собой структуру данных, состоящую из узлов,
# каждый из которых содержит данные и ссылку на следующий узел. В Python для
# реализации связанных списков можно использовать собственные классы.

# Определение класса узла:

class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None
# Создание связанного списка:

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node1.next_node = node2
node2.next_node = node3

# Добавление элемента в конец списка:

def append_to_linked_list(head, data):
    new_node = Node(data)
    current = head
    while current.next_node:
        current = current.next_node
    current.next_node = new_node

# Удаление элемента из списка:

def delete_from_linked_list(head, data):
    current = head
    if current.data == data:
        return head.next_node
    while current.next_node:
        if current.next_node.data == data:
            current.next_node = current.next_node.next_node
            return head
        current = current.next_node
    return head

# Проход по списку:

def print_linked_list(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next_node
    print("None")
