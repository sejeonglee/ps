from operator import gt, lt


class Heap:
    def __init__(self, type="max"):
        self.container = []
        self.n = 0
        self.operator = gt if type == "max" else lt

    def is_empty(self):
        return self.n == 0

    def pop(self):
        try:
            last_value = self.container.pop()
        except IndexError:
            return None
        self.n -= 1

        if self.n == 0:
            return last_value

        first_value = self.container[0]
        self.container[0] = last_value
        self._heapify(self.n - 1)
        return first_value

    def push(self, new_value):
        if self.n == 0:
            self.container.append(new_value)
            self.n += 1
            return
        first_value = self.container[0]
        self.container.append(first_value)
        self.n += 1
        self.container[0] = new_value
        self._heapify(self.n - 1)

    def _heapify(self, i):
        if i == 0:
            return

        parent_i = i // 2

        # if self.operator == gt
        # parent should be greater than child -> max heap
        if self.operator(self.container[i], self.container[parent_i]):
            self.container[i], self.container[parent_i] = (
                self.container[parent_i],
                self.container[i],
            )
        self._heapify(parent_i)


# Example
if __name__ == "__main__":
    input_arr = [1, 5, 7, 2, 2, 36, 7, 9, 1, 29]
    heap = Heap("max")

    for i in input_arr:
        heap.push(i)

    while not heap.is_empty():
        print(heap.pop())
