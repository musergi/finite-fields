from finite_fields.galois_field import GaloisField
from finite_fields.root_equivalence_class import RootEquivalenceClass


class RootGaloisField(GaloisField):
    def __init__(self, root: int) -> None:
        super().__init__()
        if not RootGaloisField._is_prime(root):
            raise ValueError("Root must be prime")
        self._equivalence_classes = [RootEquivalenceClass(n, self) for n in range(0, root)]

    @property
    def characteristic(self) -> int:
        return self.cardinality

    @property
    def dimension(self) -> int:
        return 1

    def add(self, op1: RootEquivalenceClass, op2: RootEquivalenceClass):
        res_repr = (op1.representative + op2.representative) % self.characteristic
        return RootEquivalenceClass(res_repr, self)

    def substract(self, op1: RootEquivalenceClass, op2: RootEquivalenceClass):
        res_repr = (op1.representative - op2.representative) % self.characteristic
        return RootEquivalenceClass(res_repr, self)

    def multiply(self, op1: RootEquivalenceClass, op2: RootEquivalenceClass):
        res_repr = (op1.representative * op2.representative) % self.characteristic
        return RootEquivalenceClass(res_repr, self)

    def divide(self, op1: RootEquivalenceClass, op2: RootEquivalenceClass):
        return self.multiply(op1, self.inverse(op2))

    def inverse(self, op: RootEquivalenceClass, _p: int = None, _y1: int = 1, _y2: int = 0):
        if _p is None:
            _p = self.characteristic
        a = op.representative
        if a == 1:
            return RootEquivalenceClass(_y1 % self.characteristic, self)
        q = _p // a
        return self.inverse(
            op=RootEquivalenceClass(_p - q * a, self),
            _p=a,
            _y1=_y2 - q * _y1,
            _y2=_y1)

    def __eq__(self, other):
        return self.characteristic == other.characteristic

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