class Matrix2: 
    """Une implémentation, 
        sommaire, 
        de matrice carrée 2x2
    """
    def __init__(self, a11, a12, a21, a22):
         "construit une matrice à partir des 4 coefficients" 
         # on décide d'utiliser un tuple plutôt que de ranger 
         # les coefficients individuellement 
         self.a = (a11, a12, a21, a22)
    def determinant(self):
        "le déterminant de la matrice"
        return self.a[0] * self.a[3] - self.a[1] * self.a[2]
    def __repr__(self):
        "comment présenter une matrice dans un print()"
        return f"<<mat-2x2 {self.a}>>"

matrice = Matrix2(1, 2, 2, 1)
print(f"Determinant de {matrice} = {matrice.determinant()}")