class StringReprMixin:
    def __str__(self):
        params = ', '.join([f'{k}={v}' for k, v in self.__dict__.items()])
        return f'{self.__class__.__name__}({params})'

    def __repr__(self):
        return self.__str__()


class MonoState(StringReprMixin):
    _state = {}

    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls)
        obj.__dict__ = cls._state
        return obj

    def __init__(self, nome=None, sobrenome=None):
        self.__dict__ = self._state

        if nome is not None:
            self.nome = nome

        if sobrenome is not None:
            self.sobrenome = sobrenome


class A(MonoState):
    ...


if __name__ == '__main__':
    m1 = MonoState(nome='Gabriel')
    m2 = A(sobrenome="Galacci")
    print(m1)
    print(m2)
