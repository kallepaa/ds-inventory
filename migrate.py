import sqlite3
from sqlite3 import Error
import glob
import config

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    return conn

if __name__ == '__main__':

    con = create_connection(config.db)

    if con:
        files = glob.glob(config.db_migrate)
        
        for f in files:
            cur = con.cursor() 
            with open(f, "r") as f_in:
                sql = f_in.read() 
            cur.executescript(sql)
        
        con.close()
