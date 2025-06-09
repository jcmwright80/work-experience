import MySQLdb

def get_connection():
    return MySQLdb.connect(
        host="127.0.0.1",
        user="root",
        password="root",
        db="todo",
        port=3307
    )
