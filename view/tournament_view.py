"""
This module defines functions and a class for managing user input
and displaying tournament information.
"""

from utils.formatvalidator import validate_date_format
from utils.confirm_return_menu import confirm_return_to_main_menu


def display_tournament_list(tournaments):
    """Display the list of tournaments."""
    formatted_output = tournaments

    print("\nListe des tournois:")
    for index, tournament in enumerate(formatted_output, 1):
        print(f"{index}. {tournament.name} à {tournament.place}")


def get_tournament_index_from_user(total_tournaments):
    """Ask the user to enter the index of the tournament."""
    print("\n\033[92mRetour au menu principal: 'q'\033[0m")
    while True:
        index_input = input("\nEntrez l'index du tournoi "
                            "dont vous souhaitez voir les détails: ")
        if index_input.isdigit():
            index = int(index_input)
            if 1 <= index <= total_tournaments:
                return index
            else:
                print(f"\033[91mL'index doit être compris entre 1 "
                      f"et {total_tournaments}.\033[0m")
        elif index_input == "q":
            break
        else:
            print("\033[91mL'index doit être un nombre entier.\033[0m")


def prompt_add_players():
    """Ask the user if they want to add players to the tournament."""
    while True:
        add_players_choice = (
            input("Souhaitez-vous ajouter des joueurs au tournoi ? (y/n) : "))
        if add_players_choice.lower() == "y":
            return True
        elif add_players_choice.lower() == "n":
            return False
        else:
            print("\033[91mVeuillez effectuer un choix valide.\033[0m")


def prompt_play_tournament():
    """Ask the user if they want to start the tournament."""
    while True:
        play_tournament_choice = (
            input("Souhaitez-vous lancer le tournoi ? (y/n) : "))
        if play_tournament_choice.lower() == "y":
            return True
        elif play_tournament_choice.lower() == "n":
            return False
        else:
            print("\033[91mVeuillez effectuer un choix valide\033[0m")


def get_user_choice():
    print("\033[92mRetour au menu principal sans sauvegarde: 'q'\033[0m")
    return input("Votre choix : ")


def display_add_player_menu(num_players):
    """Display the menu for adding players to the tournament."""
    if num_players >= 6 and num_players % 2 == 0:
        print("\nSouhaitez-vous ajouter un joueur existant (1), "
              "créer un nouveau joueur (2) "
              "ou arrêter l'ajout de joueur (3) ?: ")
    else:
        print("\nSouhaitez-vous ajouter un joueur existant (1) "
              "ou créer un nouveau joueur (2) ?: ")


def ask_to_play_next_round():
    """Ask the user if they want to play the next round."""
    play_next_round = input("Voulez-vous jouer le round suivant ? (y/n): ")
    while play_next_round not in ["y", "n"]:
        print("\033[91mVeuillez effectuer un choix valide.\033[0m")

        play_next_round = input("Voulez-vous jouer le round suivant ? (y/n): ")
    return play_next_round == "y"


