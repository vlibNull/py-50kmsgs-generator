from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Set up a route to display the messages
@app.route("/")
def display_messages():
    # Get the page number from the URL query parameters
    page = int(request.args.get("page", 1))

    # Connect to the database
    conn = sqlite3.connect("messages.db")
    cur = conn.cursor()

    # Retrieve the total number of messages
    cur.execute("SELECT COUNT(*) FROM messages")
    total_messages = cur.fetchone()[0]

    # Calculate the number of messages to display per page
    messages_per_page = 100
    total_pages = (total_messages + messages_per_page - 1) // messages_per_page

    # Calculate the offset for the current page
    offset = (page - 1) * messages_per_page

    # Retrieve the messages for the current page
    cur.execute("""
        SELECT m.id, m.message, u.name, m.created_at
        FROM messages m
        JOIN users u ON m.user_id = u.id
        ORDER BY m.created_at DESC
        LIMIT ? OFFSET ?
    """, (messages_per_page, offset))
    messages = cur.fetchall()

    # Close the database connection
    conn.close()

    # Render the template with the messages and pagination links
    return render_template("messages.html", messages=messages, total_pages=total_pages, current_page=page)

if __name__ == "__main__":
    app.run(debug=True)