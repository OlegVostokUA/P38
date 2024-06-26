# class Stack:
#     def __init__(self):
#         self.our_stack = []
#
#     def push(self, x):
#         self.our_stack.append(x)
#
#     def pop(self):
#         x = self.our_stack.pop()
#         return x
#
#     def clear(self):
#         self.our_stack.clear()
#
#     def is_empty(self):
#         return len(self.our_stack) == 0
#
#     def top(self):
#         if self.is_empty():
#             raise Exception('Stack: "top" applied to empty container')
#         x = self.our_stack[-1]
#         return x
#
#     def __len__(self):
#         return len(self.our_stack)
#
#
# def brackets_checker(sb):
#     s = Stack()
#
#     for brace in sb:
#         if brace not in '()[]':
#             continue
#         if brace in '([':
#             s.push(brace)
#         else:
#             if s.is_empty():
#                 return False
#             left = s.pop()
#             if left == '(':
#                 right = ')'
#             elif left == '[':
#                 right = ']'
#             if right != brace:
#                 return False
#
#     # if s.is_empty():
#     #     return True
#     # else:
#     #     return False
#
#     return s.is_empty()
#
# print(brackets_checker('()((([])))[][[]]()[()]'))
# print(brackets_checker('(15+5)/[(57676+90]'))
# print(brackets_checker('[(])'))

# class Queue:
#     def __init__(self):
#         self.items = []
#
#     def empty(self):
#         return len(self.items) == 0
#
#     def enqueue(self, item):
#         self.items.append(item)
#
#     def dequeue(self):
#         if self.empty():
#             raise Exception('Queue is empty')
#         return self.items.pop(0)
#
#     def __len__(self):
#         return len(self.items)

# from collections import deque
#
# q = deque()
#
# # print(help(q))
#
# q.append('eat')
# q.append(25322)
# q.append(25.8)
#
# print(q.pop())
# print(q.pop())
# print(q.pop())

# from queue import Queue
#
# q = Queue()
#
# # print(q.qsize())
#
# q.put(12)
# q.put(22)
# q.put(32)
# # print(q.qsize())
# print(q.get())
# print(q.get())
# print(q.get())
# print(q.qsize())

# from multiprocessing import Queue
#
# q = Queue()
#
# # print(q.qsize())
#
# q.put(12)
# q.put(22)
# q.put(32)
# # print(q.qsize())
# print(q.get())
# print(q.get())
# print(q.get())
# print(q.qsize())
# print(help(q))

class PriorityQueue:
    def __init__(self):
        self.m_items = []

    def empty(self):
        return len(self.m_items) == 0

    def insert(self, key, priority):
        self.m_items.append((key, priority))

    def extract_minimum(self):
        if self.empty():
            raise Exception('PriorityQueue is empty')

        minpos = 0

        for i in range(1, len(self.m_items)):
            if self.m_items[minpos][1] > self.m_items[i][1]:
                minpos = i

        return self.m_items.pop(minpos)[0]


pq = PriorityQueue()

print(pq.empty())
pq.insert('Rabs', 5)
pq.insert('Dems', 5)

pq.insert('Hells', 1)
pq.insert('Fax', 2)
pq.insert('Loops', 4)
print(pq.empty())
##
print(pq.extract_minimum())
print(pq.extract_minimum())
print(pq.extract_minimum())
print(pq.extract_minimum())
print(pq.extract_minimum())
print(pq.empty())

