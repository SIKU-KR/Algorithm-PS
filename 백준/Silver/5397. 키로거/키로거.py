class Node:
    def __init__(self, value=None):
        self.value = value
        self.prev = None
        self.next = None

class DLL:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.tail.prev = self.head
        self.head.next = self.tail
        self.cursor = self.tail

    def insert(self, value):
        new = Node(value)
        prev = self.cursor.prev
        new.prev = prev
        prev.next = new
        self.cursor.prev = new
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
        point = self.head.next
        while point != self.tail:
            print(point.value, end='')
            point = point.next
        print()

n = int(input())
for i in range(n):
    text = input()
    a = DLL()
    for char in text:
        if char == '<':
            a.move_left()
        elif char == '>':
            a.move_right()
        elif char == '-':
            a.delete()
        else:
            a.insert(char)
    a.print()