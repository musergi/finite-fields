import random
from typing import List


class EquivalenceClass:
    def __init__(self, class_repr: int, field: 'GaloisField') -> None:
        self._class_repr: int = class_repr
        self._field: 'GaloisField' = field

    def __contains__(self, element):
        return element % self._field.cardinality == self._class_repr

    def get_repr(self):
        return self._class_repr

    representative = property(fget=get_repr)

    def __add__(self, other: 'EquivalenceClass'):
        return self._field.add(self, other)

    def __sub__(self, other: 'EquivalenceClass'):
        return self._field.substract(self, other)

    def __eq__(self, other):
        return self._class_repr == other._class_repr and \
            self._field == other._field
    
    def __repr__(self):
        return str(self._class_repr)


class GaloisField:
    def __init__(self) -> None:
        self._equivalence_classes: List[EquivalenceClass] = None

    def random(self) -> EquivalenceClass:
        return random.choice(self._equivalence_classes)

    def get_cardinality(self) -> int:
        return len(self._equivalence_classes)

    cardinality = property(fget=get_cardinality)

    def get_p(self) -> int:
        raise NotImplementedError()

    p = property(fget=lambda self: self.get_p())

    def get_m(self) -> int:
        raise NotImplementedError()

    m = property(fget=lambda self: self.get_m())

    @property
    def zero(self):
        return self._equivalence_classes[0]

    @property
    def one(self):
        return self._equivalence_classes[1]

    def __contains__(self, equivalence_class):
        return equivalence_class in self._equivalence_classes

    def __getitem__(self, index):
        return self._equivalence_classes[index]

    def __repr__(self) -> str:
        return f'GF({self.cardinality})'

class RootGaloisField(GaloisField):
    def __init__(self, root: int) -> None:
        super().__init__()
        if not RootGaloisField._is_prime(root):
            raise ValueError("Root must be prime")
        self._equivalence_classes = [EquivalenceClass(n, self) for n in range(0, root)]

    def get_p(self) -> int:
        return self.cardinality

    def get_m(self) -> int:
        return 1

    def add(self, op1: EquivalenceClass, op2: EquivalenceClass):
        res_repr = (op1.representative + op2.representative) % self.cardinality
        return EquivalenceClass(res_repr, self)

    def substract(self, op1: EquivalenceClass, op2: EquivalenceClass):
        res_repr = (op1.representative - op2.representative) % self.cardinality
        return EquivalenceClass(res_repr, self)

    def __eq__(self, other):
        return self.cardinality == other.cardinality

    def __repr__(self) -> str:
        return f'GF({self.cardinality})'

    @staticmethod
    def _is_prime(n):
        if n == 1:
            return False
        i = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += 1
        return True
