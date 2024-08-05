# type:ignore
"""
Flyweight é um padrão de projeto estrutural que tem a intenção de usar
compartilhamento
para suportar eficientemente grandes quantidades de objetos de forma granular.

Só use o Flyweight quanto TODAS as condições a seguir forem verdadeiras:

- uma aplicação utiliza uma grande quantidade de objetos;
- os custos de armazenamento são altos por causa da grande quantidade de
objetos;
- a maioria dos estados de objetos podem se tornar extrínsecos;
- muitos objetos podem ser substituídos por poucos objetos compartilhados;
- a aplicação não depende da identidade dos objetos.

Importante:
- Estado intrínseco é o estado do objeto que não muda, esse estado deve estar
dentro do objeto flyweight;
- Estado extrínseco é o estado do objeto que muda, esse estado pode ser movido
para fora do objeto flyweight;

Dicionário:
Intrínseco - que faz parte de ou que constitui a essência, a natureza de algo;
que é próprio de algo; inerente.
Extrínseco - que não pertence à essência de algo; que é exterior.
"""
from __future__ import annotations
from typing import List, Dict


# Context
class Client:
    def __init__(self, name: str) -> None:
        self.name = name
        self._addresses: List = []

        # Address Data - Extrinsic
        self.addresses_number: str
        self.addresses_details: str

    def add_address(self, address: Address) -> None:
        self._addresses.append(address)

    def list_addresses(self) -> None:
        for address in self._addresses:
            address.show_address(self.addresses_number,
                                 self.addresses_details)


# Flyweight
class Address:
    def __init__(self, street: str, neighborhood: str, zip_code: str) -> None:
        self._street = street
        self._neighborhood = neighborhood
        self._zip_code = zip_code

    def show_address(self, address_number: str, address_details: str) -> None:
        print(
            self._street, address_number, self._neighborhood, address_details,
            self._zip_code
        )


class AddressFactory:
    _addresses: Dict = {}  # Flyweight Pool

    def _get_key(self, **kwargs) -> StopAsyncIteration:
        return ''.join(kwargs.values())

    def get_address(self, **kwargs):
        key = self._get_key(**kwargs)

        try:
            address_flyweight = self._addresses[key]
            print('Usando o objeto já criado!')
        except KeyError:
            address_flyweight = Address(**kwargs)
            self._addresses[key] = address_flyweight
            print('Criando novo objeto!')

        return address_flyweight


if __name__ == '__main__':
    address_factory = AddressFactory()

    a1 = address_factory.get_address(
        street='AV. Brasil',
        neighborhood='Centro',
        zip_code='11111-111'
    )

    a2 = address_factory.get_address(
        street='AV. Brasil',
        neighborhood='Centro',
        zip_code='11111-111'
    )

    gabriel = Client('Gabriel')
    gabriel.addresses_number = '50'
    gabriel.addresses_details = 'Casa'
    gabriel.add_address(a1)
    gabriel.list_addresses()

    print()

    joana = Client('Joana')
    joana.addresses_number = '250A'
    joana.addresses_details = 'AP 555'
    joana.add_address(a1)
    joana.list_addresses()

    print(a1 == a2)
