# -*-coding:UTF-8-*

from ManageDb import*
from constants import*
from PrepareData import*



def main():


    # get and clean the data
    PrepareData.get_categories()
    PrepareData.instantiate_categories()
    PrepareData.get_and_verify_products_integrity()
    PrepareData.instantiate_products()

    STORES = [store.store for store in PrepareData.instantiated_products]
    BRANDS = [brand.brand for brand in PrepareData.instantiated_products]

    PrepareData.get_and_clean_additional_data(STORES)
    PrepareData.instantiate_stores()
    PrepareData.get_and_clean_additional_data(BRANDS)
    PrepareData.instantiate_brands()

    # build and fill de data base
    ManageDb.build()
    ManageDb.fill(INSERT_CATS, PrepareData.instantiated_categories)
    ManageDb.select(SQL_ARGS, NAME_OF_TABLE[0])
    ManageDb.fill(INSERT_STORES, PrepareData.instantiated_stores)
    ManageDb.select(SQL_ARGS, NAME_OF_TABLE[2])
    ManageDb.fill(INSERT_BRANDS, PrepareData.instantiated_brands)
    ManageDb.select(SQL_ARGS, NAME_OF_TABLE[3])















if __name__ == '__main__':
    main()
else:
    pass