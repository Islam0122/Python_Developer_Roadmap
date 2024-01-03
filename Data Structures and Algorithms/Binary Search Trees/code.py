class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, root, key):
        if root is None:
            return TreeNode(key)
        if key < root.key:
            root.left = self._insert(root.left, key)
        elif key > root.key:
            root.right = self._insert(root.right, key)
        return root

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self._search(root.left, key)
        return self._search(root.right, key)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, root, key):
        if root is None:
            return root
        if key < root.key:
            root.left = self._delete(root.left, key)
        elif key > root.key:
            root.right = self._delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            root.key = self._min_value_node(root.right)
            root.right = self._delete(root.right, root.key)
        return root

    def _min_value_node(self, root):
        current = root
        while current.left is not None:
            current = current.left
        return current


# Пример использования
bst = BinarySearchTree()
keys = [50, 30, 70, 20, 40, 60, 80]

for key in keys:
    bst.insert(key)

# Поиск
search_key = 40
result = bst.search(search_key)
if result:
    print(f"Элемент {search_key} найден в дереве.")
else:
    print(f"Элемент {search_key} не найден в дереве.")

# Удаление
delete_key = 30
bst.delete(delete_key)
print(f"Элемент {delete_key} удален из дерева.")


# -----------------------------------------------------------------------------------------------------------
def binary_search(lst, search_item):
    # Инициализация нижней и верхней границ поиска
    low, high = 0, len(lst) - 1

    # Пока нижняя граница не превысит верхнюю
    while low <= high:
        # Находим средний элемент
        middle = (low + high) // 2
        guess = lst[middle]

        # Если угадали элемент, возвращаем True
        if guess == search_item:
            return True
        # Если угаданный элемент больше искомого, уменьшаем верхнюю границу
        elif guess > search_item:
            high = middle - 1
        # Если угаданный элемент меньше искомого, увеличиваем нижнюю границу
        else:
            low = middle + 1

    # Если элемент не найден
    return False


# Пример использования
lst = [3, 5, 11, 12, 15, 23, 25, 34, 67, 86]
value = 67
result = binary_search(lst, value)

# Вывод результата
if result:
    print("Элемент найден!")
else:
    print("Элемент не найден.")


# -----------------------------------------------------------------------------------------------
def linear_search(lst, search_item):
    for i, item in enumerate(lst):
        if item == search_item:
            return i
    return -1  # Элемент не найден


# Пример использования
data = [3, 8, 4, 1, 9, 5, 2]
target = 4
result = linear_search(data, target)

if result != -1:
    print(f"Элемент {target} найден по индексу {result}.")
else:
    print(f"Элемент {target} не найден.")
