import sqlite3

class Course:
    def __init__(self, name):
        self.name = name

    def create(self):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO courses (name) VALUES (?)", (self.name,))
        conn.commit()
        conn.close()

    @classmethod
    def delete(cls, course_id):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM courses WHERE id = ?", (course_id,))
        conn.commit()
        conn.close()

    @staticmethod
    def get_all():
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM courses")
        courses = cursor.fetchall()
        conn.close()
        return courses

    @staticmethod
    def find_by_id(course_id):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM courses WHERE id = ?", (course_id,))
        course = cursor.fetchone()
        conn.close()
        return course

