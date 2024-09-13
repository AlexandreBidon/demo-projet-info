from business_object.watchable_content.abstract_watchable_content import AbstractWatchableContent
from tmdb.search_movie import get_movie_by_id
from tmdb.providers import get_providers_for_movie


class Movie(AbstractWatchableContent):

    def __init__(self, id: int):
        # Rechercher le film
        # Si on ne le trouve pas -> erreur
        try:
            result = get_movie_by_id(id)
            name = result["name"]
            description = result["description"]
            providers = get_providers_for_movie(id)
        except Exception as e:
            print(e)
            raise Exception("Impossible de créer le film, l'id n'est surement pas bon")
        super().__init__(
            name=name,
            id=id,
            description=description,
            providers=providers
        )

    def __str__(self):
        return f"#### {self._name} ####\n\n{self._description}\n\nCe film est disponible sur:\n{self._providers}"
