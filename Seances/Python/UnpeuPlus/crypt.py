def decale(n):
    def _decale(c):
        return chr(ord(c)+n)
    return _decale

decale(1)('A')
decale(2)('A')
decale(26)('A')
''.join(map(decale(1), 'ABCD'))
''.join(map(decale(26), 'Bonjour'))

def 