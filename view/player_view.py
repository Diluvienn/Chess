from utils.formatvalidator import validate_date_format, validate_national_chess_id_format


def get_player_info_from_user():
    """Obtient les informations d'un nouveau joueur depuis l'entrée utilisateur."""
    while True:
        firstname = input("\nEntrez le prénom du joueur: ").title()
        if all(char.isalpha() or char == '-' for char in firstname):
            break
        else:
            print("\033[91mLe prénom ne peut contenir que des lettres et des tirets. "
                  "Veuillez réessayer.\033[0m")

    while True:
        lastname = input("Entrez le nom de famille du joueur: ").title()
        if lastname.replace(' ', '').isalpha():
            break
        else:
            print("\033[91mLe nom de famille ne peut contenir "
                  "que des lettres et des espaces. Veuillez réessayer.\033[0m")

    while True:
        birth = input("Entrez la date de naissance du joueur (format: DD-MM-YYYY): ")
        if validate_date_format(birth):
            break
        else:
            print("\033[91mFormat de date invalide. "
                  "Veuillez utiliser le format 'DD-MM-YYYY'. Veuillez réessayer.\033[0m")

    while True:
        national_chess_id = input("Entrez l'identifiant national du joueur (format: AB12345): ").upper()
        if validate_national_chess_id_format(national_chess_id):
            break
        else:
            print("\033[91mFormat d'identifiant national invalide. "
                  "Veuillez utiliser le format 'AB12345'.\033[0m")

    return firstname, lastname, birth, national_chess_id


class PlayerView:
    def __init__(self, player_repository):
        self.player_repository = player_repository

    def show_players(self):
        self.player_repository.load_players()
        self.player_repository.display_players_by_index()
