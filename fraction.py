def pgcd(a,b):
    while b:
        a,b = b,a%b
    return a

class Fraction:
    def __init__(self, n, d):
        self.n = n
        self.d = d
        if d == 0:
            raise ValueException("denominateur égale à 0")
    
    def __repr__(self):
        return f"{self.n}/{self.d}"

    def simp(self):
        """Permet de simplifier et normaliser une Fraction.
        >>> str(Fraction(12,-15).simp()) == str(Fraction(-4,5))
        True
        """
        pgcdLocal = pgcd(self.n,self.d)
        self.n = int(self.n/pgcdLocal)
        self.d = int(self.d/pgcdLocal)
        return Fraction(self.n,self.d)
    def __add__(self,other):
        """Permet d'additionner deux objects de types Fraction ensemble.
        >>> Fraction(2,3) + Fraction(4,6) == Fraction(4,3)
        True
        """
        self.n = self.n*other.d + other.n * self.d
        self.d = self.d * other.d
        return self.simp()
    
    def __sub__(self,other):
        """Permet de soustraire deux objects de types Fraction.
        >>> Fraction(2,3) - Fraction(2,6) == Fraction(1,3)
        True
        """
        self.n = self.n*other.d - other.n * self.d
        self.d = self.d * other.d
        return self.simp()
    
    def __mul__(self,other):
        """Permet de multiplier deux objects de types Fraction.
        >>> Fraction(2,3) * Fraction(2,6) == Fraction(2,9) 
        True
        """
        self.n = self.n*other.n
        self.d = self.d*other.d
        return self.simp()
    
    def __truediv__(self,other):
        """Permet de diviser deux objects de types Fraction.
        >>> Fraction(2,3) / Fraction(2,6) == Fraction(2,1) 
        True
        """
        self.n = self.n*other.d
        self.d = self.d*other.n
        return self.simp()

    def __eq__(self,other):
        """Permet de savoir si deux fractions sont egales.
        >>> Fraction(4,8) == Fraction(1,2) 
        True
        """
        selff = Fraction(self.n*other.d, self.d * other.d).simp()
        otherr = Fraction(other.n*self.d, other.d * self.d).simp()
        if selff.n == otherr.n :
            return True
        else:
            return False

    def __ge__(self, other):
        """Permet de savoir si une fraction est superieure ou egale a une autre.
        >>> Fraction(7,8) >= Fraction(1,2) 
        True
        >>> Fraction(1,2) >= Fraction(88,9)
        False
        """
        selff = Fraction(self.n*other.d, self.d * other.d).simp()
        otherr = Fraction(other.n*self.d, other.d * self.d).simp()
        if selff.n >= otherr.n:
            return True
        else:
            return False
            

    def __neg__(self):
        """Retourne l'oppose d'une fraction
        >>> -Fraction(4,5)
        -4/5
        """
        return Fraction(-self.n, self.d)

    def inv(self):
        """Retourne l'inverse d'une fraction
        >>> Fraction(1,2).inv()
        2/1"""
        return Fraction(self.d,self.n)

    def puissance(self, n):
        """Calcule la puissance d'une fraction
        >>> Fraction(4,5).puissance(2)
        16/25"""
        return Fraction(self.n**n,self.d**n).simp()

import doctest
doctest.testmod(verbose=True)
