from functions.productRepository import ProductRepository
import pytest

@pytest.mark.parametrize("id, resultadoEsperado",{
    (1, None)
})
def test_get_product(id, resultadoEsperado):
    produto = ProductRepository()
    resultado = produto.get_product(id)
    assert resultado == resultadoEsperado