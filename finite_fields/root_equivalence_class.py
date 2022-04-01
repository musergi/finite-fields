from finite_fields.galois_field import GaloisField

class RootEquivalenceClass:
    def __init__(self, class_repr: int, field: 'GaloisField') -> None:
        self._class_repr: int = class_repr
        self._field: 'GaloisField' = field

    def __contains__(self, element) -> bool:
        return element % self._field.characteristic == self._class_repr

    def __add__(self, other: 'RootEquivalenceClass') -> 'RootEquivalenceClass':
        return self._field.add(self, other)

    def __sub__(self, other: 'RootEquivalenceClass'):
        return self._field.substract(self, other)

    def __mul__(self, other: 'RootEquivalenceClass'):
        return self._field.multiply(self, other)

    def __floordiv__(self, other: 'RootEquivalenceClass'):
        return self._field.divide(self, other)

    def __truediv__(self, other: 'RootEquivalenceClass'):
        return self._field.divide(self, other)

    def __invert__(self):
        return self._field.inverse(self)

    def __eq__(self, other):
        return self._class_repr == other._class_repr and \
               self._field == other._field

    def __repr__(self):
        return f'{self._class_repr} in GF({self._field.cardinality})'
