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
    def characteristic(self) -> int:
        """Gets the characteristic associated with the field.

        The prime p is referred as the characteristic of the field. In the
        case of a root Galois Field the characteristic fully defines the field
        as all arithmetic is done modulo the characteristic.

        Returns
        -------
        int
            The characteristic of the field.
        """
        raise NotImplementedError()

    @property
    def dimension(self) -> int:
        """Gets the dimension of the field.

        For root Galois Field the dimension is 1. For extended Galois Field it
        can be interpreted as the degree of the used polynomial for generating
        the field. It is called dimension as it represents the vector
        extension of the root Galois Field.

        Returns
        -------
        int
            The dimension of the field.
        """
        raise NotImplementedError()

    @property
    def cardinality(self) -> int:
        """Gets the cardinality of the field.

        This value can easily be calculated as p^m. And it represents the
        number of elements in the field.

        Returns
        -------
        int
            The cardinality of the field.
        """
        return len(self._equivalence_classes)

    @property
    def zero(self) -> EquivalenceClass:
        """Get the zero element.

        This value represents the additive identity for the field. Meaning that
        it is the identity element for the group formed by the set and the
        addition operation.

        Returns
        -------
        EquivalenceClass
            The equivalence class corresponding to the zero element.
        """
        return self._equivalence_classes[0]

    @property
    def one(self) -> EquivalenceClass:
        """Get the one element.

        This value represents the multiplicative identity for the field.
        Meaning that it is the identity element for the group formed by the set
        and the multiplication operation.

        Returns
        -------
        EquivalenceClass
            The equivalence class corresponding to the one element.
        """
        return self._equivalence_classes[1]

    def __contains__(self, equivalence_class: EquivalenceClass) -> bool:
        """Checks if an equivalence class is part of the field.
        
        In order for this function to work it is required that the
        _equivalence_classes attribute contains all the elements of the set.

        
         Parameters
        ----------
        equivalence_class
            Equivalence class to be tested for inclusion in the field.


        Returns
        -------
        bool
            True if the equivalence class is in the set, False otherwise.
        """
        return equivalence_class in self._equivalence_classes

    def __getitem__(self, index: int) -> EquivalenceClass:
        """Gets the equivalence class with the passed index.

        As there is no notion of order in fields the only ensured property of
        the indices is that element 0 is the zero equivalence class and that
        element 1 is the one equivalence class. Even if not ensured the output
        of this function is deterministic therefore the same index will always
        yield the same output. It is important to note that a default
        implementation is provided if the _equivalence_classes attribute is
        defined.

        Parameters
        ----------
        index
            Index of the equivalence class to be fetched must be between 0
            the cardinality - 1.

        Returns
        -------
        EquivalenceClass
            The equivalence class representing the index.
        """
        return self._equivalence_classes[index]

    def __repr__(self) -> str:
        """Gets the string representation of the field.

        Returns
        -------
        str
            The string representation
        """
        return f'GF({self.cardinality})'
