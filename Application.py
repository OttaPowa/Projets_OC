# -*-coding:UTF-8-*

from ManageDb import*
from constants import*
from PrepareData import*
from DbClasses import*



def main():


    # get and clean the data
    PrepareData.get_categories()
    PrepareData.instantiate(DICT_OF_CLASSES["Category"], PrepareData.cleaned_categories)
    PrepareData.get_and_sort_products()
    PrepareData.calibrate(PrepareData.raw_products)
    PrepareData.instantiate(DICT_OF_CLASSES["Product"], PrepareData.cleaned_products)

    STORES = [store.store for store in DbClasses.Product.instantiated_products]
    BRANDS = [brand.brand for brand in DbClasses.Product.instantiated_products]

    PrepareData.get_stores_or_brands(STORES)
    PrepareData.instantiate(DICT_OF_CLASSES["Store"], PrepareData.setted_items)
    print(DbClasses.Store.instantiated_stores[8].name)
    PrepareData.get_stores_or_brands(BRANDS)
    PrepareData.instantiate(DICT_OF_CLASSES["Brand"], PrepareData.setted_items)
    print(DbClasses.Brand.instantiated_brands[18].name)


    """PrepareData.get_and_clean_additional_data(BRANDS)
    PrepareData.instantiate_brands()

    # build and fill de data base
    ManageDb.build()
    ManageDb.fill(INSERT_CATS, DbClasses.Category.instantiated_categories)
    ManageDb.select(SQL_ARGS, NAME_OF_TABLE[0])
    ManageDb.fill(INSERT_STORES, DbClasses.Store.instantiated_stores)
    ManageDb.select(SQL_ARGS, NAME_OF_TABLE[2])
    ManageDb.fill(INSERT_BRANDS, DbClasses.Brand.instantiated_brands)
    ManageDb.select(SQL_ARGS, NAME_OF_TABLE[3])"""















if __name__ == '__main__':
    main()
else:
    pass