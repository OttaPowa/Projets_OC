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
                 nutriscore="",
                 category= ""):
        """
            Constructor
            :param arg1: name of the product
            :type arg1: string
            :param arg2: url of the product
            :type arg2: string
            :param arg3: url of the picture of the product
            :type arg3: string
            :param arg4: brand of the product
            :type arg4: string
            :param arg5: stores were the product can be bought
            :type arg5: string
            :param arg6: nutriscore of the product
            :type arg6: string
            :param arg7: category of the product
            :type arg7: string
        """

        self.name = name
        self.url = url
        self.picture_url = picture_url
        self.brand = brand
        self.store = store
        self.nutriscore = nutriscore
        self.category = category


class Brand:
    def __init__(self,
                 name=""):
        """
            Constructor
            :param arg1: name of the product
            :type arg1: string
        """

        self.name = name


class Store(Brand):
    """
        child class of Category
    """


