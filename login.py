import sqlite3
import hashlib
import maskpass

def is_valid_credentials(input_username, input_password):
    conn = sqlite3.connect("ppadb6.db")


    cursor = conn.execute('SELECT password_hash FROM users WHERE username = ?', (input_username,))

    password = cursor.fetchone()[0]

    conn.close()
    if password == input_password:
        return True
    return False


if __name__ == "__main__":
    print("Login")

    while True:
        username = input("What is your username? ")
        password = maskpass.askpass(prompt = "What is your password? ", mask = "#")
        password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        
        if is_valid_credentials(username, password):
            print("Access granted.")
            print("Revealing darkest secret...")
        else:
            print("Access denied.")