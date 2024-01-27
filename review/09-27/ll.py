class Node():
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList():
    def __init__(self, value):
        new_node = Node(value)
        self.length = 1
        self.head = new_node
        self.tail = new_node

    def print_list(self):
        tmp = self.head
        while tmp is not None:
            print(tmp.value)
            tmp = tmp.next

    def append(self, value):
        new_node = Node(value)
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1


foo = LinkedList(5)

foo.append(14)

foo.print_list()