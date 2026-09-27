import pytest

from src.pedidos import calcular_total


@pytest.mark.parametrize(
    "precio,cantidad,esperado", [(150000, 3, 450000), (0, 2, 0), (1, 1, 1)]
)
def test_total_valido(precio, cantidad, esperado):
    assert calcular_total(precio, cantidad) == esperado


@pytest.mark.parametrize("precio,cantidad", [(-1, 1), (100, 0), (100, -1)])
def test_rechaza_valores_invalidos(precio, cantidad):
    with pytest.raises(ValueError):
        calcular_total(precio, cantidad)


@pytest.mark.parametrize(
    "precio,cantidad",
    [(1.5, 1), (100, 1.5), (True, 1), (100, False), ("100", 1), (100, None)],
)
def test_rechaza_tipos_invalidos(precio, cantidad):
    with pytest.raises(TypeError):
        calcular_total(precio, cantidad)
