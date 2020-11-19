# -*-coding:UTF-8-*

from constants import*
from ManageDb import ManageDb


class Interactions:

    @staticmethod
    def authentication():

        user_name = input("Tapez votre nom d'utilisateur: ")
        password = input("Tapez votre mot de passe: ")

        if (user_name, password) == test:
            print("\nIdentification réussie\n")
        else:
            print("Echec de l'identification")
            return False

    @staticmethod
    def selection():
        stat = True
        while stat:
            try:
                cat_numbr = int(input("Tapez le numéro de la catégorie que vous souhaitez explorer:"))
                return cat_numbr
            except ValueError:
                print("entrez un nombre s'il vous plait!")
                continue

