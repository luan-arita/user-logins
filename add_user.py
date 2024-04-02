import hashlib
import sqlite3
import maskpass

def username_taken(name):
    conn = sqlite3.connect("ppadb6.db")
    #c = conn.cursor()

    cursor = conn.execute('SELECT username FROM users WHERE username = ?', (name,))

    data = cursor.fetchone()
    if data is None:
        return False
    else:
        return True

#print(username_taken('John'))

if __name__ == "__main__":
    print("Login")

    while True:
        username = input("What is your username? ")
        if username_taken(username):
            print("Username already taken!")
        else:
            print("Username available.")
            break    

    password = maskpass.askpass(prompt = "What is your password? ", mask = "#")

    password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    
    conn = sqlite3.connect("ppadb6.db")
    c = conn.cursor()

    c.execute("INSERT INTO users VALUES (?, ?)", (username, password))

    conn.commit()

    result = c.execute("SELECT * FROM users")
    for row in result:
        print(row)


