"""
Product classes
"""

class Product:
    def __init__(self,cost:float):
        self.cost = cost
    def _use(self,price:float,operator:str):
        return price
    def use(self,price:float,operator:str):
        return self._use(price,operator)

class MonthlyPass(Product):
    def __init__(self,cost,fare):
        self.cost = cost
        self.fare = fare
    def _use(self,price:float,operator:str):
        if operator == 'Metrorail':
            return max(0,price - self.fare)
        elif operator == 'Metrobus':
            return 0
        else:
            return price
    @classmethod
    def from_fare(cls,fare):
        return cls(fare*32,fare)

class StoredValue(Product):
    def __init__(self):
        self.cost = 0
