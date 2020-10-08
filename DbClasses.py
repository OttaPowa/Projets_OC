# -*-coding:UTF-8-*


class Category:

    def __init__(self,
                 name="",
                 url=""):
        """
            Constructor
            :param arg1: name of the category
            :type arg1: string
            :param arg2: url of the category
            :type arg2: string
        """

        self.name = name
        self.url = url


class Product:
    def __init__(self,
                 name="",
                 url="",
                 picture_url="",
                 brand="",
                 store="",
                 description="",
                 nutriscore="",
                 category=""):

        self.name = name
        self.url = url
        self.picture_url = picture_url
        self.brand = brand
        self.store = store
        self.description = description
        self.nutriscore = nutriscore
        self.category = category


class Store(Category):
    """
        child class of Category
    """


class Brand(Category):
    """
        child class of Category
    """