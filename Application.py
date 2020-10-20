# -*-coding:UTF-8-*

from ManageDb import*
from constants import*
from PrepareData import*



def main():


    # get and clean the data
    PrepareData.get_and_clean_categories()
    PrepareData.instantiate_categories()
    PrepareData.get_and_clean_products()
    PrepareData.instantiate_products()
    MY_PRODUCTS_BRANDS = [brand.brand for brand in PrepareData.instantiated_products]
    MY_PRODUCTS_STORES = [store.store for store in PrepareData.instantiated_products]
    PrepareData.get_and_clean_brands_and_stores()
"""
    # build and fill de data base
    ManageDb.build()
    ManageDb.fill(INSERT_SQL, PrepareData.instantiated_categories)
    ManageDb.select(NAMES_OF_TABLES[0])
    """
















if __name__ == '__main__':
    main()
else:
    pass