from pass_analyzer.analysis import read_month
from pathlib import Path

DATA_DIR = Path(__file__).parent / 'data'

def test_read_month():
    infile = DATA_DIR / 'ted_march.csv'
    outfile = DATA_DIR / 'read_month.txt'
    read_month(infile,outfile)