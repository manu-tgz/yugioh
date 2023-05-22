from ..domain.queries import DeckQueries

class DeckUseCases():
    def player_amount():
        return DeckQueries.gb_player('player', 'id')
        