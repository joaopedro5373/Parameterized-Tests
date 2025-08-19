from functions.productRepository import ProductRepository
import pytest

@pytest.mark.parametrize("product_id, resultadoEsperado",[
    (1, None)
])
def test_remove_product(product_id, resultadoEsperado):
    produto = ProductRepository()
    resultado = produto.remove_product(product_id)
    assert resultado == resultadoEsperado