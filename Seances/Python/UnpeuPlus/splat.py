x = ['A', 'B']
y = ('C', 'D')
z = [*x, *y]
print (z)
# réponse 
# ['A', 'B', 'C', 'D']

d1={0: 'A', 1: 'B', 'c': 'C', 'd': 'D'}
d2={'v1':'Data v1', 'v2':2, 1.0:'pourquoi pas'}
print(*d1)
print([*d1,*d2])
print({**d1,**d2})
'''
>>> d1={0: 'A', 1: 'B', 'c': 'C', 'd': 'D'}
>>> d2={'v1':'Data v1', 'v2':2, 1.0:'pourquoi pas'}
>>> print(*d1)
0 1 c d
>>> print([*d1,*d2])
[0, 1, 'c', 'd', 'v1', 'v2', 1.0]
>>> print({**d1,**d2})
{0: 'A', 1: 'pourquoi pas', 'c': 'C', 'd': 'D', 'v1': 'Data v1', 'v2': 2}
'''