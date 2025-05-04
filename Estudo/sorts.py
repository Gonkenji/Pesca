class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        values = []
        current = self.head
        while current:
            print(current.data)
            values.append(str(current.data))
            current = current.next_node
        return " -> ".join(values)

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next_node:
                current = current.next_node
            current.next_node = new_node

# Teste
lista = LinkedList()
lista.append(10)
lista.append(20)
lista.append(30)

print(lista)  # Saída: 10 -> 20 -> 30

print(lista.data)
