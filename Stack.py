"""
In stack data structure the items are placed in top of one another.
PUSH - insert into the top of the stack
POP - remove from the top of the stack
PEEK - return the top element of the stack

"""


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        if item not in self.items:
            self.items.append(item)

    def pop(self):
        if len(self.items) <= 0:
            return "No element in the stack"
        else:
            return self.items.pop()

    def is_empty(self):
        return self.items == []

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def get_stack(self):
        return self.items


s = Stack()
s.push("A")
s.push("B")
print(s.get_stack())
s.push("c")
print(s.get_stack())
s.pop()
print(s.get_stack())
print(s.peek())
print(s.is_empty())

