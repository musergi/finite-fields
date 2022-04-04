from finite_fields.galois_field import GaloisField

class RootEquivalenceClass:
    def __init__(self, class_repr: int, field: 'GaloisField') -> None:
        if field.characteristic != 0:
            self._class_repr: int = class_repr % field.characteristic
        else:
            self._class_repr: int = class_repr
        self._field: 'GaloisField' = field

    def __contains__(self, element: int) -> bool:
        return element % self._field.characteristic == self._class_repr

    def __add__(self, other: 'EquivalenceClass') -> 'EquivalenceClass':
        return RootEquivalenceClass(self._class_repr + other._class_repr, self._field)

    def __sub__(self, other: 'EquivalenceClass') -> 'EquivalenceClass':
        return RootEquivalenceClass(self._class_repr - other._class_repr, self._field)

    def __mul__(self, other: 'EquivalenceClass') -> 'EquivalenceClass':
        return RootEquivalenceClass(self._class_repr * other._class_repr, self._field)

    def __floordiv__(self, other: 'EquivalenceClass') -> 'EquivalenceClass':
        return self * ~other

    def __truediv__(self, other: 'EquivalenceClass') -> 'EquivalenceClass':
        return self * ~other

    def __invert__(self) -> 'EquivalenceClass':
        class_repr = self._extended_euclid(self._class_repr, self._field.characteristic)
        return RootEquivalenceClass(class_repr, self._field)

    def _extended_euclid(self, a: int, p: int, y1: int=1, y2: int=0) -> int:
        if a == 1:
            return y1
        q = p // a
        return self._extended_euclid(p - q * a, a, y2 - q * y1, y1)

    def __eq__(self, other):
        return self._class_repr == other._class_repr and \
               self._field == other._field

    def __repr__(self):
        return f'{self._class_repr} in GF({self._field.cardinality})'
