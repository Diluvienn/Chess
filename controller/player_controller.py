"""Module containing the PlayerController class.

This module provides a controller class
for managing player-related operations,
such as displaying players,
creating new players,
and adding players to the list.

Classes:
    PlayerController:
    A controller class for managing player-related operations.
"""

from model.player import Player
from view.player_view import get_player_info_from_user


class PlayerController:
    """A controller class for managing player-related operations.

    Attributes:
        player_repository (PlayerRepository):
        An instance of PlayerRepository for managing player data.
        player_view (PlayerView):
        An instance of PlayerView for displaying player-related views.

    """

    def __init__(self, player_repository, player_view):
        self.player_repository = player_repository
        self.player_view = player_view

    def show_players(self):
        """Display the list of players."""
        sorted_players = (
            self.player_repository.get_player_by_alphabetical_order())
        if not sorted_players:
            print("Aucun joueur enregistré pour le moment.")
        else:
            print("Liste des joueurs :\n")
            for index, player_info in enumerate(sorted_players, start=1):
                print(f"{index}. "
                      f"{player_info['lastname']} {player_info['firstname']}")

            while True:
                choice = input("\nSouhaitez-vous les détails d'un joueur ? "
                               "(y/n): ").lower()
                if choice == "n":
                    break
                elif choice == "y":
                    print("\n\033[92mRetour au menu principal : 'q'.\033[0m")
                    player_index = input("Veuillez "
                                         "indiquer l'index du joueur : ")
                    if player_index != "q":
                        try:
                            player_index = int(player_index)
                            if 1 <= player_index <= len(sorted_players):
                                player_info = sorted_players[player_index - 1]
                                print("\nDétails du joueur :\n")
                                print(f"Nom: {player_info['lastname']} "
                                      f"{player_info['firstname']}")
                                print(f"Date de naissance: {player_info['birth']}")
                                print(f"Identifiant national d'échecs: {player_info['national chess ID']}")
                            else:
                                print("\033[91mIndex invalide.\033[0m")
                        except ValueError:
                            print("\033[91mVeuillez entrer un numéro valide.\033[0m")
                    else:
                        return

    def create_new_player(self):
        """Obtain player information and create a Player object."""
        firstname, lastname, birth, national_chess_id = (
            get_player_info_from_user())

        # de retour au menu principal sans sauvegarder
        if firstname is None:
            return

        new_player = Player(firstname, lastname, birth, national_chess_id)
        print(f"La joueuse ou le joueur "
              f"{new_player.firstname} {new_player.lastname} "
              f"a bien été ajouté.e à la liste.")
        self.player_repository.add_player(new_player)
        return new_player

    def add_player(self):
        """Add a new player to the list of players."""
        player_info = self.player_view.create_player()
        if player_info is not None:
            new_player = Player(*player_info)
            self.player_repository.add_player(new_player)
