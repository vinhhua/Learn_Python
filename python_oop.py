class Stack(object):
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self) -> object:
        return self.items.pop()

    def peek(self) -> object:
        return self.items[len(self.items) - 1]

    def size(self) -> int:
        return len(self.items)

    def print_stack(self):
        for i in self.items:
            print(i)

    @property
    def is_empty(self) -> bool:
        return len(self.items) == 0


class Employee(object):
    def __init__(self, name="Unknown", id="Unknown"):
        self.name = name
        self.id = id

    @property
    def get_name(self):
        return self.__name

    @property
    def get_id(self):
        return self.id


def main():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.print_stack()
    print(stack.peek())


if __name__ == '__main__':
    main()




