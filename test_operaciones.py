# Para poder realizar las pruebas unitarias, se debe instalar pytest en el entorno virtual. Esto se puede hacer ejecutando el siguiente comando en la terminal:
# pip install pytest
# Para ver los resultados de las pruebas
# en la terminal escribir:
# pytest v-

from .modulos.operacionesSimples import suma, resta, multiplicacion, division
import pytest

def test_suma():
    assert suma(5, 3) == 8

def test_resta():
    assert resta(5, 3) == 2
    
def test_multiplicacion():
    assert multiplicacion(5, 3) == 15
    
def test_division():
    assert division(10, 2) == 5

def test_division_por_cero():
    with pytest.raises(ValueError):
        division(5, 0)