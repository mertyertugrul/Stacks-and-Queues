class StackArray(object):
    def __init__(self, value):
        self.array = [value]


    def push(self, value):
        self.array.append(value)
        return self

    def peek(self):
        return self.array[len(self.array)-1]

    def pop(self):
        self.array.pop()
        return self

    def __str__(self):
        return str(self.array)