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
    
    def __div__(self,other):
        """Permet de diviser deux objects de types Fraction.
        >>> Fraction(2,3) / Fraction(2,6) == Fraction(2,1) 
        True
        """
        self.n = self.n*other.d
        self.d = self.d*other.n
        return self.simp()
    
    
    def __eq__(self,other):
        pass
    
    def __ge__(self, other):
        pass
    
    def __neg__(self, other):
        pass
    
    def inv(self, others):
        pass
    
    def puissance(self, others):
        pass
