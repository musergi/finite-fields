class EquivalenceClass:
    """Class for representing equivalence classes.

    This class is intended to be used as the base class for all equivalence
    classes. It does not implement any of the methods only providing an
    interface to be implemented by all subclasses.
    """

    @property
    def zero(self) -> 'EquivalenceClass':
        """Zero element of the field of the equivalence class.
        
        Gets the identity of the additive group in the field which contains
        this equivalence class.
        
        Returns
        -------
        EquivalenceClass:
            Equivalence class representing the zero element.
        """
        raise NotImplementedError()

    @property
    def is_zero(self) -> bool:
        """Test if the equivalence class is zero.

        Test if the equivalence class is the identity element in the additive
        group.

        Returns
        -------
        bool:
            True is it is zero, False otherwise
        """
        return self == self.zero

    def __contains__(self, element: int) -> bool:
        """Tests if an integer is in the equivalence class.

        The base of an equivalence class is that it represents an infinite set
        of values. This function test if a particular integer value is in the
        equivalence class, in other words part of the set.

        Parameters
        ----------
        element:
            Integer that will be tested for inclusion in the test.

        Returns
        -------
        bool:
            True if the integer is in the class, False otherwise.
        """
        raise NotImplementedError()

    def __add__(self, other: 'EquivalenceClass') -> 'EquivalenceClass':
        """Adds two equivalence classes.
        
        Parameters
        ----------
        other:
            The second operand of the addition.

        Returns
        -------
        EquivalenceClass
            The result of the addition.
        
        """
        raise NotImplementedError()

    def __sub__(self, other: 'EquivalenceClass') -> 'EquivalenceClass':
        """Substracts two equivalence classes.
        
        Parameters
        ----------
        other:
            The second operand of the substraction.

        Returns
        -------
        EquivalenceClass
            The result of the substraction.
        
        """
        raise NotImplementedError()

    def __mul__(self, other: 'EquivalenceClass') -> 'EquivalenceClass':
        """Muplies two equivalence classes.
        
        Parameters
        ----------
        other:
            The second operand of the multiplication.

        Returns
        -------
        EquivalenceClass
            The result of the multiplication.
        
        """
        raise NotImplementedError()

    def __floordiv__(self, other: 'EquivalenceClass') -> 'EquivalenceClass':
        """Divides two equivalence classes.
        
        Parameters
        ----------
        other:
            The second operand of the division.

        Returns
        -------
        EquivalenceClass
            The result of the division.
        
        """
        raise NotImplementedError()

    def __truediv__(self, other: 'EquivalenceClass'):
        """Divides two equivalence classes.
        
        Parameters
        ----------
        other:
            The second operand of the division.

        Returns
        -------
        EquivalenceClass
            The result of the division.
        
        """
        raise NotImplementedError()

    def __invert__(self) -> 'EquivalenceClass':
        """Gives the inverse of the equivalence class.

        Returns
        -------
        EquivalenceClass
            The inverse of the equivalence class.
        
        """
        raise NotImplementedError()

    def __eq__(self, other: 'EquivalenceClass') -> bool:
        """Tests for equiality with another equivalence class.
        
        Parameters
        ----------
        other
            The second operand of the comparison.

        Returns
        -------
        bool
            True if the equivalence classes are equal, False otherwise
        """
        raise NotImplementedError()

    def __repr__(self):
        """String representation of the equivalence class.

        Retruns
        -------
        str
            The string representation of the equivalence class.
        """
        return 'EquivalenceClass'
