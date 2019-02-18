from collections import deque

class kqueue():
    def __init__(self):
        self.list=list()

    def push(self,x):
        print('kqueue push')
        self.list.append(x)
        self.list = deque(self.list)
        print('queue 現在是',self.list)

    def pop(self):
        print('kqueue pop')
        return self.list.popleft()
        print('queue 現在是:',self.list)

    def size(self):
        return len(self.list)

    def front(self):
        return self.list[0]

    def back(self):
        return self.list[-1]