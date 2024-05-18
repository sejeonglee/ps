from typing import Any, Optional


class DLListNode:
    """
    Node for double linked list
    contains value, prev and next"""

    def __init__(self, value, container):
        """
        Initialization of node, requires value
        """
        self.prev: Optional[DLListNode] = None
        self.next: Optional[DLListNode] = None
        self.value: Any = value
        self.container = container

    def self_pop(self):
        """
        Delete itself from the list.
        In detail, it connects prev and next node
        except the node itself.
        """
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev
        self.container.length -= 1
        return self.value

    def insert_next_to(self, value):
        new_node = DLListNode(value, self.container)
        new_node.prev = self
        new_node.next = self.next
        if self.next:
            self.next.prev = new_node
        self.next = new_node
        self.container.length += 1

        return new_node

    def insert_prev_to(self, value):
        new_node = DLListNode(value, self.container)
        new_node.prev = self.prev
        new_node.next = self
        if self.prev:
            self.prev.next = new_node
        self.prev = new_node
        self.container.length += 1
        return new_node


class DLListDummyNode(DLListNode):
    """
    Dummy node for double linked list
    for head and tail
    """

    def __init__(self, container):
        self.prev: Optional[DLListNode] = None
        self.next: Optional[DLListNode] = None
        self.value: None = None
        self.container = container

    def self_pop(self):
        raise ValueError("Dummy node cannot be deleted")


class DLList:
    def __init__(self):

        self.head = DLListDummyNode(self)
        self.tail = DLListDummyNode(self)
        self.head.next = self.tail
        self.tail.prev = self.head

        self.length = 0

    def append_head(self, value):
        new_node = self.head.insert_next_to(value)

        return new_node

    def append_tail(self, value):
        new_node = self.tail.insert_prev_to(value)

        return new_node

    def pop_head(self):
        if self.head.next == self.tail:
            raise ValueError("List is empty")
        if self.head.next:
            value = self.head.next.self_pop()

        return value

    def pop_tail(self):
        if self.tail.prev == self.head:
            raise ValueError("List is empty")
        if self.tail.prev:
            value = self.tail.prev.self_pop()
        return value

    def insert_i(self, i, value, start="head"):
        """
        Insert the value at the i-th position(0-base) from the head or tail.
        """
        if start == "head":
            cursor: DLListNode = self.head.next if self.head.next else self.head
            for _ in range(i):
                if cursor == self.tail:
                    break
                cursor = cursor.next if cursor.next else cursor
            cursor.insert_prev_to(value)
        elif start == "tail":
            cursor = self.tail.prev if self.tail.prev else self.tail
            for _ in range(i):
                if cursor == self.head:
                    break
                cursor = cursor.prev if cursor.prev else cursor
            cursor.insert_next_to(value)
        else:
            raise NotImplementedError("start should be head or tail")

    def select_i(self, i, start="head"):
        if start == "head":
            cursor: DLListNode = self.head.next if self.head.next else self.head
            for _ in range(i):
                if cursor.next == self.tail:
                    break
                cursor = cursor.next if cursor.next else cursor
            return cursor
        elif start == "tail":
            cursor = self.tail.prev if self.tail.prev else self.tail
            for _ in range(i):
                if cursor.next == self.head:
                    break
                cursor = cursor.prev if cursor.prev else cursor
            return cursor
        else:
            raise NotImplementedError("start should be head or tail")

    def __getitem__(self, i):
        return self.select_i(i, start="head")

    def __str__(self):
        cursor: DLListNode = self.head
        res = ""
        while cursor.next is not None:
            res += f"{cursor.value if not isinstance(cursor, DLListDummyNode) else 'HEAD'} <-> "
            cursor = cursor.next
        res += "TAIL"
        return res

    def __len__(self):
        return self.length


def _print_dll(dll: DLList):
    cursor: DLListNode = dll.head
    while cursor.next is not None:
        print(
            f"{cursor.value if not isinstance(cursor, DLListDummyNode) else 'HEAD'} <-> ",
            end="",
        )
        cursor = cursor.next
    print("TAIL")


def _print_dll_reverse(dll: DLList):
    cursor: DLListNode = dll.tail
    while cursor.prev is not None:
        print(
            f"{cursor.value if not isinstance(cursor, DLListDummyNode) else 'TAIL'} <-> ",
            end="",
        )
        cursor = cursor.prev
    print("HEAD")


if __name__ == "__main__":
    d = DLList()
    d.append_head(1)
    d.append_head(2)
    d.append_tail(3)
    d.append_tail(4)
    _print_dll(d)
    d.insert_i(2, 5, start="head")
    _print_dll(d)

    print(f"__len__ method test")
    print(f"length: {len(d)}")

    print(f"__getitem__ method test")
    for i in range(5):
        print(d[i].value)
    print(f"string of dll test")
    print(d)

    d.pop_head()
    d.pop_tail()
    print(d)
    print(len(d))

    d[1].self_pop()
    print(d)
    print(len(d))
    # _print_dll_reverse(d)
