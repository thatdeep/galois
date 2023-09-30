import numpy as np


class PrimeFieldElement:
    def __init__(self, value, p):
        if isinstance(value, PrimeFieldElement):
            self.value = value.value % p
        else:
            self.value = value % p
        self.p = p

    def __add__(self, other):
        if self.p != other.p:
            raise ValueError("Modulus p must be the same for both operands.")
        return PrimeFieldElement((self.value + other.value) % self.p, self.p)

    def __sub__(self, other):
        if self.p != other.p:
            raise ValueError("Modulus p must be the same for both operands.")
        return PrimeFieldElement((self.value - other.value) % self.p, self.p)

    def __mul__(self, other):
        if self.p != other.p:
            raise ValueError("Modulus p must be the same for both operands.")
        return PrimeFieldElement((self.value * other.value) % self.p, self.p)
    
    def reciprocal(self):
        # Calculate the multiplicative inverse using the extended Euclidean algorithm
        a, b = self.value, self.p
        x, y, u, v = 0, 1, 1, 0
        while a != 0:
            q, r = b // a, b % a
            m, n = x - u * q, y - v * q
            b, a, x, y, u, v = a, r, u, v, m, n
        if b == 1:
            # The multiplicative inverse exists
            return PrimeFieldElement(x % self.p, self.p)
        else:
            raise ValueError(f"{self.value} has no multiplicative inverse modulo {self.p}")

    def __pow__(self, exponent):
        if not isinstance(exponent, int):
            return ValueError('exponent should be int')
        if exponent < 0:
            multinv = self.reciprocal()
            return multinv ** (-exponent)
        return PrimeFieldElement(pow(self.value, exponent, self.p), self.p)

    def __eq__(self, other):
        if self.p != other.p:
            raise ValueError("Modulus p must be the same for both operands.")
        return self.value == other.value
    
    def __lt__(self, other):
        if self.p != other.p:
            raise ValueError("Modulus p must be the same for both operands.")
        return self.value < other.value

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)


class PrimeField:
    def __init__(self, p, n=1):
        if n != 1:
            return NotImplementedError(f'n != 1 is not supported yet')
        from utils import is_prime
        if not is_prime(p):
            return ValueError('p must be prime')
        self.p = p
        self.n = n
        self.elements = None
        
        if self.n == 1:
            elements = []
            for i in range(0, p):
                elements.append(PrimeFieldElement(i, p))
            self.elements = np.array(elements, dtype=object)
    
    def apply(self, func, x=None, multiplicative=False, unique=False):
        if x is None:
            if multiplicative:
                elements = self.multiplicative()
            else:
                elements = self.elements.copy()
        else:
            elements = np.array([PrimeFieldElement(el, self.p, sym=self.sym) for el in x], dtype=object)
            print(elements)
        images = np.array([func(el) for el in elements], dtype=object)
        if unique:
            images = np.unique(images)
        return images
    
    def multiplicative(self):
        return self.elements[1:].copy()
    
    def squares(self):
        squares = self.multiplicative() ** 2
        squares = np.unique(squares)
        return squares
    
    def __getitem__(self, n):
        if isinstance(n, int):
            # If a single integer is provided, return the corresponding element
            return self.elements[n % self.p]
        elif isinstance(n, (list, tuple, np.ndarray)):
            # If a list, tuple, or NumPy array of integers is provided, return a new CustomArrayWrapper
            # with the selected elements
            if isinstance(n, (list, tuple)):
                selected_elements = type(n)(self.elements[[i % self.p for i in n]].copy())
            else:
                selected_elements = self.elements[[i % self.p for i in n].copy()]
            return selected_elements
        else:
            raise TypeError("Unsupported index type. Use int or iterable of ints.")
