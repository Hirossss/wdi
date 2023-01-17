class Figure:

    def __init__(self,name):
        self.name = name

class Bishop(Figure):

    def __init__(self,name,posx,posy):
        super().__init__(name)              #uwzgledniamy stara zmienna "imie figury" utworzona w wyzszej klasie, mechanizm dziedziczenia
        self.posx=posx
        self.posy=posy

