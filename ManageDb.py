# -*-coding:UTF-8-*

import mysql.connector
from PrepareData import PrepareData


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
                            nutriscore varchar(20) DEFAULT NULL,
                            description text DEFAULT NULL,
                            brand varchar (50) DEFAULT NULL,
                            stores text DEFAULT NULL,
                            category_id smallint DEFAULT NULL,
                            PRIMARY KEY(id))
                            ENGINE=InnoDB;

                        CREATE TABLE store (
                            id int NOT NULL AUTO_INCREMENT,
                            name varchar(200) DEFAULT NULL,
                            url varchar(300) DEFAULT NULL,
                            PRIMARY KEY(id))
                            ENGINE=InnoDB;

                        CREATE TABLE brand (
                            id int NOT NULL AUTO_INCREMENT,
                            name varchar(200) DEFAULT NULL,
                            url varchar(300) DEFAULT NULL,
                            PRIMARY KEY(id))
                            ENGINE=InnoDB;"""

        for result in cls.cursor.execute(DATA_BASE_SQL, multi=True):
            pass

        cls.connexion.commit()
        """cls.cursor.close()  # toutes ces instructions plantent !
        cls.connexion.close()"""

        print("La base de données à été crée.")

    @classmethod
    def delete(cls):
        """
            delete database, table, line or column
        """

    @classmethod
    def show_tables(cls):
        """
        update the database data...

        """

        cls.cursor.execute("show tables")

        for x in cls.cursor:
            print(x)

    @classmethod
    def select(cls):
        """
            select function in SQL
        """
        x = "*"
        print(cls.cursor.execute(f"select {x} from category")) # ne marche pas


    @classmethod
    def fill(cls):
        """
            fill the database with the transformed API data
        """

        SQL = "INSERT INTO category (name, url) VALUES (%s, %s)"

        for i in PrepareData.instantiated_categories:
            print(f'insertion de {i.name} dans la base de données')
            cls.cursor.execute(SQL, (i.name, i.url))
        cls.connexion.commit()

        # tout bon ca focntionne il faut remplir les produits maintenat et voir comment gérér les brands et les stores avec clé etrangères et containtes