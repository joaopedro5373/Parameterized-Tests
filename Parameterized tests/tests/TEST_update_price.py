from functions.Product import Product
import pytest

@pytest.mark.parametrize("new_buyprice, new_sellprice, resultadoEsperado",[
    (3, 3, None),
    (None, 1, ValueError)
])
def test_update_price(new_buyprice, new_sellprice, resultadoEsperado):

    produto = Product(id = 1, name = "batata", buyprice=1, sellprice=2, weight=3, volume=5)

    if isinstance(resultadoEsperado, type) and issubclass(resultadoEsperado, Exception):
        with pytest.raises(resultadoEsperado):
            produto.update_price(new_buyprice, new_sellprice)
    else:
        resultado = produto.update_price(new_buyprice, new_sellprice)
        assert resultado == resultadoEsperado