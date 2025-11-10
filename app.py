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
    conn = psycopg2.connect('postgresql://tmar_postgres_user:CB9YlJtgM8sN2OUiaWldcOAAk5si3oC7@dpg-d47d0sq4d50c73835go0-a/tmar_postgres')
    cursor = conn.connect()
    try:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Basketball(
                First VARCHAR(255),
                Last VARCHAR(255),
                City VARCHAR(255),
                Name VARCHAR(255),
                Number INT
                );
                ''')
        conn.commit()
        return "Basketball created successfully"
    except Exception as e:
        return f"Error {e} occurred"
    finally:
        conn.close()
        
@app.route('/db_select')
def select():
    conn = psycopg2.connect('postgresql://tmar_postgres_user:CB9YlJtgM8sN2OUiaWldcOAAk5si3oC7@dpg-d47d0sq4d50c73835go0-a/tmar_postgres')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM Basketball''')
    records = cursor.fetchall()
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