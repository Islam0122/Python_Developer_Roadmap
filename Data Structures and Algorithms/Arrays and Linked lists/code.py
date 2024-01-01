def reverse_array(arr):
    return arr[::-1]


original_array = [1, 2, 3, 4, 5]
reversed_array = reverse_array(original_array)
print(f"Original Array: {original_array}")
print(f"Reversed Array: {reversed_array}")


class FunnyNode:
    def __init__(self, data):
        self.data = data
        self.next_node = None


def print_funny_linked_list(head):
    current = head
    while current:
        print(f"Node with funny data: {current.data}")
        current = current.next_node


funny_node1 = FunnyNode("Ha")
funny_node2 = FunnyNode("Hee")
funny_node3 = FunnyNode("Hoo")

funny_node1.next_node = funny_node2
funny_node2.next_node = funny_node3

print("\nFunny Linked List:")
print_funny_linked_list(funny_node1)
