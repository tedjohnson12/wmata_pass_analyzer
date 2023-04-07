
import pytest
import pandas as pd
from os import chdir
from pathlib import Path
from pass_analyzer.transaction import Transaction, get_true_fare
from pass_analyzer.products import MonthlyPass, StoredValue

def test_get_true_fare():
    p = MonthlyPass.from_fare(2.00)
    op = 'Metrorail'
    change = 1.8
    assert get_true_fare(p,op,change) == (3.8,3.8)
    change = 0.0
    assert get_true_fare(p,op,change) == (2.0,2.0)
    op = 'Metrobus'
    assert get_true_fare(p,op,change) == (2.0,2.0)
    op = 'PGC'
    change = 1.0
    assert get_true_fare(p,op,change) == (1.0,1.0)

    p = MonthlyPass.from_fare(2.50)
    op = 'Metrorail'
    change = 1.3
    assert get_true_fare(p,op,change) == (3.8,3.8)
    change = 0.0
    assert get_true_fare(p,op,change) == (2.0,2.5)

    p = StoredValue()
    op = 'Metrorail'
    change = 2.0
    assert get_true_fare(p,op,change) == (2.0,2.0)





def test_transaction():
    datapath = Path(__file__).parent / 'data' / 'ted_march.csv'
    data = pd.read_csv(datapath)
    for row in data.iterrows():
        dat = row[1]
        t = Transaction.from_pandas_row(dat)
    