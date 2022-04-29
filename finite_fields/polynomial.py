from itertools import zip_longest
from typing import Callable, Tuple

class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = coefficients
        while len(self.coefficients) >=  1 and self.coefficients[-1].is_zero:
            self.coefficients.pop()

    @staticmethod
    def fromMonomial(coefficient, degree):
        zero_pad = [coefficient.zero] * degree
        return Polynomial(zero_pad + [coefficient])

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

    def _divide(self, other: 'Polynomial') -> Tuple['Polynomial', 'Polynomial']:
        result = []
        divided = self
        zero = self.coefficients[0].zero
        while divided.degree >= other.degree:
            coefficient = divided.coefficients[-1] / other.coefficients[-1]
            degree = divided.degree - other.degree
            quotient =  Polynomial.fromMonomial(coefficient, degree)
            divided = divided - other * quotient
            result.insert(0, coefficient)
        return Polynomial(result), divided

    def __truediv__(self, other: 'Polynomial') -> 'Polynomial':
        result, _ = self._divide(other)
        return result

    def __mod__(self, other: 'Polynomial') -> 'Polynomial':
        _, result = self._divide(other)
        return result
    
    def __eq__(self, other: 'Polynomial') -> bool:
        if len(self) != len(other):
            return False
        for c1, c2 in zip(self.coefficients, other.coefficients):
            if c1 != c2:
                return False
        return True

    def __repr__(self) -> str:
        monomes = [f'({coef}){_get_x_repr(index)}' for index, coef in enumerate(self.coefficients)]
        return " + ".join(monomes)

def _get_x_repr(degree):
    if degree == 0:
        return ''
    if degree == 1:
        return 'x'
    return f'x^{degree}'