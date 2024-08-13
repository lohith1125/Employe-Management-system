import sqlite3

class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS employees (
                id INTEGER PRIMARY KEY,
                name TEXT,
                age INTEGER,
                doj TEXT,
                email TEXT,
                gender TEXT,
                contact TEXT,
                address TEXT
            )
        """)
        self.conn.commit()

    def insert(self, name, age, doj, email, gender, contact, address):
        self.cur.execute("INSERT INTO employees (name, age, doj, email, gender, contact, address) VALUES (?, ?, ?, ?, ?, ?, ?)",
                         (name, age, doj, email, gender, contact, address))
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM employees")
        rows = self.cur.fetchall()
        return rows

    def remove(self, id):
        self.cur.execute("DELETE FROM employees WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id, name, age, doj, email, gender, contact, address):
        self.cur.execute("UPDATE employees SET name = ?, age = ?, doj = ?, email = ?, gender = ?, contact = ?, address = ? WHERE id = ?",
                         (name, age, doj, email, gender, contact, address, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
