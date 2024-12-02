class Soda:


    def __init__(self,water = None):
        self.water = water

    def show_my_drink(self):
        if self.water:
            print(f'Газировка и {self.water}')
        else:
            print('Обычная газировка')


drink1 = Soda()
drink2 = Soda('Малина')
drink1.show_my_drink()
drink2.show_my_drink()