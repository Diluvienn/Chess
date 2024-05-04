def find_player(tournament, player_firstname, player_lastname):
    """Find a player in a tournament by first and last name.

    Args:
        tournament: The tournament object.
        player_firstname (str): The first name of the player.
        player_lastname (str): The last name of the player.

    Returns:
        Player: The Player object if found, None otherwise.
    """
    for p in tournament.players_list:
        if p.firstname == player_firstname and p.lastname == player_lastname:
            return p
    return None


if __name__ == "__main__":
    pass
