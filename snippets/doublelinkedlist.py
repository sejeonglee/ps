class DLListNode:
    def __init__(self, value):
        self.prev = None
        self.next = None
        self.value = value


class DLListDummyNode:
    def __init__(self):
        self.prev = None
        self.next = None
        self.value = None


class DLList:
    def __init__(self):

        self.head = DLListDummyNode()
        self.tail = DLListDummyNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _at(self, index):
        cursor = self.head
        for _ in range(index):
            cursor = cursor.next
            if isinstance(cursor.next, DLListDummyNode):
                break
        return cursor

    def insert(self, index, data):
        cursor = self._at(index)
        node = DLListNode(data)
        node.prev = cursor
        node.next = cursor.next
        cursor.next.prev = node
        cursor.next = node

    def delete(self, index):
        cursor = self._at(index)
        cursor.next = cursor.next.next
        cursor.next.prev = cursor
        del cursor


def _print_dll(dll):
    cursor = dll.head
    while cursor is not None:
        print(
            f"{cursor.value if isinstance(cursor, DLListNode) else 'DUMMY'} <-> ",
            end="",
        )
        cursor = cursor.next
    print()


def _print_dll_reverse(dll):
    cursor = dll.tail
    while cursor is not None:
        print(
            f"{cursor.value if isinstance(cursor, DLListNode) else 'DUMMY'} <-> ",
            end="",
        )
        cursor = cursor.prev
    print()


if __name__ == "__main__":
    d = DLList()
    d.insert(0, 1)
    d.insert(1, 2)
    d.insert(2, 3)
    d.insert(3, 4)
    d.delete(1)
    d.insert(1, 5)

    _print_dll(d)
    _print_dll_reverse(d)
