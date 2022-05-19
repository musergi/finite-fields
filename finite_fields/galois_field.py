from abc import abstractmethod, abstractproperty
from collections.abc import Collection

from .equivalence_class import EquivalenceClass


class GaloisField(Collection):
    """Abstract class for all galois fields.

    This class provides the general interface all Galois Fields should present.
    It is used as a base class for all the specific Galois Field
    implementations. It also presents a series of properties that the
    subclasses should implement. It provides a default implementation for some
    methods.
    """

    @abstractmethod
    def random(self) -> EquivalenceClass: ...

    @abstractproperty
    def characteristic(self) -> int: ...

    @abstractproperty
    def dimension(self) -> int: ...

    @property
    def cardinality(self) -> int:
        return self.characteristic ** self.dimension

    @abstractproperty
    def zero(self) -> EquivalenceClass: ...

    @abstractproperty
    def one(self) -> EquivalenceClass: ...

    @abstractmethod
    def __getitem__(self, member: int) -> EquivalenceClass: ...

    def __len__(self) -> int:
        return self.cardinality

    def __repr__(self) -> str:
        return f'GF({self.cardinality})'
