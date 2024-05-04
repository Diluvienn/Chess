def confirm_return_to_previous_menu():
    """Confirm returning to the previous menu without saving.

    Returns:
        bool: True if the user confirms to return
        to the previous menu without saving,
        False otherwise.

    This function prompts the user to confirm
    whether they want to return to the previous menu
    without saving any changes.
    It handles user input validation.
    """
    confirmation = input("Voulez-vous vraiment "
                         "retourner au menu précédent "
                         "sans sauvegarder ? (y/n): ")
    if confirmation.lower() == 'y':
        print("Retour au menu précédent.")
        return True
    else:
        return False


def confirm_return_to_main_menu():
    """Confirm returning to the main menu without saving.

    Returns:
        bool: True if the user confirms to return
        to the main menu without saving,
        False otherwise.

    This function prompts the user to confirm
    whether they want to return to the main menu
    without saving any changes.
    It handles user input validation.
    """
    confirmation = input("Voulez-vous vraiment "
                         "retourner au menu principal "
                         "sans sauvegarder ? (y/n): ")
    if confirmation.lower() == 'y':
        print("Retour au menu principal sans sauvegarde.")
        return True
    else:
        return False


def confirm_stop_add_note():
    """Confirm stopping the addition of notes without saving.

    Returns:
        bool: True if the user confirms to stop adding notes without saving,
        False otherwise.

    This function prompts the user to confirm whether
    they want to stop adding notes
    without saving any changes.
    It handles user input validation.
    """
    confirmation = input("Voulez-vous vraiment abandonner les notes "
                         "sans les sauvegarder ? (y/n): ")
    if confirmation.lower() == 'y':
        print("Retour à la création du tournoi.")
        return True
    else:
        return False


if __name__ == "__main__":
    pass
