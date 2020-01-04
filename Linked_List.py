# Class Node contains its own value and it's reference to the next node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList(object):
    def __init__(self, data=None, next_node=None):
        self.next_node = next_node
        self.head = None
        self.data = data
        self.size = 0

    # Add new node to the beginning of the linked list
    def prepend(self, data):
        if self.__is_empty():
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
        self.size += 1

    # Add the new node to the end of the linked list
    def append(self, data):
        new_node = Node(data)
        if self.__is_empty():
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

        self.size += 1

    # delete the element at the end of the linked list
    def pop(self):
        if self.__is_empty():
            return
        else:
            temp = self.head.data
            self.head = self.head.next
            self.size -= 1
            return temp

    # Print the linked list
    def print_list(self):
        if self.__is_empty():
            print("The list is empty")
            return
        else:
            current = self.head
            # Keeps on traversing until current(or head) is null which is at the end of the list
            while current is not None:
                print(current.data, " -> ", end="")
                current = current.next
            print("Null")

    # TO-DO
    def delete(self, value):
        if self.__is_empty():
            print("The list is emtpy")
            return
        current = self.head
        while current.next is not None:
            if current.data == value:
                break
            current = current.next

        if current.next is None:
            print("Item not found in the list")
        else:
            current.next = current.next.next

    # Return the size of the linked list
    @property
    def get_size(self):
        return self.size

    # Return true is ll is empty, true if otherwise
    def __is_empty(self) -> bool:
        return self.head is None


def main():
    singly_linked_list = SinglyLinkedList()
    singly_linked_list.prepend(1)
    singly_linked_list.prepend(2)
    singly_linked_list.prepend(3)
    singly_linked_list.append(4)
    singly_linked_list.prepend(5)
    print(singly_linked_list.pop())
    singly_linked_list.delete(2)

    print(singly_linked_list.get_size)
    singly_linked_list.print_list()


if __name__ == '__main__':
    main()
