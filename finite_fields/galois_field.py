import random
from typing import List

from .equivalence_class import EquivalenceClass


class GaloisField:
    """Abstract class for all galois fields.

    This class provides the general interface all Galois Fields should present.
    It is used as a base class for all the specific Galois Field
    implementations. It also presents a series of properties that the
    subclasses should implement. It provides a default implementation for some
    methods.
    """

    def __init__(self) -> None:
        """The __init__ should never be directly called.

        For implementors, this constructor constructs and the
        _equivalence_classes attribute that should be overwritten in children
        classes in order to get access to the default implemented functions.

        Attributes
        ----------
        _equivalence_classes : List[EquivalenceClass]
            Set of equivalence classes in the field. It is always an empty list
            for this class as it is an abstract class.
        """
        self._equivalence_classes: List[EquivalenceClass] = []

    def random(self) -> EquivalenceClass:
        """Chooses a random element of field.

        This method can be used for fetching a random element of the field.
        This function will return a random element each time called.

        Returns
        -------
        EquivalenceClass
            Random element from the set of equivalence classes in the field.
        """
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
