import sqlite3

def main():
    with sqlite3.connect("contacts.db") as conn:
        cursor = conn.cursor()

        # Step 1: Create original table with 'id' as primary key
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS phone (
            id INTEGER PRIMARY KEY,
            country_code TEXT NOT NULL,
            phone_number TEXT NOT NULL,
            phone_type TEXT
        )
        """)

        # Step 2: Insert sample data
        sample = [
            (1, "US", "15550100", "CELLULAR"),
            (2, "XX", "99999999", "CELLULAR"),
        ]
        cursor.executemany("""
            INSERT OR IGNORE INTO phone (id, country_code, phone_number, phone_type)
            VALUES (?, ?, ?, ?)
        """, sample)
        conn.commit()

        # Step 3: SELECT phone numbers from US
        cursor.execute("SELECT phone_number FROM phone WHERE country_code = ?", ("US",))
        for (phone_number,) in cursor.fetchall():
            print(phone_number)

        # Step 4: UPDATE phone_type from CELLULAR to MOBILE
        cursor.execute("UPDATE phone SET phone_type = ? WHERE phone_type = ?", ("MOBILE", "CELLULAR"))
        conn.commit()

        # Step 5: DELETE rows with country_code = 'XX'
        cursor.execute("DELETE FROM phone WHERE country_code = ?", ("XX",))
        conn.commit()

        # Step 6: Recreate phone_new safely (drop if exists)
        cursor.execute("DROP TABLE IF EXISTS phone_new")
        cursor.execute("""
        CREATE TABLE phone_new (
            id INTEGER PRIMARY KEY,
            country_code TEXT NOT NULL,
            phone_number TEXT NOT NULL,
            phone_type TEXT
        )
        """)

        # Step 7: Copy data from phone to phone_new
        cursor.execute("""
        INSERT INTO phone_new (id, country_code, phone_number, phone_type)
        SELECT id, country_code, phone_number, phone_type FROM phone
        """)

        # Step 8: Replace old table with new one
        cursor.execute("DROP TABLE phone")
        cursor.execute("ALTER TABLE phone_new RENAME TO phone")
        conn.commit()

if __name__ == "__main__":
    main()