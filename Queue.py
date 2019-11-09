class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue(object):
    def __init__(self, value):
        self.first = Node(value)
        self.last = self.first
        self.length = 1

    def enqueue(self, value):
        self.last.next = Node(value)
        self.last = self.last.next
        self.length += 1

    def peek(self):
        return self.first.value

    def dequeue(self):
        self.first = self.first.next
        self.length -= 1

    def __str__(self):
        out = ''
        if self.length < 1:
            out = 'This list has no values.'
        else:
            i = 0
            first_copy = self.first
            while first_copy is not None:
                if i == 0:
                    out = 'first: ' + str(first_copy.value)
                elif i == self.length - 1:
                    out += '=> last: ' + str(first_copy.value)
                else:
                    out += '=> ' + str(first_copy.value)
                first_copy = first_copy.next
                i += 1
        return out
