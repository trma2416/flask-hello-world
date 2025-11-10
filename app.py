from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World from Tristan Martinez in 3308!'


@app.route('/db_test')
def connect():
    try:
        conn = psycopg2.connect('postgresql://tmar_postgres_user:CB9YlJtgM8sN2OUiaWldcOAAk5si3oC7@dpg-d47d0sq4d50c73835go0-a/tmar_postgres')
        return 'Database Connection Successful'
    except psycopg2.Error:
        return "connection unsuccessful"
    finally:
        
        conn.close()
    

@app.route('/db_create')
def create_db():
    
    conn = psycopg2.connect('postgresql://tmar_postgres_user:CB9YlJtgM8sN2OUiaWldcOAAk5si3oC7@dpg-d47d0sq4d50c73835go0-a/tmar_postgres')
    cursor = conn.cursor()
    try:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS basketball(
                first VARCHAR(255),
                last VARCHAR(255),
                city VARCHAR(255),
                name VARCHAR(255),
                number INT
                );
                ''')
        conn.commit()
        return "Basketball created successfully"
    except Exception as e:
        return f"Error {e} occurred"
    finally:
        cursor.close()
        conn.close()

@app.route('/db_insert')
def inserting():
    conn = psycopg2.connect('postgresql://tmar_postgres_user:CB9YlJtgM8sN2OUiaWldcOAAk5si3oC7@dpg-d47d0sq4d50c73835go0-a/tmar_postgres')
    cursor = conn.cursor()
    try:
        cursor.execute('''
                       INSERT INTO basketball (first, last, city, name, number)
                       VALUES
                       ('Jason', 'Tatum', 'Boston', 'Celtics', 0),
                       ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
                       ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
                       ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2),
                       ('Tristan', 'Martinez', 'CU Boulder','Buffs', 3308);
                       
                       ''')
        conn.commit()
        return "Basketball Table successfully populated"
    except psycopg2.Error:
        return "Error inserting data"
    finally:
        cursor.close()
        conn.close()
        
@app.route('/db_select')
def select():
    conn = psycopg2.connect('postgresql://tmar_postgres_user:CB9YlJtgM8sN2OUiaWldcOAAk5si3oC7@dpg-d47d0sq4d50c73835go0-a/tmar_postgres')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM basketball''')
    records = cursor.fetchall()
    cursor.close()
    conn.close()
    response_str = ""
    response_str += "<table>"
    for player in records:
        response_str += "<tr>"
        for info in player:
            response_str += f"<td>{info}<td>"
        response_str += "</tr>"
    response_str += "</table>"
    return response_str


@app.route('/db_drop')
def drop():
    conn = psycopg2.connect('postgresql://tmar_postgres_user:CB9YlJtgM8sN2OUiaWldcOAAk5si3oC7@dpg-d47d0sq4d50c73835go0-a/tmar_postgres')
    cursor = conn.cursor()
    try:
        cursor.execute('''DROP TABLE IF EXISTS basketball;
                       ''')
        conn.commit()
        return "Basketball Table Successfully Dropped"
    finally:
        cursor.close()
        conn.close()