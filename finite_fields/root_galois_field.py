from finite_fields.galois_field import GaloisField, EquivalenceClass
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
