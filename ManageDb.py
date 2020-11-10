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
                            category_id int DEFAULT NULL,
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
                            id_store int DEFAULT NULL,
                            id_product int DEFAULT NULL)
                            ENGINE=InnoDB;
                            
                        CREATE TABLE product_brand (
                            id_brand int DEFAULT NULL,
                            id_product int DEFAULT NULL)
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
        x = "*"

        cls.cursor.execute(f"SELECT {what_to_select} FROM {name_of_table}")

        for lines in cls.cursor: # affiche les tuples les uns sous les autres
            print(lines)

        """rows = cls.cursor.fetchall()# affiche les tuples les uns après les autres
                print(rows) moins lisible je trouve"""

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
    def insert_n_n_test(cls):
        """
            Insertion des données dans la base (n-n)
        """

        for product in Product.Product.instantiated_products:
            print(product.name, product.url, product.picture_url, product.nutriscore)

            cls.cursor.execute(f"INSERT INTO product (name, url, picture_url, nutriscore) VALUES ({product.name}, {product.url}, {product.picture_url}, {product.nutriscore})")
            print(f"insertion de {product.name} dans la table product")

            MyProductID = cls.cursor.execute(f"SELECT id FROM product WHERE product.name = {product.name}")

            for store in product.store:
                cls.cursor.execute(f"INSERT INTO store (name) VALUES ({store},)")
                print(f"insertion de {store} dans la table store")

            MyStoreID = cls.cursor.execute(f"SELECT id FROM store WHERE store.name = {store.name}")

            cls.cursor.execute(f"INSERT INTO product_store (id_product, id_store) VALUES ({MyProductID}, {MyStoreID})")

            # il faut garder les deux variables et les utiliser pour remplir les tables product_store et product_brand
