import random
from typing import List

from .equivalence_class import EquivalenceClass


class GaloisField:
    def __init__(self) -> None:
        self._equivalence_classes: List[EquivalenceClass] = []

    def random(self) -> EquivalenceClass:
        return random.choice(self._equivalence_classes)

    @property
    def p(self) -> int:
        raise NotImplementedError()

    @property
    def m(self) -> int:
        raise NotImplementedError()

    @property
    def q(self) -> int:
        return len(self._equivalence_classes)

    @property
    def cardinality(self) -> int:
        return self.q

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
        return f'GF({self.q})'
