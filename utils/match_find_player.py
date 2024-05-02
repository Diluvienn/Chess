
def find_player(tournament, player_firstname, player_lastname):
    for p in tournament.players_list:
        if p.firstname == player_firstname and p.lastname == player_lastname:
            return p
    return None