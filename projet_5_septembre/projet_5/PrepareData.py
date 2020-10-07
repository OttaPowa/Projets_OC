# -*-coding:UTF-8-*

import json
import requests
from DbClasses import Category


class PrepareData:

    raw_cat_data = {}

    obj_cat = []

    @staticmethod
    def get_data():
        """
            get the data by the API
        """
        request = requests.get("https://fr.openfoodfacts.org/categories.json")
        result = request.json()

        with open("data.json", "w") as data:
            json.dump(result, data, indent=4)
            # write a file named data with indent for an easier read

    @classmethod
    def transform_data(cls):
        """
            transform the JSON data into Python dictionary
        """
        with open("data.json") as json_data:
            data_dict = json.load(json_data)
            cls.raw_cat_data = data_dict

    @classmethod
    def clean_and_instantiate_data(cls):
        """
        clean the raw categories data by keeping only categories which contains between 50 and 1000 products,
        then delete unnecessary data.
        instantiate the obtained data into class category object
        """
        cleaned_cat_data = []
        final_cat_data = []

        del cls.raw_cat_data["count"]
        # delete the key named count

        for my_list in cls.raw_cat_data.values():
            # keep only categories which contains between 50 and 1000 products
            for my_dict in my_list:
                for my_item in my_dict.items():
                    if (my_item[0] == 'products' and my_item[1] > 50) \
                            and (my_item[0] == 'products' and my_item[1] < 1000):

                        cleaned_cat_data.append(my_dict)
                    else:
                        pass

        keys_name = ["name", "url", "products", "sameAs", "known", "id"]

        for y in range(len(cleaned_cat_data)):
            # delete all unnecessary keys
            del cleaned_cat_data[y][keys_name[2]]
            del cleaned_cat_data[y][keys_name[4]]
            del cleaned_cat_data[y][keys_name[5]]

            try:
                cleaned_cat_data[y][keys_name[3]]
                del cleaned_cat_data[y][keys_name[3]]
            except KeyError:
                pass

            final_cat_data.append(cleaned_cat_data[y])

        # instantiate the categories
        list_of_name = []
        list_of_url = []

        for it in final_cat_data:
            for val in it.items():
                # create two lists which has name and url at the same location

                if val[0] == "name":
                    list_of_name.append(val[1])
                if val[0] == "url":
                    list_of_url.append(val[1])

        full_list = list(zip(list_of_name, list_of_url))
        # convert the two list into a single list of tuple

        # list of categories
        for x in full_list:
            # create object instance
            obj = Category(
                x[0],
                x[1])
            cls.obj_cat.append(obj)