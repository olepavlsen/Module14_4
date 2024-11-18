import sqlite3

connection = sqlite3.connect("products.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Products(
id INTEGER,
title TEXT NOT NULL,
description TEXT NOT NULL,
price INTEGER NOT NULL
);
''')


def initiate_db(prod_id, title, description, price):
    check_prod = cursor.execute("SELECT * FROM Products WHERE id=?", (prod_id,))
    if check_prod.fetchone() is None:
        cursor.execute(f'''
    INSERT INTO Products VALUES('{prod_id}', '{title}', '{description}', '{price}')
''')
    connection.commit()


def get_all_products():
    cursor.execute("SELECT * FROM Products")
    products = cursor.fetchall()
    # for prod in products:
    #     print(prod)
    return products
initiate_db(1, "Product1", "Описание1", 100)
initiate_db(2, "Product2", "Описание1", 200)
initiate_db(3, "Product3", "Описание1", 300)
initiate_db(4, "Product4", "Описание1", 400)

connection.commit()
# connection.close()
