# -*-coding:UTF-8-*
from ManageDb import*


def main():
    # get and clean the data
    PrepareData.get_and_clean_categories()
    PrepareData.instantiate_categories()
    PrepareData.get_and_clean_products()
    PrepareData.instantiate_products()
    PrepareData.get_and_instantiate_brands_and_stores()

    """# build and fill de data base
    ManageDb.build()
    ManageDb.show_tables()
    ManageDb.fill()
    ManageDb.select()"""

















if __name__ == '__main__':
    main()
else:
    pass