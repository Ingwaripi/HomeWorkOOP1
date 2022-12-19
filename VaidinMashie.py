"""Устанавливаем режим доступа Protected в классах"""
class VaidingMashine():
    
    def __init__(self, name, prise):
        self._name = name
        self._prise = prise


class HotDrink(VaidingMashine):
    """Устанавливаем максимальную температуру напитков"""
    def __init__(self, name, prise, temperature=45):
        super().__init__(name, prise)
        self._temperature = temperature

class HotDrinkVaidingMashine(HotDrink):
    
    def __init__(self, name, prise):
        super().__init__(name, prise)

    def getProduct(self):
        print(f"Name: {self._name} Price: {self._prise} Standard temperature: {self._temperature}")
    
pt = HotDrinkVaidingMashine('Expresso', 75)
pt.getProduct()
rt = HotDrink('capuchino', 33)
print(rt.__dict__)



