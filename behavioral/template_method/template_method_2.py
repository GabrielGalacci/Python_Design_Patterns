"""
Template Method (comportamental) tem a intenção de definir
um algoritmo em um método, postergando alguns passos
para as subclasses por herança. Template method permite
que subclasses redefinam certos passos de um algoritmo
sem mudar a estrutura do mesmo.

Também é possível definir hooks para que as subclasses
utilizem caso necessário.

The Hollywood principle: "Don't Call Us, We'll Call You."
(IoC - Inversão de controle)
"""
from abc import ABC, abstractmethod


# Classe Abstrata
class Pizza(ABC):
    # Template Method
    def prepare(self) -> None:
        self.hook_before_add_ingredients()  # Hook
        self.add_ingredients()  # Abstract
        self.hook_after_add_ingredients()  # Hook
        self.cook()  # Abstract
        self.cut()  # Concreto
        self.serve()  # Concreto

    def hook_before_add_ingredients(self) -> None: pass

    def hook_after_add_ingredients(self) -> None: pass

    def cut(self) -> None:
        print(f'{self.__class__.__name__}: Cortando pizza!')

    def serve(self) -> None:
        print(f'{self.__class__.__name__}: Servindo pizza!')

    @abstractmethod
    def add_ingredients(self) -> None: pass

    @abstractmethod
    def cook(self) -> None: pass


class AModa(Pizza):
    def add_ingredients(self) -> None:
        print('AModa - Adicionando ingredientes: Presunto, Queijo, Goiabada')

    def cook(self) -> None:
        print('AModa - Cozinhando por 45 minutos no forno a lenha!')


class Veggie(Pizza):
    def hook_before_add_ingredients(self) -> None:
        print('Veggie - Lavando Ingredientes!')

    def add_ingredients(self) -> None:
        print('Veggie - Adicionando ingredientes: ingredientes veganos')

    def cook(self) -> None:
        print('Veggie - Cozinhando por 15 minutos no forno comum!')


if __name__ == '__main__':
    a_moda = AModa()
    a_moda.prepare()

    print()

    veggie = Veggie()
    veggie.prepare()
