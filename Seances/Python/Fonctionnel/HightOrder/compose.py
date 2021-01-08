def compose(*funcs):
    """Return a new function s.t.
       compose(f,g,...)(x) == f(g(...(x)))"""
    def inner(data, funcs=funcs):
        result = data
        for f in reversed(funcs):
            result = f(result)
        return result
    return inner

if __name__ == '__main__':
    times2 = lambda x: x*2
    minus3 = lambda x: x-3
    mod6 = lambda x: x%6
    # mod6(time2(minus3(x)))
    f = compose(mod6, times2, minus3)
    assert all(f(i)==((i-3)*2)%6 for i in range(1000000))
    # True