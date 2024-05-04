"""This module contains the definition of the Match class,
which represents a match in a chess tournament.
It provides methods to initialize a match with players and scores,
simulate playing the match, and obtain a string representation of the match.

Classes:
    Match: A class representing a match in a chess tournament.

Usage:
    # Create a Match instance
    # Play the match
    # Get the string representation of the match
"""
from utils.match_find_player import find_player


class Match:
    """A class representing a match in a chess tournament."""

    def __init__(self, players):

        self.players = players
        self.result = None

    def __str__(self):
        player1_name = (f"{list(self.players.keys())[0].firstname} "
                        f"{list(self.players.keys())[0].lastname}")
        player2_name = (f"{list(self.players.keys())[1].firstname} "
                        f"{list(self.players.keys())[1].lastname}")
        return (f"\nMatch: {player1_name} vs {player2_name}, "
                f"Scores: {self.players[list(self.players.keys())[0]]}-"
                f"{self.players[list(self.players.keys())[1]]}")

    def to_json(self):
        """Convert the match data to JSON format."""
        # Convertir les clés en chaînes de caractères pour les noms des joueurs
        players_json = {f"{player.firstname} {player.lastname}": score
                        for player, score in self.players.items()}

        # Créer un dictionnaire contenant les données du match
        match_json = {
            "players": players_json
        }

        return match_json

    @classmethod
    def from_json(cls, match_data, tournament):
        """Create a Match instance from JSON data.

        Args:
            match_data (dict):
            The JSON data representing the match.
            tournament (Tournament):
            The tournament instance to search for players.

        Returns:
            Match: A Match instance created from the JSON data.
        """
        # Récupérer les données des joueurs depuis le JSON
        players_data = match_data["players"]

        # Créer un dictionnaire pour stocker les objets Player et leurs scores
        players = {}
        for player_name, score in players_data.items():
            split_index = player_name.find(" ")
            if split_index != -1:
                player_firstname = player_name[:split_index]
                player_lastname = player_name[split_index + 1:]
            else:
                player_firstname = player_name
                player_lastname = ""
            player = find_player(tournament, player_firstname, player_lastname)
            if player:
                players[player] = score
            else:
                print(f"Joueur introuvable dans "
                      f"la liste des joueurs du tournoi : {player_name}")

        match = cls(players)
        return match

    def play_match(self):
        # Afficher les détails du match
        player1 = list(self.players.keys())[0]
        player2 = list(self.players.keys())[1]
        player1_name = (f"{list(self.players.keys())[0].firstname} "
                        f"{list(self.players.keys())[0].lastname}")
        player2_name = (f"{list(self.players.keys())[1].firstname} "
                        f"{list(self.players.keys())[1].lastname}")
        print(f"Match: {player1_name} contre {player2_name}")

        # Demander à l'utilisateur de saisir le résultat
        while True:
            result_input = input(f"{player1_name} (win/loss/draw):  ")
            if result_input.lower() in ["win", "loss", "draw"]:
                result = result_input.lower()
                break
            else:
                print("\033[91mVeuillez entrer "
                      "'win', 'loss' ou 'draw'.\033[0m")

        # Assigner le résultat du match à la variable d'instance self.result
        self.result = result

        # Mise à jour les scores des joueurs en fonction du résultat
        if result == "win":
            winning_player = player1
        elif result == "loss":
            winning_player = player2
        else:
            winning_player = None

        if winning_player:
            self.players[winning_player] += 1
        else:
            for player in self.players:
                self.players[player] += 0.5

        return result


if __name__ == "__main__":
    pass
