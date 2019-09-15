import os

class Suggestion:
    def __init__(self, _game_name, _match_score):
        self.game_name = _game_name
        self.match_score = _match_score

    def return_game_name(self):
        return self.game_name
