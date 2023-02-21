import sqlite3
from faker import Faker
import random
import time
import os

# Check if the database file exists, and create a new one if it doesn't
if not os.path.isfile("messages.db"):
    conn = sqlite3.connect("messages.db")
    cur = conn.cursor()

    # Create the users table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT,
            phone_number TEXT,
            email TEXT
        )
    """)

    # Create the messages table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY,
            user_id INTEGER REFERENCES users (id),
            parent_id INTEGER REFERENCES messages (id),
            message TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()

# Connect to the database
conn = sqlite3.connect("messages.db")
cur = conn.cursor()

fake = Faker()

# Generate 1k mock users
for i in range(1000):
    name = fake.name()
    phone_number = fake.phone_number()
    email = fake.email()
    cur.execute("INSERT INTO users (name, phone_number, email) VALUES (?, ?, ?)", (name, phone_number, email))

# Commit the users to the database
conn.commit()

# Generate 500k messages
for i in range(500000):
    user_id = random.randint(1, 1000)
    parent_id = random.randint(1, i) if i > 0 else None
    message = fake.text(500)
    cur.execute("INSERT INTO messages (user_id, parent_id, message) VALUES (?, ?, ?)", (user_id, parent_id, message))

    # Commit every 1000 messages
    if i % 1000 == 0:
        conn.commit()

# Commit any remaining messages to the database
conn.commit()

# Query the leaderboard stats and report the query time
start_time = time.time()
cur.execute("""
    SELECT user_id, COUNT(*) as num_messages
    FROM messages
    GROUP BY user_id
    ORDER BY num_messages DESC
    LIMIT 10
""")
result = cur.fetchall()
end_time = time.time()
print("Query time:", end_time - start_time, "seconds")

# Close the database connection
conn.close()