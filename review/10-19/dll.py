class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self, reverse=False):
        if reverse:
            temp = self.tail
        else:
            temp = self.head
        while temp is not None:
            print(temp.value)
            if reverse:
                temp = temp.prev
            else:
                temp = temp.next

    def append(self, value):
        new_node = Node(value)
        temp = self.tail
        temp.next = new_node
        new_node.prev = temp
        self.tail = new_node
        self.length += 1
        if self.head is None:
            self.head = new_node

dll = DoublyLinkedList(5)

dll.append(6)
dll.append(19)
dll.append(4000)

dll.print_list(reverse=True)
