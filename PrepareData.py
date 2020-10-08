# -*-coding:UTF-8-*

import json
import requests
from DbClasses import Category


class PrepareData:

    instantiated_categories = []
    cleaned_categories = []

    all_products = []

    @classmethod
    def get_and_clean_categories(cls):
        """
            get the data by the API
        """

        min_product = 200
        max_product = 210

        print("\nRécupération des catégories via l'API Open Food Fact...\n")

        request = requests.get("https://fr.openfoodfacts.org/categories.json")
        result = request.json()

        for key in result:#optionnel non ne sert que pour le test ? peut aussi servir pour l'utilisateur
            if key == "count":
                print(f'Récupération terminée. {result["count"]} catégories récupérées.\n')

        for categories in result["tags"]:
            if min_product <= categories["products"] <= max_product:
                print(f'Récupération de la catégorie {categories["name"]}')
                cls.cleaned_categories.append((categories["name"], categories["url"]))

        print(f'\n{len(cls.cleaned_categories)} catégories ont été récupérées après triage')

    @classmethod
    def instantiate_categories(cls):

        for data in cls.cleaned_categories:
            # create object instance
            my_data = Category(
                data[0],
                data[1])
            cls.instantiated_categories.append(my_data)

    @classmethod
    def get_and_clean_products(cls):

        position_in_cat_list = 0
        page_nbr = 1
        del_el = 0

        for cat in cls.instantiated_categories:
            temp_prod = []

            https = cls.instantiated_categories[position_in_cat_list].url

            request = requests.get(f'{https}.json/{page_nbr}')
            result = request.json()

            if len(result["products"]) > 0:
                page_nbr += 1

                for prod in result["products"]:

                    try:
                        temp_prod.append((prod["product_name_fr"], prod["url"], prod["image_url"],
                                                     prod["brands"], prod["stores"], prod["generic_name_fr"],
                                                     prod["nutrition_grades"]))

                    except KeyError:
                        del_el += 1
                        pass

            else:
                page_nbr = 1

            cls.all_products.append(temp_prod)
            position_in_cat_list += 1

        print(len(cls.all_products))

        print(cls.all_products)


    # OK ca marche !! all catégory = liste de 27 listes correspondat aux tuples des produits (position cat.name = position all product)




