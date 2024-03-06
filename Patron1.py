
class ItaxLocation:
    def tax():
        pass

class TaxUSA(ItaxLocation):
    def tax():
        return "Impuestos del 15%"

class TaxCol(ItaxLocation):
    def tax():
        return "Impuestos del 20%"

class TaxEur(ItaxLocation):
    def tax():
        return "Impuestos del 10%"

class Patrimonio:
    def __init__(self, taxLocation:ItaxLocation) -> None:
        self.taxLocation = taxLocation
    
    def val_tax(self):
        return self.taxLocation.tax()



class Colombian_money(Patrimonio):
    def __init__(self) -> None:
        super().__init__(TaxCol)
    
    def __str__(self) -> str:
        return "Manejamos pesos Colombianos y tenemos " + self.val_tax()
    


class USA_money(Patrimonio):
    def __init__(self) -> None:
        super().__init__(TaxUSA)
    
    def __str__(self) -> str:
        return "Manejamos dolares y tenemos " + self.val_tax()
    


col= Colombian_money()
us = USA_money()
print(col)
print(us)