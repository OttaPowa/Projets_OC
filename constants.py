# -*-coding:UTF-8-*


NAME_OF_TABLE = ["category", "products", "store", "brand"]
COLUMN = ["name", "url"]
SQL_ARGS = "*"

INSERT_CATS = f"INSERT INTO {NAME_OF_TABLE[0]} ({COLUMN[0]}, {COLUMN[1]}) VALUES (%s, %s)"
INSERT_STORES = f"INSERT INTO {NAME_OF_TABLE[2]} ({COLUMN[0]}) VALUES (%s)"
INSERT_BRANDS = f"INSERT INTO {NAME_OF_TABLE[3]} ({COLUMN[0]}) VALUES (%s)"

DICT_OF_CLASSES = {'class0': 'Store', 'class1': 'Brand', 'class2': 'Product', 'class3': 'Category'}
# comment faire pour instancier en automatique en remplacant le nom de la classe

