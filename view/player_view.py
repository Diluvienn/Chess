"""
This module defines functions and a class for managing user input
and displaying player information.

"""
from utils.formatvalidator import (validate_date_format,
                                   validate_national_chess_id_format)


def get_player_info_from_user(context="principal"):
    """Get information of a new player from user input."""
    firstname = None
    lastname = None
    birth = None
    national_chess_id = None

    while True:
        if context == "principal":
            print("\n\033[92mRetour au menu principal "
                  "sans sauvegarde: 'q'\033[0m")
        else:
            print("\n\033[92mRetour au menu précédent "
                  "sans sauvegarde: 'q'\033[0m")
        choice = input("\nEntrez le prénom du joueur: ")

        if choice.lower() == 'q':
            if context == "principal":
                confirmation = input("\033[92mVoulez-vous vraiment "
                                     "retourner au menu principal "
                                     "sans sauvegarder ? (y/n):\033[0m ")
                confirmation_text = "Retour au menu principal sans sauvegarde."
            else:
                confirmation = input("\033[92mVoulez-vous vraiment "
                                     "retourner au menu précédent "
                                     "sans sauvegarder ? (y/n):\033[0m ")
                confirmation_text = "Retour au menu précédent sans sauvegarde."

            if confirmation.lower() == 'y':
                print(confirmation_text)
                return None, None, None, None
            else:
                continue

        firstname = choice.title()
        if all(char.isalpha() or char == '-' for char in firstname):
            break
        else:
            print("\033[91mLe prénom ne peut contenir "
                  "que des lettres et des tirets. "
                  "Veuillez réessayer.\033[0m")
    while True:
        choice = input("Entrez le nom de famille du joueur: ").title()

        if choice.lower() == 'q':
            confirmation = input("\033[92mVoulez-vous vraiment "
                                 "retourner au menu principal "
                                 "sans sauvegarder ? (y/n):\033[0m ")
            if confirmation.lower() == 'y':
                print("Retour au menu principal sans sauvegarde.")
                return None, None, None, None
            else:
                continue

        lastname = choice
        if lastname.replace(' ', '').isalpha():
            break
        else:
            print("\033[91mLe nom de famille ne peut contenir "
                  "que des lettres et des espaces. "
                  "Veuillez réessayer.\033[0m")

    while True:
        choice = input("Entrez la date de naissance du joueur "
                       "(format: DD-MM-YYYY): ")

        if choice.lower() == 'q':
            confirmation = input("\033[92mVoulez-vous vraiment "
                                 "retourner au menu principal "
                                 "sans sauvegarder ? (y/n):\033[0m ")
            if confirmation.lower() == 'y':
                print("Retour au menu principal sans sauvegarde.")
                return None, None, None, None
            else:
                continue

        birth = choice
        if validate_date_format(birth):
            break
        else:
            print("\033[91mFormat de date invalide. "
                  "Veuillez utiliser le format 'DD-MM-YYYY'. "
                  "Veuillez réessayer.\033[0m")

    while True:
        choice = input("Entrez l'identifiant national du joueur "
                       "(format: AB12345): ").upper()

        if choice.lower() == 'q':
            confirmation = input("\033[92mVoulez-vous vraiment "
                                 "retourner au menu principal "
                                 "sans sauvegarder ? (y/n):\033[0m ")
            if confirmation.lower() == 'y':
                print("Retour au menu principal sans sauvegarde.")
                return None, None, None, None
            else:
                continue

        national_chess_id = choice
        if validate_national_chess_id_format(national_chess_id):
            break
        else:
            print("\033[91mFormat d'identifiant national invalide. "
                  "Veuillez utiliser le format 'AB12345'.\033[0m")

    return firstname, lastname, birth, national_chess_id


class PlayerView:
    """Class for displaying player information."""
    def __init__(self, player_repository):
        self.player_repository = player_repository

    def show_players(self):
        """Display the list of players."""
        self.player_repository.load_players()
        self.player_repository.display_players_by_index()
