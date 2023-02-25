import pytest

from src.models.restaurant import Restaurant
#pytest . --cov . --cov-report html

class TestRestaurant:
    @pytest.fixture
    def restaurante_nome(self):
        return "Bodybuilder"
    @pytest.fixture
    def restaurante_tipo(self):
        return "Comida Fit"
    @pytest.fixture
    def restaurante_aberto(self):
        return True
    @pytest.fixture
    def restaurante_fechado(self):
        return True
    @pytest.fixture
    def restaurante_atendidos(self):
        return "99"

    def test_describe_restaurant(self,restaurante_nome,restaurante_tipo):
        # setup
        restaurante = Restaurant(restaurante_nome,restaurante_tipo)
        resultado_esperado = f"Esse restaurante se chama {restaurante_nome} e serve {restaurante_tipo}.\nEsse restaturante está servindo {restaurante.number_served} consumidores desde que está aberto."
        #chamada
        resultado = restaurante.describe_restaurant()
        #avaliação
        assert resultado == resultado_esperado


    def test_open_restaurant(self,restaurante_nome,restaurante_aberto):
        #setup
        restaurante = Restaurant(restaurante_nome,restaurante_aberto)
        resultado_esperado = f"{restaurante_nome} agora está aberto!"

        #chamada
        resultado = restaurante.open_restaurant()

        #avalidação
        assert resultado == resultado_esperado
    def test_close_restaurant(self,restaurante_nome,restaurante_fechado):
        #setup
        restaurante = Restaurant(restaurante_nome, restaurante_fechado)
        resultado_esperado = f"{restaurante_nome} já está fechado!"

        #chamada
        resultado = restaurante.close_restaurant()

        #avalidação
        assert resultado == resultado_esperado

    def test_set_number_served(self,restaurante_nome,restaurante_atendidos):
        #setup
        restaurante = Restaurant(restaurante_nome, restaurante_atendidos)
        resultado_esperado = f"{restaurante_nome} está fechado!"

        #chamada
        resultado = restaurante.set_number_served(99)

        #avalidação
        assert resultado == resultado_esperado

    def test_increment_number_served(self,restaurante_nome,restaurante_atendidos):
        #setup
        restaurante = Restaurant(restaurante_nome, restaurante_atendidos)
        resultado_esperado = f"{restaurante_nome} está fechado!"

        #chamada
        resultado = restaurante.increment_number_served(1)

        #avalidação
        assert resultado == resultado_esperado



