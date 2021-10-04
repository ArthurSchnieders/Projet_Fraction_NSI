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
        pass
    
    def __ge__(self, other):
        pass
    
    def __neg__(self, other):
        pass
    
    def inv(self, others):
        pass
    
    def puissance(self, others):
        pass
