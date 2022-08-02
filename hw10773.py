import sys
input = sys.stdin.readline
n = int(input())
class Stack():
    def __init__(self):
        self.top = []
    def __repr__(self):
        return f'{sum(self.top)}'

    def push(self, item):
        self.top.append(item)
    
    def pop(self):
        self.top.pop()

result = Stack()
for i in range(n):
    i = int(input())
    result.push(i) if i else result.pop()

print(result)
    