class TournamentView:
    def __init__(self, tournament_controller):
        self.tournament_controller = tournament_controller

    @staticmethod
    def display_tournament_details(tournament_details):
        """Display the details of a tournament."""
        if tournament_details:
            print("\nDétails du tournoi:")
            print(f"Nom: {tournament_details['name']}")
            print(f"Lieu: {tournament_details['place']}")
            print(f"Date de début: {tournament_details['date_start']}")
            print(f"Date de fin: {tournament_details['date_end']}")
            print(f"Notes du directeur: {tournament_details['director_note']}")
            if not tournament_details['players_list']:
                print("Aucun joueur n'a encore été ajouté au tournoi.")
            if tournament_details['rounds'][0]['matches']:
                print(tournament_details['tournament_status'])
            for round_data in tournament_details['rounds']:
                matches = round_data['matches']
                if matches:
                    print(f"{round_data['name']}:")
                    print(f"  Début: {round_data['start_time']}")
                    print(f"  Fin: {round_data['end_time']}")
                    print("  Matches:")
                    for match in round_data['matches']:
                        player1, score1 = list(match['players'].items())[0]
                        player2, score2 = list(match['players'].items())[1]
                        print(f"    '{player1}' vs '{player2}'"
                              f": {score1}-{score2}")
                elif round_data == tournament_details['rounds'][0]:
                    print("Le tournoi n'a pas encore débuté.")
                    break
        else:
            print("Le tournoi spécifié n'existe pas ou n'a pas été trouvé.")

    @staticmethod
    def display_message(message):
        """Display a specific message."""
        print(message)

    def get_new_tournament_details(self):
        """Ask the user to enter details to create a new tournament."""
        name = None
        place = None
        date_start = None
        date_end = None
        director_note = None
        rounds = None

        while True:
            print("\n\033[92mRetour au menu principal "
                  "sans sauvegarde : 'q'\033[0m")
            print("\nCréation d'un nouveau tournoi:")
            choice = input("Nom du tournoi: ").title()

            if choice.lower() == 'q':
                if confirm_return_to_main_menu():
                    return None, None, None, None, None, None
                else:
                    continue

            name = choice
            if not name:
                print("\033[91mLe nom du tournoi ne peut pas être vide. "
                      "Veuillez entrer un nom de tournoi valide.\033[0m")
                continue
            else:
                break

        while True:
            choice = input("Lieu du tournoi: ").title()

            if choice.lower() == 'q':
                if confirm_return_to_main_menu():
                    return None, None, None, None, None, None
                else:
                    continue

            place = choice
            if not place:
                print("\033[91mLe lieu du tournoi ne peut pas être vide. "
                      "Veuillez entrer un lieu de tournoi valide.\033[0m")
                continue
            else:
                break

        # Demander au contrôleur d'ajouter des notes du directeur
        director_note = (
            self.tournament_controller.add_director_notes_to_tournament())
        if director_note is None:
            return None, None, None, None, None, None

        while True:
            date_start = input("Date de début (format DD-MM-YYYY): ")

            if date_start.lower() == 'q':
                if confirm_return_to_main_menu():
                    return None, None, None, None, None, None
                else:
                    continue

            if validate_date_format(date_start):
                break
            else:
                print("\033[91mFormat de date incorrect. "
                      "Veuillez saisir une date au format DD-MM-YYYY.\033[0m")

        while True:
            date_end = input("Date de fin (format DD-MM-YYYY): ")

            if date_end.lower() == 'q':
                if confirm_return_to_main_menu():
                    return None, None, None, None, None, None
                else:
                    continue

            if validate_date_format(date_end):
                break
            else:
                print("\033[91mFormat de date incorrect. "
                      "Veuillez saisir une date au format DD-MM-YYYY.\033[0m")

        while True:
            rounds_count = input(
                "Nombre de rounds (facultatif, par défaut 4): ")

            if rounds_count.lower() == 'q':
                if confirm_return_to_main_menu():
                    return None, None, None, None, None, None
                else:
                    continue

            rounds_count = int(rounds_count) if rounds_count else 4

            rounds = []
            for i in range(rounds_count):
                round_name = f"Round {i + 1}"
                round_details = {
                    "name": round_name,
                    "matches": [],
                    "start_time": None,
                    "end_time": None
                }
                rounds.append(round_details)

            return name, place, date_start, date_end, director_note, rounds

    def display_no_unstarted_tournaments_message(self):
        """Display a message indicating
        that no unstarted tournaments were found."""
        print("Aucun tournoi non débuté trouvé.")

    def display_unstarted_tournaments(self, unstarted_tournaments):
        """Display the list of unstarted tournaments."""
        print("\nTournois non débutés :")
        for idx, tournament in enumerate(unstarted_tournaments, 1):
            print(f"{idx}. {tournament['name']} à {tournament['place']}")

    def get_chosen_tournament(self, unstarted_tournaments):
        """Ask the user to choose a tournament."""
        print("\n\033[92mRetour au menu principal: 'q'\033[0m")
        while True:
            choice = (input("Choisissez le numéro du tournoi "
                            "dont vous souhaitez renseigner les joueurs : "))
            if choice == "q":
                if confirm_return_to_main_menu():
                    return None
                else:
                    continue
            else:
                try:
                    choice = int(choice)
                    if 1 <= choice <= len(unstarted_tournaments):
                        return unstarted_tournaments[choice - 1]
                    else:
                        print("\033[91mIndex invalide. "
                              "Veuillez choisir un numéro entre 1 et",
                              len(unstarted_tournaments), "\033[0m")
                except ValueError:
                    print("\033[91mVeuillez entrer un numéro valide.\033[0m")

    def display_chosen_tournament(self, chosen_tournament):
        """Display the tournament chosen by the user."""
        print(f"\nVous avez choisi le tournoi {chosen_tournament['name']} "
              f"à {chosen_tournament['place']}")


if __name__ == "__main__":
    pass
