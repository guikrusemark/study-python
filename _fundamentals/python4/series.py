class Series:
    def __init__(self, title: str, number_of_seasons: int, number_of_episodes: int, premiered_in: int):
        self.__title = title
        self.__number_of_seasons = number_of_seasons
        self.__number_of_episodes = number_of_episodes
        self.__premiered_in = premiered_in

    def __str__(self) -> str:
        return f"{self.__title} - {self.__number_of_seasons} Seasons - First premiered in {self.__premiered_in}"
