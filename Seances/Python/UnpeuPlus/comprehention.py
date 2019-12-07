[(x,x**2) for x in range(10+1)]

[x for x in range(10+1) if x%2 == 0]

[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]


[num for elem in [[1,2,3], [4,5,6], [7,8,9]] for num in elem]

[num for elem in [[1,2,3], 4, [5,6,7]] if isinstance(elem,list) for num in elem ]

((x,x**3) for x in range(10+1))

(x for x in range(10+1) if x%2 == 1)

{x for x in 'abracadabra' if x not in 'abc'}

{x:'paire' for x in range(10+1) if x%2 == 0}