class Game:
    def __init__(self, name, category, description, rating=0):
        self.name = name
        self.category = category
        self.description = description
        self.rating = rating

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category):
        self._category = category

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, rating):
        self._rating = rating

    def __str__(self):
        return f'Game: {self.name} - {self.description}'
