"""
Composite é um padrão de projeto estrutural que permite que
você utilize a composição para criar objetos em estruturas
de árvores. O padrão permite aos clientes tratarem de maneira
uniforme objetos individuais (Leaf) e composições de
objetos (Composite).

IMPORTANTE: só aplique este padrão em uma estrutura que possa
ser representada em formato hierárquico (árvore).

No padrão composite, temos dois tipos de objetos:
Composite (que representa nós internos da árvore) e Leaf
(que representa nós externos da árvore).

Objetos Composite são objetos mais complexos e com filhos.
Geralmente, eles delegam trabalho para os filhos usando
um método em comum.
Objetos Leaf são objetos simples, da ponta e sem filhos.
Geralmente, são esses objetos que realizam o trabalho
real da aplicação.
"""
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


# Component
class BoxStructure(ABC):
    @abstractmethod
    def print_content(self) -> None: pass

    @abstractmethod
    def get_price(self) -> float: pass

    def add(self, child: BoxStructure) -> None: pass
    def remove(self, child: BoxStructure) -> None: pass


# Composite
class Box(BoxStructure):
    def __init__(self, name) -> None:
        self.name = name
        self._children: List[BoxStructure] = []

    def print_content(self) -> None:
        print(f'\n{self.name}: ')
        for child in self._children:
            child.print_content()

    def get_price(self) -> float:
        return sum([
            child.get_price() for child in self._children
        ])

    def add(self, child: BoxStructure) -> None:
        self._children.append(child)

    def remove(self, child: BoxStructure) -> None:
        if child in self._children:
            self._children.remove(child)


# Leaf
class Product(BoxStructure):
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

    def print_content(self) -> None:
        print(self.name, self.price)

    def get_price(self) -> float:
        return self.price


if __name__ == '__main__':
    # Leaf
    camiseta1 = Product('camiseta1', 49.90)
    camiseta2 = Product('camiseta2', 19.90)
    camiseta3 = Product('camiseta3', 10.90)

    # Composite
    caixa_camisetas = Box('Caixa de camisetas')
    caixa_camisetas.add(camiseta1)
    caixa_camisetas.add(camiseta2)
    caixa_camisetas.add(camiseta3)

    # Leaf
    smartphone1 = Product('smartphone1', 9000)
    smartphone2 = Product('smartphone2', 11000)

    # Composite
    caixa_smatphones = Box('Caixa de smartphones')
    caixa_smatphones.add(smartphone1)
    caixa_smatphones.add(smartphone2)

    # Composite
    caixa_grande = Box('Caixa grande')
    caixa_grande.add(caixa_camisetas)
    caixa_grande.add(caixa_smatphones)
    caixa_grande.print_content()
    print(caixa_grande.get_price())
