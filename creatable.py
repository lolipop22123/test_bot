import psycopg2

class DB:
    def __init__(self, dbname, user, password, host):
        self.connection = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, sslmode='disable')
        self.cursor = self.connection.cursor()
        self.connection.autocommit = True
    
    
    def create(self):
        with self.connection:

                self.cursor.execute('''CREATE TABLE public.users
(
    user_id bigint,
    username character varying
);''')     
                
                self.cursor.execute('''CREATE TABLE public.product
(
    id serial NOT NULL,
    name character varying,
    description character varying
);''')
                
                self.cursor.execute('''CREATE TABLE public.goods
(
    id serial NOT NULL,
    user_id bigint
    product_id bigint
);''')


DB('testbot', 'postgres', '1111', 'localhost').create()
 ###