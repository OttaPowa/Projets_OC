# -*-coding:UTF-8-*
import mysql.connector
import requests
import json
from DbClasses import Category


class ManageDb:
    """
        This class manage the interactions with the database
    """
    RAW_CAT_DATA = {}
    CLEANED_CAT_DATA = []
    FINAL_CAT_DATA = []

    connexion = mysql.connector.connect(host="localhost", user="root", password="Donn1eDark0", database="projet5")
    cursor = connexion.cursor()
    SQL_CAT_INSERT = """INSERT INTO category (name,url) VALUES (%(name)s, %(url)s)"""


    def verify_prerequisite():
        """
            verify if MySQL is installed on the client computer. if not print a message with à link to DL it.
        """

    @classmethod
    def connect(cls):
        """
            connect to the MySQL database
        """

    @classmethod
    def build(cls):
        """
            build the MySQL database
        """

        cls.cursor.execute("""
        CREATE TABLE IF NOT EXISTS category (
            id smallint NOT NULL AUTO_INCREMENT,
            name varchar(50) DEFAULT NULL,
            url varchar(300) DEFAULT NULL,
            PRIMARY KEY(id))
            ENGINE=InnoDB;
        CREATE TABLE IF NOT EXISTS product (
            id smallint NOT NULL AUTO_INCREMENT,
            name varchar(50) DEFAULT NULL,
            url varchar(300) DEFAULT NULL,
            picture_url varchar(300) DEFAULT NULL,
            nutriscore varchar(20) DEFAULT NULL,
            description text DEFAULT NULL,
            brand varchar (50) DEFAULT NULL,
            stores text DEFAULT NULL,
            category_id smallint DEFAULT NULL,
            PRIMARY KEY(id))
            ENGINE=InnoDB;
        CREATE TABLE IF NOT EXISTS store (
            id smallint NOT NULL AUTO_INCREMENT,
            name varchar(50) DEFAULT NULL,
            url varchar(300) DEFAULT NULL,
            PRIMARY KEY(id))
            ENGINE=InnoDB;
        CREATE TABLE IF NOT EXISTS brand (
            id smallint NOT NULL AUTO_INCREMENT,
            name varchar(50) DEFAULT NULL,
            url varchar(300) DEFAULT NULL,
            PRIMARY KEY(id))
            ENGINE=InnoDB;
        CREATE TABLE IF NOT EXISTS user_saves (
            id_product 1 smallint DEFAULT NULL,
            nutriscore 1 varchar(20) DEFAULT NULL,
            id_product 2 smallint DEFAULT NULL,
            nutriscore 2 varchar(20) DEFAULT NULL)
            ENGINE=InnoDB;
                    
        """, multi=True)

    @staticmethod
    def get_data():
        """
            get the data by the API
        """
        request = requests.get("https://fr.openfoodfacts.org/categories.json")
        result = request.json()

        with open("data.json", "w") as data:
            json.dump(result, data, indent=4)

    @classmethod
    def transform(cls):
        """
            transform the JSON data into Python dictionary
        """
        with open("data.json") as json_data:
            data_dict = json.load(json_data)
            cls.RAW_CAT_DATA = data_dict

    @classmethod
    def fill(cls):
        """
            fill the database with the transformed API data
        """

        for current_cat in cls.FINAL_CAT_DATA:
            if current_cat.keys() == "name":
                cat_instance = Category(current_cat.values()[0])
            if current_cat.keys() == "url":
                cat_instance = Category(current_cat.values()[1])

            print(cat_instance.name)

        """sort_cat_list = []

               for current_cat in cls.FINAL_CAT_DATA:
                   new = sorted(current_cat.items(), key=lambda t: t[0])
                   sort_cat_list.append(new)*"""

        """my_cat = Category(current_cat[0],
                          current_cat[1])

    print(sort_cat_list.name)"""


    @classmethod
    def delete(cls):
        """
            delete database, table, line or column
        """

    def update():
        """
        update the database data...
        for now it serves as a request test
        """

    @classmethod
    def clean_data(cls):
        """
        clean the raw categories data by keeping only categories which contains between 50 and 1000 products
        """

        del cls.RAW_CAT_DATA["count"]

        for my_list in cls.RAW_CAT_DATA.values():
            for my_dict in my_list:
                for my_item in my_dict.items():
                    if (my_item[0] == 'products' and my_item[1] > 50) and (my_item[0] == 'products' and my_item[1] < 1000):
                        cls.CLEANED_CAT_DATA.append(my_dict)
                    else:
                        pass

        keys_name = ["name", "url", "products", "sameAs", "known", "id"]

        for y in range(len(cls.CLEANED_CAT_DATA)):

            del cls.CLEANED_CAT_DATA[y][keys_name[2]]
            del cls.CLEANED_CAT_DATA[y][keys_name[4]]
            del cls.CLEANED_CAT_DATA[y][keys_name[5]]

            try:
                cls.CLEANED_CAT_DATA[y][keys_name[3]]
                del cls.CLEANED_CAT_DATA[y][keys_name[3]]
            except KeyError:
                pass

            cls.FINAL_CAT_DATA.append(cls.CLEANED_CAT_DATA[y])

