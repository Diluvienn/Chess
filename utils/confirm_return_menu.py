def confirm_return_to_previous_menu():
    confirmation = input("Voulez-vous vraiment retourner au menu précédent sans sauvegarder ? (y/n): ")
    if confirmation.lower() == 'y':
        print("Retour au menu précédent.")
        return True
    else:
        return False


def confirm_return_to_main_menu():
    """Demande confirmation pour retourner au menu principal sans sauvegarder."""
    confirmation = input("Voulez-vous vraiment retourner au menu principal sans sauvegarder ? (y/n): ")
    if confirmation.lower() == 'y':
        print("Retour au menu principal sans sauvegarde.")
        return True
    else:
        return False


def confirm_stop_add_note():
    confirmation = input("Voulez-vous vraiment abandonner les notes sans les sauvegarder ? (y/n): ")
    if confirmation.lower() == 'y':
        print("Retour à la création du tournoi.")
        return True
    else:
        return False

