import sqlite3

class Book:
    def __init__(self, title, year, cost, author_id, course_id):
        self.title = title
        self.year = year
        self.cost = cost
        self.author_id = author_id
        self.course_id = course_id

    def create(self):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO books (title, year, cost, author_id, course_id) VALUES (?, ?, ?, ?, ?)", (self.title, self.year, self.cost, self.author_id, self.course_id))
        conn.commit()
        conn.close()

    def delete(self):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM books WHERE id = ?", (self.id,))
        conn.commit()
        conn.close()

    @staticmethod
    def get_all():
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books")
        books = cursor.fetchall()
        conn.close()
        return books

    @staticmethod
    def find_by_id(book_id):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books WHERE id = ?", (book_id,))
        book = cursor.fetchone()
        conn.close()
        return book