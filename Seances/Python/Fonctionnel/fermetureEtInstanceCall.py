# Objet callable (pouvant être utilisé comme fonction)
class Adder(object):
    def __init__(self, n):
        self.n = n
    #L'objet fonction appel __call__
    def __call__(self, m):
        return self.n + m

add5_i = Adder(5)
print(add5_i(10))

#Fonction avec fermeture
def make_adder(n):
    def adder(m):
        return m + n
    return adder
add5_f = make_adder(5)  
print(add5_f(10))

def make_lambda_adder(n):
    return lambda m: m + n
add5_l = make_lambda_adder(5)  
print(add5_l(10))

n=100
print(add5_f(10))
print(add5_l(10))