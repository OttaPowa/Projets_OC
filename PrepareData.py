# -*-coding:UTF-8-*

import json
import requests
import Category
from constants import*


class PrepareData:
    cleaned_categories = []
    raw_products = []
    cleaned_products = []
    setted_items = []

    @classmethod
    def get_categories(cls):
        """
            get the data by the API
        """
        cleaned_categories = []
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
                cleaned_categories.append((categories["name"], categories["url"]))

        cls.cleaned_categories = cleaned_categories
        print(f'\n{len(cls.cleaned_categories)} catégories ont été récupérées après triage')

    @classmethod
    def get_and_sort_products(cls):
        """
            get the products by the API and clean the obtained data
        """

        position_in_cat_list = 0    # counter to change the url in the instantiated_categories
        page_nbr = 1    # counter to go forward in the pages of the products
        del_el = 0    # elements ignored because of a missing key corresponding to a needed data
        x = 0    # counter to display the final number of products contained in each category
        uncleaned_products = []
        empty_slot = 0

        for cat in Category.Category.instantiated_categories:
            temp_prod = []  # temporary list of product for the current category
            https = Category.Category.instantiated_categories[position_in_cat_list].url
            request = requests.get(f'{https}.json/{page_nbr}')
            result = request.json()

            if len(result["products"]) > 0:
                page_nbr += 1

                for prod in result["products"]:
                    try:
                        temp_prod.append((prod["product_name_fr"], prod["url"], prod["image_url"], prod["brands"],
                                          prod["stores"], prod["nutrition_grades"], prod["categories"]))
                    except KeyError:
                        del_el += 1
                        pass
            else:
                page_nbr = 1

            uncleaned_products.append(temp_prod)
            position_in_cat_list += 1

        print(f'\n{del_el} produits ont été ignorés car une clé était manquante\n')

        for i in uncleaned_products:
            print(f'{len(i)} produits ont été récupérés dans la catégorie {Category.Category.instantiated_categories[x].name}')
            x += 1

        for my_list in uncleaned_products:
            for my_product in my_list:
                # instantiate only the products that contains all the needed data
                if my_product[0] == "" or my_product[1] == "" or my_product[2] == "" or my_product[3] == "" or \
                        my_product[4] == "" or my_product[5] == "" or my_product[6] == "":
                    empty_slot += 1
                    pass
                else:
                    cls.raw_products.append(my_product)

        print(f"\n{empty_slot} produits ont été ignorés car certaines données étaient manquantes\n")


    @classmethod
    def calibrate(cls, list_of_data):
        """
             get and sort the brands and the stores, eliminating multiple occurencies and similar names
        """
        temp_list = []

        lowercase_items = [(arg1.lower(), arg2.lower(), arg3.lower(), arg4.lower(), arg5.lower(), arg6.lower(),
                            arg7.lower()) for arg1, arg2, arg3, arg4, arg5, arg6, arg7 in list_of_data]

        stripped_items = [(arg1.strip(), arg2.strip(), arg3.strip(), arg4.strip(), arg5.strip(), arg6.strip(),
                           arg7.strip()) for arg1, arg2, arg3, arg4, arg5, arg6, arg7 in lowercase_items]

        dot_replaced_items = [(arg1.replace(".", ""), arg2, arg3, arg4.replace(".", ""),
                               arg5.replace(".", ""), arg6.replace(".", ""), arg7.replace(".", ""))
                              for arg1, arg2, arg3, arg4, arg5, arg6, arg7 in stripped_items]

        slip_quotation_marks = [(arg1.replace("'", "''"), arg2, arg3, arg4.replace("'", "''"),
                                 arg5.replace("'", "''"), arg6.replace("'", "''"), arg7.replace("'", "''"))
                                for arg1, arg2, arg3, arg4, arg5, arg6, arg7 in dot_replaced_items]

        for i in slip_quotation_marks:
            if i != " ":
                temp_list.append(i)

        cls.cleaned_products = temp_list

    @classmethod
    def get_and_set(cls, items):
        temp_all = []
        final_temp = []
        cls.setted_items = []

        for item in items:
            list_of_splited_items = item.split(",")
            for f in range(len(list_of_splited_items)):
                for i in list_of_splited_items:
                    temp = i.split(",")
                    temp_all.append(temp)

        for i in temp_all:
            for x in i:
                final_temp.append(x.strip())
        ready = list(set(final_temp))

        for z in ready:
            cls.setted_items.append([z])
        print(cls.setted_items)






    @classmethod
    def get_stores_or_brands(cls, items):

        """
             get and sort the brands and the stores, eliminating multiple occurencies and similar names
        """
        temp_item_list = []
        split_item1 = ""
        split_item2 = ""
        split_item3 = ""
        split_item4 = ""
        cls.setted_items = []  # empty the list

        for item in items:
            # break tuples and put them in a unique list
            try:
                split_item1, split_item2, split_items3, split_items_4 = item.split(",")
            except ValueError:
                try:
                    split_item1, split_item2, split_item3 = item.split(",")
                except ValueError:
                    try:
                        split_item1, split_item2 = item.split(",")
                    except ValueError:
                        temp_item_list.append(item.strip())
                    temp_item_list.append(split_item1.strip())
                    temp_item_list.append(split_item2.strip())
                temp_item_list.append(split_item1.strip())
                temp_item_list.append(split_item2.strip())
                temp_item_list.append(split_item3.strip())
            temp_item_list.append(split_item1.strip())
            temp_item_list.append(split_item2.strip())
            temp_item_list.append(split_item3.strip())
            temp_item_list.append(split_item4.strip())

        # eliminate duplicated names
        setted_items = list(set(temp_item_list))
        del setted_items[0]  # delete the first item of the list (a blank "" generated by splitting tuples)

        for i in setted_items:
            # put each item in a list (the instantiation method need a list to work)
            cls.setted_items.append([i])

    @classmethod
    def instantiate(cls, class_name, list_to_instantiate):

        for item in list_to_instantiate:
            my_item = class_name(item)











