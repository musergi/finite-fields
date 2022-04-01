class EquivalenceClass:
    def __contains__(self, element) -> bool:
        raise NotImplementedError()

    def __add__(self, other: 'EquivalenceClass') -> 'EquivalenceClass':
        raise NotImplementedError()

    def __sub__(self, other: 'EquivalenceClass'):
        raise NotImplementedError()

    def __mul__(self, other: 'EquivalenceClass'):
        raise NotImplementedError()

    def __floordiv__(self, other: 'EquivalenceClass'):
        raise NotImplementedError()

    def __truediv__(self, other: 'EquivalenceClass'):
        raise NotImplementedError()

    def __invert__(self):
        raise NotImplementedError()

    def __eq__(self, other):
        raise NotImplementedError()

    def __repr__(self):
        return 'EquivalenceClass'
