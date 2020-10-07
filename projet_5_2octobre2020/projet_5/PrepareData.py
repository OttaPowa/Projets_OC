# -*-coding:UTF-8-*

import json
import requests
from DbClasses import Category


class PrepareData:

    instantiated_categories = []
    cleaned_categories = []
    products = []

    @classmethod
    def get_and_clean_categories(cls):
        """
            get the data by the API
        """

        min_product = 150
        max_product = 200

        print("\nRécupération des catégories via l'API Open Food Fact...\n")

        request = requests.get("https://fr.openfoodfacts.org/categories.json")
        result = request.json()

        for keys in result:
            if keys == "count":
                print(f'Récupération terminée. {result["count"]} catégories récupérées\n')

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

        """for myurl in cls.instantiated_categories:
            print(myurl.name)
            if myurl.name == "Rillettes de sardine":
                print(myurl.url)"""
        x = 0
        for cat in cls.instantiated_categories:

            https = cls.instantiated_categories[x].url
            print(https)

            request = requests.get(f'{https}.json/{x}') # x est le numéro de page(pas sur de devoir le mettre ici
            result2 = request.json()
            print(f'les produits correspondant à la catégorie {cat.name} ont été récupérés')

            x += 1

            for prod in result2["products"]: #arg la je rentre dans la clé numéro de produit...ah non c'est bon !
                print(prod)
                #je rentre dans la liste des produits avec leur données stockés dans la page
                cls.products.append((prod["product_name_fr"], prod["url"], prod["image_url"], prod["brands"],
                                    prod["stores"], prod["generic_name_fr"], prod["nutrition_grades"]))




