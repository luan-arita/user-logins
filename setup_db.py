import os
import sqlite3

path = './ppadb6.db'

if __name__ == "__main__":
    if os.path.isfile(path):
        while True:
            answer = input("Database already exists. Do you want to delete and recreate it? y/n ")

            if answer == 'y':
                os.remove(path)
                break
            elif answer == 'n':
                print("Ok. Exiting")
                exit(0)
            else:
                print("I didn't understand you.")
                
    conn = sqlite3.connect("ppadb6.db")
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS users(username VARCHAR, password_hash VARCHAR)")

    conn.commit()

    print("Database created!")
