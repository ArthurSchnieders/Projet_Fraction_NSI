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
        if n < 0 and

    def __add__(self,other):
        pass

    def __sub__(self,other):
        pass

    def __mul__(self,other):
        pass

    def __div__(self,other):
        pass

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

    def inv(self, others):
        pass

    def puissance(self, others):
        pass
