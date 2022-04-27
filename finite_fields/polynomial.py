from itertools import zip_longest
from typing import Callable

class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = coefficients
        if len(self.coefficients) > 1:
            while self.coefficients[-1].is_zero:
                self.coefficients.pop()

    @property
    def degree(self) -> int:
        return len(self) - 1

    def __len__(self) -> int:
        return len(self.coefficients)

    def _elementwise(self, other: 'Polynomial', func: Callable):
        coefficients = []
        for c1, c2 in zip_longest(self.coefficients, other.coefficients):
            if c1 is None:
                coefficients.append(c2)
            elif c2 is None:
                coefficients.append(c1)
            else:
                coefficients.append(func(c1, c2))
        return Polynomial(coefficients)

    def __add__(self, other: 'Polynomial') -> 'Polynomial':
        return self._elementwise(other, lambda x, y: x + y)
    
    def __sub__(self, other: 'Polynomial') -> 'Polynomial':
        return self._elementwise(other, lambda x, y: x - y)

    def __mul__(self, other: 'Polynomial') -> 'Polynomial':
        result = [self.coefficients[0].zero] * (self.degree + other.degree + 1)
        for deg1, c1 in enumerate(self.coefficients):
            for deg2, c2 in enumerate(other.coefficients):
                result[deg1 + deg2] += c1 * c2
        return Polynomial(result)
    
    def __eq__(self, other: 'Polynomial') -> bool:
        if len(self) != len(other):
            return False
        for c1, c2 in zip(self.coefficients, other.coefficients):
            if c1 != c2:
                return False
        return True

    def __repr__(self) -> str:
        monomes = [f'({coef})x^{index}' for index, coef in enumerate(self.coefficients)]
        return " + ".join(monomes)
