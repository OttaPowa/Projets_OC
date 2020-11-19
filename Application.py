# -*-coding:UTF-8-*

from ManageDb import*
from constants import*
from PrepareData import*
from Category import Category
from Product import Product
from Brand import Brand
from Store import Store
from Interactions import Interactions


def main():

    # get and clean the data:
    PrepareData.get_categories()
    PrepareData.get_and_sort_products()
    PrepareData.calibrate(PrepareData.raw_products)
    PrepareData.instantiate(DICT_OF_CLASSES["Product"], PrepareData.cleaned_products)

    STORES = [store.store for store in Product.instantiated_products]
    BRANDS = [brand.brand for brand in Product.instantiated_products]
    CATEGORIES = [categories.category for categories in Product.instantiated_products]

    PrepareData.get_and_set(STORES)
    PrepareData.instantiate(DICT_OF_CLASSES["Store"], PrepareData.setted_items)
    PrepareData.get_and_set(BRANDS)
    PrepareData.instantiate(DICT_OF_CLASSES["Brand"], PrepareData.setted_items)
    PrepareData.get_and_set(CATEGORIES)
    PrepareData.get_url(PrepareData.setted_items)
    PrepareData.instantiate(DICT_OF_CLASSES["Category"], PrepareData.cleaned_cat_with_url)

    # build and fill the data base:
    ManageDb.build()
    ManageDb.fill(INSERT_CATS, Category.instantiated_categories)
    ManageDb.fill(INSERT_STORES, Store.instantiated_stores)
    ManageDb.fill(INSERT_BRANDS, Brand.instantiated_brands)
    ManageDb.fill(INSERT_PRODUCTS, Product.instantiated_products)
    ManageDb.insert_n_n(Product.instantiated_products, NAME_OF_TABLE[1], NAME_OF_TABLE[2],
                        NAME_OF_TABLE[4], COLUMN[8], COLUMN[6])
    ManageDb.insert_n_n(Product.instantiated_products, NAME_OF_TABLE[1], NAME_OF_TABLE[3],
                        NAME_OF_TABLE[5], COLUMN[8], COLUMN[7])  # method en test
    ManageDb.insert_n_n(Product.instantiated_products, NAME_OF_TABLE[1], NAME_OF_TABLE[0],
                        NAME_OF_TABLE[6], COLUMN[8], COLUMN[5])

    # application:
    print(GREETING_MESSAGE)

    if Interactions.authentication() is False:
        Interactions.authentication()
    else:
        ManageDb.select((COLUMN[4], COLUMN[0]), NAME_OF_TABLE[0])
        nbr = Interactions.selection()
        ManageDb.select(COLUMN[0], f"{NAME_OF_TABLE[0]} WHERE {COLUMN[4]} = {nbr}") # affiche le nom de la catégorie correpondnat a l'id tapé




if __name__ == '__main__':
    main()
else:
    pass