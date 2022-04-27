from itertools import zip_longest

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

    def __add__(self, other: 'Polynomial') -> 'Polynomial':
        coefficients = []
        for c1, c2 in zip_longest(self.coefficients, other.coefficients):
            if c1 is None:
                coefficients.append(c2)
            elif c2 is None:
                coefficients.append(c1)
            else:
                coefficients.append(c1 + c2)
        return Polynomial(coefficients)
    
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
