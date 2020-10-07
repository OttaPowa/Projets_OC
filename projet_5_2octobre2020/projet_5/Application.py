# -*-coding:UTF-8-*
from ManageDb import*


def main():

    PrepareData.get_and_clean_categories()
    PrepareData.instantiate_categories()
    PrepareData.get_and_clean_products()
    """ManageDb.build_db()
    ManageDb.fill_db()
    ManageDb.update()"""

















if __name__ == '__main__':
    main()
else:
    pass