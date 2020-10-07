# -*-coding:UTF-8-*

import mysql.connector
from PrepareData import PrepareData


class ManageDb:
    """
        This class manage the interactions with the database
    """

    connexion = mysql.connector.connect(host="localhost", user="root", password="Donn1eDark0", database="projet5")
    cursor = connexion.cursor()
    SQL_CAT_INSERT = """INSERT INTO category (name,url) VALUES (%(name)s, %(url)s)"""

    @classmethod
    def verify_prerequisite(cls):
        """
            verify if MySQL is installed on the client computer. if not print a message with à link to DL it.
        """

    @classmethod
    def connect(cls):
        """
            connect to the MySQL database
        """

    @classmethod
    def build_db(cls):
        """
            build the MySQL database
        """

        cls.cursor.execute("""
        DROP TABLE category;
        CREATE TABLE category (
            id smallint NOT NULL AUTO_INCREMENT,
            name varchar(200) DEFAULT NULL,
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

    @classmethod
    def delete(cls):
        """
            delete database, table, line or column
        """

    @classmethod
    def update(cls):
        """
        update the database data...

        """
        cls.cursor.execute('INSERT INTO category(name,url) VALUES(' + i.name + ',' + i.url + ');')

        cls.cursor.execute("""
                                SELECT *
                                FROM category;
                                """)

    @classmethod
    def fill_db(cls):
        """
            fill the database with the transformed API data
        """
        sql = "INSERT INTO category (name,url) VALUES (%s, %s)"
        for i in PrepareData.obj_cat:

            cls.cursor.execute(sql, (i.name, i.url))