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
        selff = simp(Fraction(self.n*other.d, self.d * other.d))
        otherr = simp(Fractions(other.n*self.d, other.d * self.d))
        if selff.n == otherr.n :
            return True
        else:
            return False

    def __ge__(self, other):
        selff = simp(Fraction(self.n*other.d, self.d * other.d))
        otherr = simp(Fractions(other.n*self.d, other.d * self.d))
        if selff.n >= otherr.n:
            return self
        elif otherr.n >= selff.n:
            return other
        else:
            return


    def __neg__(self):
        return Fraction(-self.n, self.d)

    def inv(self):
        return Fraction(self.d,self.n)

    def puissance(self, n):
        return simp(Fraction(self.n**n,self.d**n))
