import pandas as pd
from pass_analyzer.transaction import Transaction, get_true_fare
from pass_analyzer.products import StoredValue, MonthlyPass

def read_month(infile,outfile):
    data = pd.read_csv(infile)
    transactions = []
    for row in data.iterrows():
        dat = row[1]
        transactions.append(Transaction.from_pandas_row(dat))
    stored_value = StoredValue()
    fares = [2.0,2.25,2.5,2.75,3.0,3.25,3.5,3.75,4.0,4.25]
    passes = [stored_value] + [MonthlyPass.from_fare(fare) for fare in fares]
    with open(outfile,'wt', encoding='UTF-8') as file:
        w1,w2,w3 = 15,10,10
        file.write(f'{"Product Type": <25}{"Min Cost": <10}{"Max Cost": <10}\n')
        for p in passes:
            tmin, tmax = p.cost,p.cost # total
            for t in transactions:
                fmin, fmax = t.true_fare # fares
                cmin = p.use(fmin,t.operator) # cost
                cmax = p.use(fmax,t.operator)
                tmin += cmin
                tmax += cmax
            file.write(f'{str(p): <25}${tmin:<10.2f}${tmax:<10.2f}\n')

