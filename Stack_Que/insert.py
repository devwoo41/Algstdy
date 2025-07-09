s=set()
s.add(5)
s.add(3)
s.add(5)
s.add(2)
print(s)

s1 = set()
s2 = set()
for i in [1, 2, 3]:
    s1.add(i)
for i in [3, 2, 1]:
    s2.add(i)
print(s1 == s2)

a=set()
b=set()
for i in [1,2,3]:
    a.add(i)
for i in [4,5,6]:
    b.add(i)

c=a.union(b)
print(c)







