"""
test products
"""
import pytest
from pass_analyzer.products import Product, MonthlyPass, StoredValue

def test_Product():
    p = Product(20.00)
    assert p.use(2.00,'Metrorail') == pytest.approx(2.00,rel=1e-6)

def test_MonthlyPass():
    p = MonthlyPass(20.00,2.50)
    assert p.use(2.00,'Metrorail') == pytest.approx(0.00,rel=1e-6)
    assert p.use(3.00,'Metrorail') == pytest.approx(0.50,rel=1e-6)
    assert p.use(3.00,'Metrobus') == pytest.approx(0.00,rel=1e-6)
    assert p.use(1.00,'PGC bus') == pytest.approx(1.00,rel=1e-6)

    p = MonthlyPass.from_fare(2.00)
    assert p.cost == pytest.approx(64.00,rel=1e-6)

def test_StoredValue():
    p = StoredValue()
    assert p.use(2.00,'Metrorail') == pytest.approx(2.00,rel=1e-6)
    assert p.cost == pytest.approx(0.00,rel=1e-6)