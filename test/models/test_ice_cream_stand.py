import pytest

from src.models.ice_cream_stand import IceCreamStand

class TestIceCreamStand:
    @pytest.fixture
    def restaurante_nome(self):
        return "Pinguim-real"
    @pytest.fixture
    def restaurante_tipo(self):
        return "Sorveteria"
    @pytest.fixture
    def lista_sabores(self):
        return ["Morango", "Chocolate", "Creme"]
    @pytest.fixture
    def lista_sabores_sem(self):
        return []

    def test_flavors_available(self,restaurante_nome, restaurante_tipo, lista_sabores):
        # setup
        sorveteria = IceCreamStand(restaurante_nome, restaurante_tipo, lista_sabores)
        # chamada
        resultado = sorveteria.flavors_available()
        # avaliação
        assert resultado == lista_sabores

    def test_flavors_available_sem_sabor(self,restaurante_nome, restaurante_tipo, lista_sabores_sem):
        # setup
        sorveteria = IceCreamStand(restaurante_nome, restaurante_tipo, lista_sabores_sem)
        resultado_esperado = f"Estamos sem estoque atualmente!"
        # chamada
        resultado = sorveteria.flavors_available()
        # avaliação
        assert resultado == resultado_esperado
        #assert sorveteria.flavors == [] validar que não tem de fato


    def test_find_flavor(self, restaurante_nome, restaurante_tipo, lista_sabores):
        # setup
        sorveteria = IceCreamStand(restaurante_nome, restaurante_tipo, lista_sabores)
        sabor_buscado = "Creme"
        resultado_esperado = f"Temos no momento {sabor_buscado}!"
        # chamada
        resultado = sorveteria.find_flavor(sabor_buscado)
        # avaliação
        assert resultado == resultado_esperado

    def test_find_flavor_nao_tem(self, restaurante_nome, restaurante_tipo, lista_sabores):
        # setup
        sorveteria = IceCreamStand(restaurante_nome, restaurante_tipo, lista_sabores)
        sabor_buscado = "Flocos"
        resultado_esperado = f"Não Temos no momento {sabor_buscado}!"
        # chamada
        resultado = sorveteria.find_flavor(sabor_buscado)
        # avaliação
        assert resultado == resultado_esperado

    def test_find_flavor_sem_estoque(self, restaurante_nome, restaurante_tipo, lista_sabores):
        # setup
        sorveteria = IceCreamStand(restaurante_nome, restaurante_tipo, lista_sabores)
        sabor_buscado = []
        resultado_esperado = f"Estamos sem estoque atualmente!"
        # chamada
        resultado = sorveteria.find_flavor(sabor_buscado)
        # avaliação
        assert resultado == resultado_esperado

    def test_add_flavor(self, restaurante_nome, restaurante_tipo, lista_sabores):
        # setup
        sorveteria = IceCreamStand(restaurante_nome, restaurante_tipo, lista_sabores)
        novo_sabor = "Napolitano"
        resultado_esperado = f"{novo_sabor} adicionado ao estoque!"
        # chamada
        resultado = sorveteria.add_flavor(novo_sabor)
        # avaliação
        assert resultado == resultado_esperado

    def test_add_flavor(self, restaurante_nome, restaurante_tipo, lista_sabores):
        # setup
        sorveteria = IceCreamStand(restaurante_nome, restaurante_tipo, lista_sabores)
        novo_sabor = "Chocolate"
        resultado_esperado = f"\nSabor já disponivel!"
        # chamada
        resultado = sorveteria.add_flavor(novo_sabor)
        # avaliação
        assert resultado == resultado_esperado


