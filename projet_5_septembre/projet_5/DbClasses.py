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


"""class Product:
    def __init__(self,
                 id=int,
                 name="",
                 url="",
                 picture_url="",
                 brand_id= Brand.id,
                 store_id = Store.id,
                 description="",
                 nutriscore="",
                 category_id= Category.id):

        self.id = id
        self.name = name
        self.url = url
        self.picture_url = picture_url
        self.brand_id = Brand.id
        self.store_id = Store.id
        self.description = description
        self.nutriscore = nutriscore
        self.category_id = Category.id"""


"""class Store(Category):



class Brand(Category):"""
