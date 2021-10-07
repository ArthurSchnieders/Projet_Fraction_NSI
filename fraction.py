def pgcd(a,b):
    while b:
        a,b = b,a%b
    return a

class Fraction:
    def __init__(self, n, d):
        self.n = n
        self.d = d
        if d == 0:
            raise ValueException("denominateur egal a 0")



    def simp(self):
        pgcdLocal = pgcd(self.n,self.d)
        self.n = self.n/pgcdLocal
        self.d = self.d/pgcdLocal

    def __add__(self,other):
        self.n = self.n*other.d + other.n * self.d
        self.d = self.d * other.d
        self.simp()

    def __sub__(self,other):
        self.n = self.n*other.d - other.n * self.d
        self.d = self.d * other.d
        self.simp()

    def __mul__(self,other):
        self.n = self.n*other.n
        self.d = self.d*other.d
        self.simp()

    def __div__(self,other):
        self.n = self.n*other.d
        self.d = self.d*other.n
        self.simp()


    def __eq__(self,other):
        1 = simp(Fraction(self.n*other.d, self.d * other.d))
        2 = simp(Fractions(other.n*self.d, other.d * self.d))
        if 1.n == 2.n :
            return True
        else:
            return False

    def __ge__(self, other):
        1 = simp(Fraction(self.n*other.d, self.d * other.d))
        2 = simp(Fractions(other.n*self.d, other.d * self.d))
        if 1.n >= 2.n:
            return self
        elif 2.n >= 1.n:
            return other
        else:
            return


    def __neg__(self):
        return Fraction(-self.n, self.d)

    def inv(self):
        return Fraction(self.d,self.n)

    def puissance(self, n):
        return Fraction(self.)
