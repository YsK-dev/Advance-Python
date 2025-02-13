import sqlite3


conn = sqlite3.connect('example.db')# Connect to SQLite database or create it if it doesn't exist


cursor = conn.cursor()# Create a cursor 

# Create a table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    email TEXT NOT NULL UNIQUE
)
''')

# Insert some data to the table
def insert_user(name, age, email):
    cursor.execute('''
    INSERT INTO users (name, age, email) VALUES (?, ?, ?)
    ''', (name, age, email))
    conn.commit()
    print(f"User {name} added successfully!")

# Query all users
def fetch_all_users():
    cursor.execute('SELECT * FROM users')
    rows = cursor.fetchall()
    for row in rows:
        print(row)

# Query a single user by email
def fetch_user_by_email(email):
    cursor.execute('SELECT * FROM users WHERE email = ?', (email,))
    user = cursor.fetchone()
    if user:
        print(f"User found: {user}")
    else:
        print(f"No user found with email: {email}")

# Update a user's age by email
def update_user_age(email, new_age):
    cursor.execute('''
    UPDATE users SET age = ? WHERE email = ?
    ''', (new_age, email))
    conn.commit()
    print(f"User with email {email} updated to age {new_age}")

# Delete a user by email
def delete_user(email):
    cursor.execute('DELETE FROM users WHERE email = ?', (email,))
    conn.commit()
    print(f"User with email {email} deleted successfully!")

# Main function to demonstrate functionality
def main():
    # Insert some users
    insert_user('yakup', 30, 'yakubişko@gmail.com')
    insert_user('eyub', 25, 'alkan@gmail.com')
    insert_user('Esra', 35, 'srtky@gmail.com')

    # Fetch all users
    print("\nAll users:")
    fetch_all_users()

    # Fetch a single user by email
    print("\nFetching user by email:")
    fetch_user_by_email('bob@example.com')

    # Update a user's age
    print("\nUpdating user's age:")
    update_user_age('alice@example.com', 31)
    fetch_all_users()

    # Delete a user
    print("\nDeleting user:")
    delete_user('charlie@example.com')
    fetch_all_users()

    # Close the connection
    conn.close()

if __name__ == '__main__':
    main()