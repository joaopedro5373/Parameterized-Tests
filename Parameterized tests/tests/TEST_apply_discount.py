from functions.Product import Product
import pytest

@pytest.mark.parametrize("discount_percentage, resultadoEsperado",[
    (10, 90),
    (200, ValueError)
])
def test_apply_discount(discount_percentage, resultadoEsperado):
    produto = Product(id = 1, name = "batata", buyprice=1, sellprice=100, weight=3, volume=5)

    if isinstance(resultadoEsperado, type) and issubclass(resultadoEsperado, ValueError):
        with pytest.raises(resultadoEsperado):
            produto.apply_discount(discount_percentage)
    else:
        resultado = produto.apply_discount(discount_percentage)
        assert resultado == resultadoEsperado