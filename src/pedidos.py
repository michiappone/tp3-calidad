"""Cálculo de pedidos: importes enteros en centavos, sin redondeos implícitos."""


def calcular_total(precio_centavos: int, cantidad: int) -> int:
    """Rechaza booleanos, tipos no enteros, precios negativos y cantidades < 1."""
    if type(precio_centavos) is not int or type(cantidad) is not int:
        raise TypeError("Precio y cantidad deben ser enteros")
    if precio_centavos < 0:
        raise ValueError("El precio no puede ser negativo")
    if cantidad < 1:
        raise ValueError("La cantidad debe ser mayor que cero")
    return precio_centavos * cantidad
