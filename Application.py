# -*-coding:UTF-8-*

from ManageDb import*
from constants import*
from PrepareData import*
from Category import Category
from Product import Product
from Brand import Brand
from Store import Store



def main():


    # get and clean the data
    PrepareData.get_categories()
    PrepareData.instantiate(DICT_OF_CLASSES["Category"], PrepareData.cleaned_categories)
    PrepareData.get_and_sort_products()
    PrepareData.calibrate(PrepareData.raw_products)
    PrepareData.instantiate(DICT_OF_CLASSES["Product"], PrepareData.cleaned_products)

    STORES = [store.store for store in Product.instantiated_products]
    BRANDS = [brand.brand for brand in Product.instantiated_products]

    PrepareData.get_stores_or_brands(STORES)
    PrepareData.instantiate(DICT_OF_CLASSES["Store"], PrepareData.setted_items)
    PrepareData.get_stores_or_brands(BRANDS)
    PrepareData.instantiate(DICT_OF_CLASSES["Brand"], PrepareData.setted_items)

    # build and fill de data base
    ManageDb.build()
    ManageDb.fill(INSERT_CATS, Category.instantiated_categories)
    ManageDb.select(SQL_ARGS, NAME_OF_TABLE[0])
    ManageDb.fill(INSERT_STORES, Store.instantiated_stores)
    ManageDb.select(SQL_ARGS, NAME_OF_TABLE[2])
    ManageDb.fill(INSERT_BRANDS, Brand.instantiated_brands)
    ManageDb.select(SQL_ARGS, NAME_OF_TABLE[3])
    ManageDb.fill(INSERT_PRODUCTS, Product.instantiated_products)
    ManageDb.select(SQL_ARGS, NAME_OF_TABLE[1])
    ManageDb.select(COLUMN[0], NAME_OF_TABLE[1])
    ManageDb.select(COLUMN[1], NAME_OF_TABLE[0])
    ManageDb.insert_n_n_test() # methode en test
    """ManageDb.select(SQL_ARGS, NAME_OF_TABLE[4])"""











if __name__ == '__main__':
    main()
else:
    pass