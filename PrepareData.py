# -*-coding:UTF-8-*

import json
import requests
from DbClasses import Category, Product, Brand


class PrepareData:

    instantiated_categories = []
    cleaned_categories = []

    all_products = []
    instantiated_products = []

    instantiated_brands = []



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

        for key in result:
            if key == "count":
                print(f'Récupération terminée. {result["count"]} catégories récupérées.\n')

        for categories in result["tags"]:
            if min_product <= categories["products"] <= max_product:
                print(f'Récupération de la catégorie {categories["name"]}')
                cls.cleaned_categories.append((categories["name"], categories["url"]))

        print(f'\n{len(cls.cleaned_categories)} catégories ont été récupérées après triage')

    @classmethod
    def instantiate_categories(cls):
        """
            instantiate the categories into the class Category
        """

        for data in cls.cleaned_categories:
            # create object instance
            my_data = Category(
                data[0],
                data[1])
            cls.instantiated_categories.append(my_data)

    @classmethod
    def get_and_clean_products(cls):
        """
            get the products by the API and clean the obtained data
        """

        position_in_cat_list = 0    # counter to change the url in the instantiated_categories
        page_nbr = 1    # counter to go forward in the pages of the products
        del_el = 0    # elements ignored because of a missing key corresponding to a needed data
        x = 0    # counter to display the final number of products contained in each categorie

        for cat in cls.instantiated_categories:
            temp_prod = []  # temporary list of product for the current category

            https = cls.instantiated_categories[position_in_cat_list].url

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

            cls.all_products.append(temp_prod)
            position_in_cat_list += 1

        print(f'\n{del_el} produits ont été ignorés car une clé était manquante\n')

        for i in cls.all_products:

            print(f'{len(i)} produits ont été récupérés dans la catégorie {cls.instantiated_categories[x].name}')
            x += 1

    @classmethod
    def instantiate_products(cls):
        empty_slot = 0

        for my_list in cls.all_products:
            for my_product in my_list:
                # instantiate only the products that contains all the needed data
                """for elem in range(len(my_product)):
                    if my_product[elem] == "":"""
                if my_product[0] == "" or my_product[1] == "" or my_product[2] == "" or my_product[3] == "" or \
                        my_product[4] == "" or my_product[5] == "":
                    empty_slot += 1
                    pass
                else:
                    # create object instance

                    my_data = Product(
                        my_product[0],
                        my_product[1],
                        my_product[2],
                        my_product[3],
                        my_product[4],
                        my_product[5])

                    cls.instantiated_products.append(my_data)
        print(f"\n{empty_slot} produits ont été ignorés car certaines données étaient manquantes\n")



    @classmethod
    def get_and_clean_brands_and_stores(cls):

        """
             get and sort the brands and the stores, eliminating multiple occurencies and similar names
        """
        # cette methode doit pouvoir s'appliquer aussi aux stores (juste a remplacer le .brand par .store dans le split mais n'y arrive pas)
        # essayé en remplcant cls.instaiated product par un génrique et en mettant instatiated product.brand en argument de l'application mais ne ocntionne pas car ne cible par l'argument mais la liste d'objet
        # autre piste: mettre lower et strip sur tout les elements avant d'instancier.

        temp_brand_list = []
        split_brand1 = ""
        split_brand2 = ""
        lowercase_brands = []
        stripped_brands = []
        cleaned_brands = []

        for brand in cls.instantiated_products:
            # break tuples of brands and put them in a unique list of brands
            print(brand.name, brand.store)
            try:
                split_brand1, split_brand2 = brand.brand.split(",")
            except ValueError:
                pass
                temp_brand_list.append(split_brand1)
                temp_brand_list.append(split_brand2)

        for brand in temp_brand_list:
            # eliminate empty brands and makes all lowercase
            if brand != "":
                lowercase_brands.append(brand.lower())

        for brand in lowercase_brands:
            # strip all brands of leading and trailing withe space
            stripped_brands.append(brand.strip())

        for brand in stripped_brands:
            # replace . with no withe space
            cleaned_brands.append(brand.replace(".", ""))

        # eliminate similar names
        sorted_brands = list(set(cleaned_brands))

        print(sorted_brands)

        MY_PRODUCTS_BRANDS = [brand.name for brand in cls.instantiated_products]

        print(MY_PRODUCTS_BRANDS)

        # instantiate the brands
        for brand in sorted_brands:
            my_brand = Brand(brand[0])
            cls.instantiated_brands.append(my_brand)






