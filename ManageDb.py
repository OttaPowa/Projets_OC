# -*-coding:UTF-8-*

import mysql.connector
from PrepareData import PrepareData
from constants import*


class ManageDb:
    """
        This class manage the interactions with the database
    """

    connexion = mysql.connector.connect(user="root", password="Donn1eDark0", database="projet5")
    cursor = connexion.cursor()


    SQL_CAT_INSERT = """INSERT INTO category (name,url) VALUES (%(name)s, %(url)s)"""

    @classmethod
    def verify_prerequisite(cls):
        """
            verify if MySQL is installed on the client computer. if not print a message with à link to DL it.
        """

    @classmethod
    def build(cls):
        """
            build the MySQL database
        """
        print("Contruction de la base de données...")

        DATA_BASE_SQL = """
                        DROP TABLE IF EXISTS category;
                        DROP TABLE IF EXISTS product;
                        DROP TABLE IF EXISTS store;
                        DROP TABLE IF EXISTS brand;
                        DROP TABLE IF EXISTS product_store;
                        DROP TABLE IF EXISTS product_brand;
                        DROP TABLE IF EXISTS product_category;
                        
                        CREATE TABLE category(
                            id int NOT NULL AUTO_INCREMENT,
                            name varchar(200) DEFAULT NULL,
                            url varchar(300) DEFAULT NULL,
                            PRIMARY KEY(id))ENGINE=InnoDB;

                        CREATE TABLE product (
                            id int NOT NULL AUTO_INCREMENT,
                            name varchar(200) DEFAULT NULL,
                            url varchar(300) DEFAULT NULL,
                            picture_url varchar(300) DEFAULT NULL,
                            nutriscore varchar(5) DEFAULT NULL,
                            PRIMARY KEY(id))
                            ENGINE=InnoDB;

                        CREATE TABLE store (
                            id int NOT NULL AUTO_INCREMENT,
                            name varchar(200) DEFAULT NULL,
                            PRIMARY KEY(id))
                            ENGINE=InnoDB;

                        CREATE TABLE brand (
                            id int NOT NULL AUTO_INCREMENT,
                            name varchar(200) DEFAULT NULL,
                            PRIMARY KEY(id))
                            ENGINE=InnoDB;
                            
                        CREATE TABLE product_store (
                            id_product int DEFAULT NULL,
                            id_store int DEFAULT NULL)
                            ENGINE=InnoDB;
                            
                        CREATE TABLE product_brand (
                            id_product int DEFAULT NULL,
                            id_brand int DEFAULT NULL)
                            ENGINE=InnoDB;
                            
                        CREATE TABLE product_category (
                            id_product int DEFAULT NULL,
                            id_category int DEFAULT NULL)
                            ENGINE=InnoDB; 
                        """

        for result in cls.cursor.execute(DATA_BASE_SQL, multi=True):
            pass

        cls.connexion.commit()
        print("La base de données à été crée.")

    @classmethod
    def delete(cls, name_of_table):
        """
            delete database, table, line or column
        """
        cls.cursor.execute(f"DROP TABLE {name_of_table}")

    @classmethod
    def show_tables(cls):
        """
        update the database data...

        """
        cls.cursor.execute("SHOW TABLES")
        for lines in cls.cursor:
            print(lines)

    @classmethod
    def select(cls, what_to_select, name_of_table):
        """
            select function in SQL
        """

        cls.cursor.execute(f"SELECT {what_to_select} FROM {name_of_table}")

        for lines in cls.cursor:  # affiche les tuples les uns sous les autres
            print(lines)

        """rows = cls.cursor.fetchall()# affiche les tuples les uns après les autres
                print(rows) moins lisible je trouve , de plus fetchall renvoie une liste 
                de tuple alors que cette methode seulemnt un tuple"""

    @classmethod
    def fill(cls, insert_statement, list_of_items):
        """
            fill the database with the transformed API data
        """

        for item in list_of_items:
            try:
                cls.cursor.execute(insert_statement, (item.name, item.url, item.picture_url, item.nutriscore))
            except AttributeError:
                try:
                    cls.cursor.execute(insert_statement, (item.name, item.url))

                except AttributeError:
                    cls.cursor.execute(insert_statement, (item.name,))

        cls.connexion.commit()

    @classmethod
    def insert_n_n_test(cls, instantiated_list, name_of_table1, name_of_table2, name_of_table3, column1, column2):
        """
            Insertion des données dans la base (n-n)
        """

        for product in instantiated_list:
            my_product_id = tuple
            my_store_id = tuple

            query_product_id = f'SELECT id FROM {name_of_table1} WHERE name = "{product.name}"'
            print(query_product_id)
            cls.cursor.execute(query_product_id)
            for row in cls.cursor:
                my_product_id = row
                print(my_product_id)

            list_of_splited_items = []

            if name_of_table2 == 'store':
                list_of_splited_stores = product.store.split(",")
                list_of_splited_items = list_of_splited_stores
            if name_of_table2 == 'brand':
                list_of_splited_brands = product.brand.split(",")
                list_of_splited_items = list_of_splited_brands
            if name_of_table2 == 'category':
                list_of_splited_categories = product.category.split(",")
                list_of_splited_items = list_of_splited_categories

            """temp_all = []
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

            """
            # GROS PROBLEME CETTE METHODE LIMTE A DEUX CAT OU DEUX BARND OU DEUX STORE !! utiliser len ou range(len) comme en test
            first_store = []
            second_store = []

            try:
                second_store = list_of_splited_items[1].strip()
                first_store = list_of_splited_items[0].strip()
            except IndexError:
                first_store = list_of_splited_items[0].strip()

            query_store_id1 = f'SELECT id FROM {name_of_table2} WHERE name = "{first_store}"'
            print(query_store_id1)
            cls.cursor.execute(query_store_id1)

            for line in cls.cursor:  # this method get a tuple instead of a list of tuples with fetch.
                my_store_id = line
                print(my_store_id)

            if second_store != []:
                query_store_id2 = f'SELECT id FROM {name_of_table2} WHERE name = "{second_store}"'
                print(query_store_id2)
                cls.cursor.execute(query_store_id2)
                for line in cls.cursor:  # this method get a tuple instead of a list of tuples with fetch.
                    my_store_id1 = line
                    print(my_store_id1)

            query_insert = f"INSERT INTO {name_of_table3} ({column1}, {column2}) VALUES (%s, %s)"
            cls.cursor.execute(query_insert, (my_product_id[0], my_store_id[0]))
            # the result of the select is a lone tuples, so i select just the data not the tuple.





