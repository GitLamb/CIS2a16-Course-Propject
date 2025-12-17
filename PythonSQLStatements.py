# Jason Lambert
# CIS261
# Python SQL Statements

import sqlite3

def main():
    # Connect to database and enable named row access
    with sqlite3.connect("contacts.db") as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        # Create table if missing
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS phone (
            id INTEGER PRIMARY KEY,
            phone_number TEXT NOT NULL UNIQUE,
            country_code TEXT,
            phone_type TEXT
        )
        """)

        # Insert sample row (ignore if already exists)
        cursor.execute("""
        INSERT OR IGNORE INTO phone (phone_number, country_code, phone_type)
        VALUES (?, ?, ?)
        """, ("+1-555-0100", "US", "CELLULAR"))

        # Select phone numbers where country_code = "US"
        cursor.execute("SELECT phone_number FROM phone WHERE country_code = ?", ("US",))
        for row in cursor.fetchall():
            print(row["phone_number"])

if __name__ == "__main__":
    main()