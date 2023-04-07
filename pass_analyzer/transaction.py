"""
Transaction class
"""
import datetime

from products import Product, MonthlyPass, StoredValue

class Transaction:
    """
    Transaction with WMATA
    """
    def __init__(
            self,
            time:datetime.datetime,
            desc:str,
            operator:str,
            entry:str,
            exit:str,
            product:Product,
            remaining_rides:int,
            change:float,
            balance:float
    ):
        self.time = time
        self.desc = desc
        self.operator = operator
        self.entry = entry
        self.exit = exit
        self.product = product
        self.remaining_rides = remaining_rides
        self.change = change
        self.balance = balance
    @classmethod
    def from_pandas_row(cls,row):
        time = row['Time']
        time = datetime.datetime.strptime(time,'%m/%d/%y %I:%M %p')
        desc = row['Description']
        operator = row['Operator']
        entry = row['Entry Location/ Bus Route']
        exit = row['Exit Location']
        product_str = row['Product']
        if 'stored value' in product_str.lower():
            product = StoredValue()
        elif 'monthly unlimited pass' in product_str.lower():
            _,s = product_str.split('$')
            fare = float(s[:4])
            product = MonthlyPass.from_fare(fare)
        else:
            raise ValueError(f'Unknown product {product_str}')
        
        try:
            remaining_rides = int(row['Rem. Rides'])
        except ValueError:
            remaining_rides = None
        
        change_str = row['Change (+/-)']
        k = 1
        if '(' in change_str:
            k = -1
        change = k * float(change_str.split[1][:4])
        balance = float(row['Balance'].replace('$',''))

        return cls(
            time,
            desc,
            operator,
            entry,
            exit,
            product,
            remaining_rides,
            change,
            balance
        )