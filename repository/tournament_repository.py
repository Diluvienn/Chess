import os
import json

from unidecode import unidecode

from model.tournament import Tournament
from utils.confirm_return_menu import confirm_return_to_main_menu


class TournamentRepository:
    """Repository for managing tournament data storage and retrieval."""

    def __init__(self, filename='tournament.json'):
        """Initialize the TournamentRepository.

        Args:
            filename (str, optional):
            Name of the JSON file to store tournament data.
            Defaults to 'tournament.json'.
        """
        data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
        self.filename = os.path.join(data_dir, filename)

    def load_tournaments(self):
        """Load tournaments from the JSON file.

       Returns:
           List[dict]: A list of dictionaries containing
           tournament information loaded from the JSON file.
           If the file does not exist, an empty list is returned.
       """
        if not os.path.exists(self.filename):
            return []

        with open(self.filename, 'r') as file:
            tournaments = json.load(file)
        return tournaments

    def get_tournaments_by_alphabetical_order(self):
        """Get tournaments from the repository sorted alphabetically by name.

        Returns:
            List[str]: A list of tournament names sorted alphabetically.

        Note:
            This method retrieves tournament data from the repository,
            sorts the tournaments alphabetically
            by name, and returns a list of tournament names.
        """
        tournaments = self.load_tournaments()
        sorted_tournaments = sorted(tournaments, key=lambda x: x['name'])
        formatted_output = []
        for tournament_data in sorted_tournaments:
            tournament = Tournament(**tournament_data)
            formatted_output.append(tournament)

        return formatted_output

    def add_tournament(self, tournament):
        """Add a tournament to the repository.

        Args:
            tournament (Tournament):
            The tournament object to be added to the repository.

        """
        tournaments = self.load_tournaments()
        tournament_data = tournament.to_json()

        # Convertir les joueurs en JSON
        players_json = []
        for player in tournament.players_list:
            player_json = player.to_json()
            players_json.append(player_json)
        tournament_data["players_list"] = players_json

        # Convertir les paires jouées en JSON
        played_pairs_json = []
        for pair in tournament.played_pairs:
            player1_json = pair[0].to_json()
            player2_json = pair[1].to_json()
            played_pair_json = {"player1": player1_json,
                                "player2": player2_json}
            played_pairs_json.append(played_pair_json)
        tournament_data["played_pairs"] = played_pairs_json

        # Convertir les rounds en JSON
        rounds_json = []
        for round in tournament.rounds:
            round_json = round.to_json()
            rounds_json.append(round_json)
        tournament_data["rounds"] = rounds_json

        # Recherche le tournoi existant
        # et met à jour ses données s'il existe déjà
        for i, existing_tournament in enumerate(tournaments):
            if existing_tournament["name"] == tournament.name:
                tournaments[i] = tournament_data
                break
        else:
            tournaments.append(tournament_data)

        with open(self.filename, 'w') as file:
            json.dump(tournaments, file, indent=4)

    def find_unfinished_tournaments(self):
        """Find tournaments that are not yet finished.

        Returns:
            List[dict]: A list of dictionaries containing information about
            tournaments that are not yet finished.

        This method retrieves all tournaments from the repository,
        identifies the ones that have not reached their final round,
        and returns their details.
        """
        tournaments = self.load_tournaments()
        unfinished_tournaments = []

        for tournament in tournaments:
            round_count = len(tournament["rounds"])
            round_count = int(round_count)
            if (tournament["current_round"] < round_count and
                    (tournament["current_round"] != 0
                     or len(tournament["players_list"]) > 0)):
                unfinished_tournaments.append(tournament)
        return unfinished_tournaments

    def resume_tournament(self):
        """Resume a tournament that is not yet finished.

        Returns:
            dict or None: Details of the chosen tournament to resume,
            or None if no unfinished tournament is found.

        This method allows the user to choose a tournament from the list
        of unfinished tournaments to resume. It prompts the user to select
        a tournament by number,
        provides options for returning to the main menu,
        and handles input validation.
        """
        unfinished_tournaments = self.find_unfinished_tournaments()
        if not unfinished_tournaments:
            print("Aucun tournoi non terminé trouvé.")
            return
        print("\nTournois non terminés :")
        for idx, tournament in enumerate(unfinished_tournaments, 1):
            print(f"{idx}. {tournament['name']} à {tournament['place']}")
        print("\n\033[92mRetour au menu principal: 'q'\033[0m")
        while True:
            choice = input("Choisissez le numéro du tournoi à reprendre : ")
            if choice == "q":
                if confirm_return_to_main_menu():
                    return None
                else:
                    continue
            else:
                try:
                    choice = int(choice)
                    if 1 <= choice <= len(unfinished_tournaments):
                        chosen_tournament = unfinished_tournaments[choice - 1]
                        print(f"\nVous avez choisi de reprendre "
                              f"le tournoi {chosen_tournament['name']} "
                              f"à {chosen_tournament['place']}")
                        return chosen_tournament
                    else:
                        print("\033[91mIndex invalide. "
                              "Veuillez choisir un numéro entre 1 et",
                              len(unfinished_tournaments),
                              "\033[0m")
                except ValueError:
                    print("\033[91mVeuillez entrer un numéro valide.\033[0m")

    def find_unstarted_tournaments(self):
        """Find tournaments that have not yet started.

        Returns:
            List[dict]: A list of dictionaries containing information about
            tournaments that have not yet started.

        This method retrieves all tournaments from the repository
        and identifies the ones that have not started yet.
        """
        tournaments = self.load_tournaments()
        unstarted_tournaments = []

        for tournament in tournaments:
            if tournament["current_round"] == 0:
                unstarted_tournaments.append(tournament)
        return unstarted_tournaments

    def get_tournament_details(self, tournament_name):
        """Get details of a specific tournament.

        Args:
            tournament_name (str):
            The name of the tournament to retrieve details for.

        Returns:
            dict or None: Details of the requested tournament,
            or None if the tournament is not found.

        This method searches for a tournament by name in the repository
        and returns its details, including name, place, start and end dates,
        director's note, current round, player scores, and rounds details.
        If the tournament is not found, it returns None.
        """
        for tournament_data in self.load_tournaments():
            tournament_name_normalized = (
                unidecode(tournament_data['name'].title()))
            if (tournament_name_normalized ==
                    unidecode(tournament_name.title())):
                tournament_details = {
                    "name": tournament_data["name"],
                    "place": tournament_data["place"],
                    "date_start": tournament_data["date_start"],
                    "date_end": tournament_data["date_end"],
                    "director_note": tournament_data["director_note"],
                    "players_score": tournament_data['players_score'],
                    "rounds": tournament_data['rounds'],
                    "players_list": tournament_data['players_list']
                }
                current_round = tournament_data['current_round']
                rounds_count = len(tournament_data['rounds'])
                if current_round == rounds_count:
                    tournament_details["tournament_status"] = \
                        " Tournoi terminé"
                else:
                    tournament_details["tournament_status"] = \
                        f"Round actuel : {current_round} sur {rounds_count}"

                # stocker les détails des rounds joués
                played_rounds_details = []

                # Ajout des détails des rounds joués
                for idx, round_data in enumerate(tournament_data['rounds']):
                    round_details = {
                        "name": round_data['name'],
                        "start_time": round_data.get('start_time', None),
                        "end_time": round_data.get('end_time', None),
                        "matches": round_data.get('matches', [])
                    }
                    played_rounds_details.append(round_details)

                tournament_details["played_rounds"] = played_rounds_details
                return tournament_details
        return None


if __name__ == "__main__":
    pass
