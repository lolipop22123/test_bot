import psycopg2
import os
import pickle

class DB:
    def __init__(self, dbname, user, password, host):
        self.connection = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, sslmode='disable')
        self.cursor = self.connection.cursor()
        self.connection.autocommit = True
    

    def add_user(self, user_id, username):
        with self.connection:
            self.cursor.execute('SELECT user_id FROM users WHERE user_id=%s', (user_id,))
            result = self.cursor.fetchone()
            if result == None:
                self.cursor.execute(
                    'INSERT INTO users (user_id, username) VALUES (%s, %s)',
                    (user_id, username))
                return
            else:
                return
    
    def add_product(self, name, description):
        with self.connection:
            self.cursor.execute(
                'INSERT INTO product (name, description) VALUES (%s, %s)',
                (name, description))
            return
    
    def get_all_products(self):
        with self.connection:
            self.cursor.execute('SELECT id, name, description FROM public.product')
            products = self.cursor.fetchall()
            return products
        
    
    def add_products_good(self, user_id, product_id):
            with self.connection:
                self.cursor.execute(
                    'SELECT * FROM goods WHERE user_id = %s AND product_id = %s',
                    (user_id, product_id))
                result = self.cursor.fetchone()

                if result is None:
                    self.cursor.execute(
                        'INSERT INTO goods (user_id, product_id) VALUES (%s, %s)',
                        (user_id, product_id))
                else:
                    # Если запись уже есть в базе данных, можно обновить ее или выполнить другие действия
                    # self.cursor.execute(
                    #     'UPDATE goods SET ... WHERE user_id = %s AND product_id = %s',
                    #     (user_id, product_id))
                    pass

                self.connection.commit()  # Важно выполнить коммит после операций с базой данных
    
    def is_product_purchased(self, user_id, product_id):
        with self.connection:
            self.cursor.execute(
                'SELECT * FROM goods WHERE user_id = %s AND product_id = %s',
                (user_id, product_id))
            result = self.cursor.fetchone()

            return result is not None  # Вернет True, если запись существует, и False в противном случае
