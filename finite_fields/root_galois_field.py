import random
from finite_fields.galois_field import GaloisField, EquivalenceClass
from finite_fields.root_equivalence_class import RootEquivalenceClass


class RootGaloisField(GaloisField):
    def __init__(self, root: int) -> None:
        super().__init__()
        if not RootGaloisField._is_prime(root):
            raise ValueError("Root must be prime")
        self._characterisitic = root

    @property
    def characteristic(self) -> int:
        return self._characterisitic

    @property
    def dimension(self) -> int:
        return 1

    @property
    def zero(self) -> EquivalenceClass:
        return RootEquivalenceClass(0, self)

    @property
    def one(self) -> EquivalenceClass:
        return RootEquivalenceClass(1, self)

    def random(self) -> EquivalenceClass:
        repr = random.randint(0, self._characterisitic)
        return RootEquivalenceClass(repr, self)

    def __iter__(self):
        current = self.zero
        yield current
        current += self.one
        while current != self.zero:
            yield current
            current += self.one
    
    def __contains__(self, el: EquivalenceClass) -> bool:
        return el._field == self

    def __eq__(self, other):
        return self._characterisitic == other._characterisitic

    def __repr__(self) -> str:
        return f'GF({self._characterisitic})'

    def __getitem__(self, member: int) -> EquivalenceClass:
        return RootEquivalenceClass(member, self)

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
