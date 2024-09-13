from abc import ABC, abstractmethod


class AbstractWatchableContent(ABC):

    def __init__(self, name: str, id: str, description: str):
        self._name = name
        self._id = id
        self._description = description

    @abstractmethod
    def get_providers():
        """
        Permet de récupérer la liste des plateformes
        """
        pass

    def add_to_watchlist():
        pass
