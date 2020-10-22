# -*-coding:UTF-8-*

import json
import requests
from DbClasses import Category, Product, Brand, Store
from constants import*


class PrepareData:
    cleaned_categories = []
    cleaned_products = []

    sorted_items = []

    @classmethod
    def get_categories(cls):
        """
            get the data by the API
        """

        min_product = 200
        max_product = 210

        print("\nRécupération des catégories via l'API Open Food Fact...\n")

        request = requests.get("https://fr.openfoodfacts.org/categories.json")
        result = request.json()

        for key in result:
            if key == "count":
                print(f'Récupération terminée. {result["count"]} catégories récupérées.\n')

        for categories in result["tags"]:
            if min_product <= categories["products"] <= max_product:
                print(f'Récupération de la catégorie {categories["name"]}')
                cls.cleaned_categories.append((categories["name"], categories["url"]))

        print(f'\n{len(cls.cleaned_categories)} catégories ont été récupérées après triage')

    @classmethod
    def get_and_sort_products(cls):
        """
            get the products by the API and clean the obtained data
        """

        position_in_cat_list = 0    # counter to change the url in the instantiated_categories
        page_nbr = 1    # counter to go forward in the pages of the products
        del_el = 0    # elements ignored because of a missing key corresponding to a needed data
        x = 0    # counter to display the final number of products contained in each categorie
        uncleaned_products = []
        empty_slot = 0

        for cat in DbClasses.Category.instantiated_categories:
            temp_prod = []  # temporary list of product for the current category
            https = DbClasses.Category.instantiated_categories[position_in_cat_list].url
            request = requests.get(f'{https}.json/{page_nbr}')
            result = request.json()

            if len(result["products"]) > 0:
                page_nbr += 1

                for prod in result["products"]:
                    try:
                        temp_prod.append((prod["product_name_fr"], prod["url"], prod["image_url"], prod["brands"],
                                          prod["stores"], prod["nutrition_grades"]))
                    except KeyError:
                        del_el += 1
                        pass
            else:
                page_nbr = 1

            uncleaned_products.append(temp_prod)
            position_in_cat_list += 1

        print(f'\n{del_el} produits ont été ignorés car une clé était manquante\n')

        for i in uncleaned_products:
            print(f'{len(i)} produits ont été récupérés dans la catégorie {DbClasses.Category.instantiated_categories[x].name}')
            x += 1

        for my_list in uncleaned_products:
            for my_product in my_list:
                # instantiate only the products that contains all the needed data
                if my_product[0] == "" or my_product[1] == "" or my_product[2] == "" or my_product[3] == "" or \
                        my_product[4] == "" or my_product[5] == "":
                    empty_slot += 1
                    pass
                else:
                    cls.cleaned_products.append(my_product)

        print(f"\n{empty_slot} produits ont été ignorés car certaines données étaient manquantes\n")

    @classmethod
    def calibrate(cls, list_of_data):

        """
             get and sort the brands and the stores, eliminating multiple occurencies and similar names
        """
        lowercase_items = []
        stripped_items = []
        cleaned_items = []

        print(list_of_data)
        # REVOIR LA MANIERE / CELA FAIT UNE LISTE ET NON UNE LISTE DE TUPLES VOIR COMMENT GERER LE LOWER OU REFORMER LES TUPLES APRES TRAITEMENT
        for tupl in list_of_data:
            for item in tupl:
                lowercase_items.append(item.lower())

        for item in lowercase_items:
            # strip all items of leading and trailing withe space
            stripped_items.append(item.strip())

        list_of_data = stripped_items
        print(list_of_data)

    @classmethod
    def get_and_clean_additional_data(cls, items):

        """
             get and sort the brands and the stores, eliminating multiple occurencies and similar names
        """
        temp_item_list = []
        split_item1 = ""
        split_item2 = ""
        lowercase_items = []
        stripped_items = []
        cleaned_items = []

        """for item in items: UTILSE POUR BARND ET STORE
            # break tuples and put them in a unique list

            try:
                split_item1, split_item2 = item.split(",")
            except ValueError:
                pass
                temp_item_list.append(split_item1)
                temp_item_list.append(split_item2)"""


        for item in temp_item_list:
            # ignore empty items and lowercase it
            if item != "":
                lowercase_items.append(item.lower())

        for item in lowercase_items:
            # strip all items of leading and trailing withe space
            stripped_items.append(item.strip())

        for item in stripped_items:
            # replace "." with no white space
            cleaned_items.append(item.replace(".", ""))


        """"# eliminate similar names UTILSE POUR BARND ET STORE
        sorted_items = list(set(cleaned_items))
        cls.sorted_items = sorted_items"""
        """print(sorted_items)"""

    @classmethod
    def instantiate(cls, class_name, list_to_instantiate):

        for item in list_to_instantiate:
            my_item = class_name(item)
        print(list_to_instantiate)
        print(DbClasses.Category.instantiated_categories[3].name)










