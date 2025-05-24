from Stack_stct import Stack
"""
a=Stack()
a.push('2')
print(a)
print(type(a))
print(a.pop())
a.pop()
a.push(1)
a.push(2)
a.push(3)
print(a.__len__())
"""
K=input().split()
stack_r=Stack()
stack_l=Stack()
for i in K:
    if i=='(':
        stack_l.push('(')
    elif i==')':
        stack_r.push('(')

print(stack_l.__len__())