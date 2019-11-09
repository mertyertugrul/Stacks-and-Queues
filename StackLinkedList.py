class Node(object):
    def __init__(self, data=None, ):
        self.value = data
        self.next = None


class StackLinked(object):
    def __init__(self, value):
        self.top = Node(value)
        self.bottom = self.top
        self.length = 1

    def push(self, value):
        temp = self.top
        self.top = Node(value)
        self.top.next = temp
        self.length += 1
        return self

    def peek(self):
        return self.top.value

    def pop(self):
        self.top = self.top.next
        self.length -= 1
        return self

    def __str__(self):
        out = ''
        if self.length < 1:
            out = 'This list has no values.'
        else:
            i = 0
            top_copy = self.top
            while top_copy:
                if i == 0:
                    out = 'top: ' + str(top_copy.value)
                elif i == self.length - 1:
                    out += '=> bottom: ' + str(top_copy.value)
                else:
                    out += '=> ' + str(top_copy.value)
                top_copy = top_copy.next
                i += 1
        return out