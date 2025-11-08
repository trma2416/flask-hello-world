from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World from Tristan Martinez in 3308!'


@app.route('/db_test')
def connect():
    conn = psycopg2.connect('postgresql://tmar_postgres_user:CB9YlJtgM8sN2OUiaWldcOAAk5si3oC7@dpg-d47d0sq4d50c73835go0-a/tmar_postgres')
    conn.close()
    return 'Database Connection Successful'

@app.route('/db_create')
def create_db():
    #use with block so no need to close connection each time
    with psycopg2.connect('postgresql://tmar_postgres_user:CB9YlJtgM8sN2OUiaWldcOAAk5si3oC7@dpg-d47d0sq4d50c73835go0-a/tmar_postgres') as conn:
        cursor = conn.connect()
        try:
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS Basketball(
                First varchar(255),
                Last varchar(255),
                City varchar(255),
                Name varchar(255),
                Number int
                );
                ''')
            conn.commit()
            return "Basketball created successfully"
        except Exception as e:
            return f"Error {e} occurred"