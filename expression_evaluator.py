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

def to_postfix(infix):
    my_stack = Stack()
    postfix = []
    precedence = {"+": 2, "-": 2, "*": 1, "/": 1, "(": 0}
    infix = infix.split()
    for element in infix:
        if element.isdigit():
            postfix.append(element)
        elif element == "(":
            my_stack.push(element)
        elif element == ")":
            while not my_stack.is_empty() and my_stack.top() != "(":
                postfix.append(my_stack.pop())
            my_stack.pop()
        elif element in precedence:
            while not my_stack.is_empty() and my_stack.top() != "(":
                if precedence[my_stack.top()] >= precedence[element]:
                    postfix.append(my_stack.pop())
                else:
                    break
            my_stack.push(element)
    while not my_stack.is_empty():
        postfix.append(my_stack.pop())

    return postfix

def evaluate(postfix):
    my_stack = Stack()

    for element in postfix:
        if element.isdigit():
            my_stack.push(int(element))
        else:
            b = my_stack.pop()
            a = my_stack.pop()
            if element == "*" :
                my_stack.push(a * b)
            if element == "/" :
                my_stack.push(a / b)
            if element == "+":
                my_stack.push(a + b)
            if element == "-":
                my_stack.push(a - b)

    return my_stack.pop()

def main():
    infix = "17 * ( 2 + 3 ) + 4 + ( 8 * 5 )"
    postfix = to_postfix(infix)
    print(postfix)
    output = evaluate(postfix)
    print(output)

if __name__ == "__main__":
    main()