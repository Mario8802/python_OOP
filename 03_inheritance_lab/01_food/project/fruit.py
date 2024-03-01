from project.food import Food
import typing


class Fruit(Food):
    def __init__(self, name, expiration_date):
        super().__init__(expiration_date)
        self.name = name
        self.expiration_date = expiration_date

