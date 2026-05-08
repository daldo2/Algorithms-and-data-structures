class Stack:
    def __init__(self):
        self.max_size = 20
        self.stack = [None] * self.max_size
        self.top_index = -1

    def push(self, add):
        if self.top_index + 1 >= self.max_size:
            return 1
        self.top_index += 1
        self.stack[self.top_index] = add
        return 0

    def pop(self):
        if self.is_empty():
            return 1
        pop = self.stack[self.top_index]
        self.stack[self.top_index] = None
        self.top_index -= 1
        return pop

    def is_empty(self):
        return self.top_index == -1

    def top(self):
        if self.is_empty():
            return None
        return self.stack[self.top_index]

class Node:
    def __init__(self, data):
        self.data = data
        self.descendant = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self,data):
        new_node = Node(data)
        new_node.descendant = self.head
        self.head = new_node

def add_to_stack(stack, my_list):
    current_node = my_list.head
    while current_node is not None:
        stack.push(current_node.data)
        current_node = current_node.descendant


def is_palindrome(stack,my_list):
    current_node = my_list.head
    while current_node is not None:
        if stack.pop() != current_node.data:
            return False
        current_node = current_node.descendant
    return True


def main():
    my_list = LinkedList()
    stack = Stack()
    string = "12203022"
    print(string)


    for element in string:
        my_list.add_node(element)

    add_to_stack(stack, my_list)

    if is_palindrome(stack, my_list):
        print("It is indeed palindrome")
    else:
        print("It is not palindrome")


if __name__ == "__main__":
    main()