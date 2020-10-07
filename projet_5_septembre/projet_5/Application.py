# -*-coding:UTF-8-*
from ManageDb import*


def main():

    PrepareData.get_data()
    PrepareData.transform_data()
    PrepareData.clean_and_instantiate_data()
    ManageDb.build_db()
    ManageDb.fill_db()

















if __name__ == '__main__':
    main()
else:
    pass