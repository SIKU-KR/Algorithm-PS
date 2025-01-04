class Node:
    def __init__(self, value=None):
        self.value = value
        self.prev = None
        self.next = None


class Editor:
    def __init__(self, initval):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cursor = self.tail

        for c in initval:
            self.insert(c)
    

    def insert(self, value):
        new = Node(value)
        prev_node = self.cursor.prev
        self.cursor.prev = new
        prev_node.next = new
        new.prev = prev_node
        new.next = self.cursor


    def delete(self):
        if self.cursor.prev == self.head:
            return
        
        target = self.cursor.prev
        prev = target.prev
        prev.next = self.cursor
        self.cursor.prev = prev


    def move_left(self):
        if self.cursor.prev != self.head:
            self.cursor = self.cursor.prev

    def move_right(self):
        if self.cursor != self.tail:
            self.cursor = self.cursor.next

    def print(self):
        self.cursor = self.head.next
        while self.cursor.value != None:
            print(self.cursor.value, end='')
            self.move_right()

str = input()
a = Editor(str)
n = int(input())

for i in range(n):
    inp = input()
    if inp[0] == 'L':
        a.move_left()
    elif inp[0] == 'D':
        a.move_right()
    elif inp[0] == 'B':
        a.delete()
    elif inp[0] == 'P':
        a.insert(inp[2])

a.print()
