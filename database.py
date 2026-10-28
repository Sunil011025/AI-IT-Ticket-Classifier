
import sqlite3
from pathlib import Path

DATABASE_PATH = Path(__file__).with_name("tickets.db")


def get_connection():
    """Create a connection to the SQLite database."""
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def init_db():
    """Create the tickets table if it doesn't exist."""
    with get_connection() as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS tickets (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                description TEXT NOT NULL,
                category TEXT NOT NULL,
                priority TEXT NOT NULL,
                sentiment TEXT NOT NULL,
                suggested_response TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

    print("Database initialized successfully!")


def save_ticket(description, result):
    """Save a classified ticket and return its ID."""
    with get_connection() as connection:
        cursor = connection.execute("""
            INSERT INTO tickets (
                description,
                category,
                priority,
                sentiment,
                suggested_response
            )
            VALUES (?, ?, ?, ?, ?)
        """, (
            description,
            result["category"],
            result["priority"],
            result["sentiment"],
            result["suggested_response"],
        ))

        return cursor.lastrowid


def get_all_tickets():
    """Return saved tickets, newest first."""
    with get_connection() as connection:
        rows = connection.execute("""
            SELECT * FROM tickets
            ORDER BY id DESC
        """).fetchall()

    return [dict(row) for row in rows]

def get_dashboard_stats():
    """Return total ticket, priority, and category counts."""
    with get_connection() as connection:
        total = connection.execute(
            "SELECT COUNT(*) FROM tickets"
        ).fetchone()[0]

        priority_rows = connection.execute("""
            SELECT priority, COUNT(*) AS count
            FROM tickets
            GROUP BY priority
        """).fetchall()

        category_rows = connection.execute("""
            SELECT category, COUNT(*) AS count
            FROM tickets
            GROUP BY category
        """).fetchall()

    priorities = {
        "Critical": 0,
        "High": 0,
        "Medium": 0,
        "Low": 0,
    }

    categories = {
        "Hardware": 0,
        "Software": 0,
        "Network": 0,
        "Access": 0,
        "Other": 0,
    }

    for row in priority_rows:
        if row["priority"] in priorities:
            priorities[row["priority"]] = row["count"]

    for row in category_rows:
        if row["category"] in categories:
            categories[row["category"]] = row["count"]

    return {
        "total": total,
        "priorities": priorities,
        "categories": categories,
    }
