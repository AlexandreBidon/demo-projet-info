from business_object.watchable_content.abstract_watchable_content import AbstractWatchableContent


class Movie(AbstractWatchableContent):

    def get_providers(self):
        print(self._id)
        return 2
