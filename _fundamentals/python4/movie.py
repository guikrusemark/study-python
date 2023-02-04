class Movie:
    def __init__(self, title: str, year: int, rating: float):
        self.__title = title
        self.__year = year
        self.__rating = rating

    @property
    def year(self) -> int:
        return self.__year

    def __str__(self) -> str:
        return f"{self.__title} - IMDB rating: {self.__rating} - First premiered in {self.__year}"
