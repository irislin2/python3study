from collections import deque

class kstack():
    def __init__(self):
        self.list=list()

    def push(self,x):
        print('kstack push')
        self.list.append(x)
        self.list = deque(self.list)
        print('stack 現在是',self.list)

    def pop(self):
        print('kstack pop')
        return self.list.pop()
        print('stack 現在是:',self.list)

    def size(self):
        return len(self.list)

    def top(self):
        return self.list[-1]