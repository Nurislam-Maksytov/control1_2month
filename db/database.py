import sqlite3


class Database:
    def __init__(self, db_name="library.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            author TEXT,
            year INTEGER,
            available INTEGER,
            type TEXT
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS readers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT
        )
        """)
        self.conn.commit()

    # 📚 CRUD для книг
    def add_book(self, title, author, year, book_type):
        self.cursor.execute(
            "INSERT INTO books (title, author, year, available, type) VALUES (?, ?, ?, ?, ?)",
            (title, author, year, 1, book_type)
        )
        self.conn.commit()

    def get_books(self):
        self.cursor.execute("SELECT * FROM books")
        return self.cursor.fetchall()

    def delete_book(self, book_id):
        self.cursor.execute("DELETE FROM books WHERE id=?", (book_id,))
        self.conn.commit()

    def search_books(self, query):
        query = f"%{query}%"
        self.cursor.execute(
            "SELECT * FROM books WHERE title LIKE ? OR author LIKE ?",
            (query, query)
        )
        return self.cursor.fetchall()

    # 👤 CRUD для читателей
    def add_reader(self, name, email):
        self.cursor.execute(
            "INSERT INTO readers (name, email) VALUES (?, ?)",
            (name, email)
        )
        self.conn.commit()

    def get_readers(self):
        self.cursor.execute("SELECT * FROM readers")
        return self.cursor.fetchall()