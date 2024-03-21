import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS authors (
    id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT
);''')

cursor.execute('''CREATE TABLE IF NOT EXISTS courses (
    id INTEGER PRIMARY KEY,
    name TEXT
);''')

cursor.execute('''CREATE TABLE books (
    id INTEGER PRIMARY KEY,
    title TEXT,
    year INTEGER,
    cost INTEGER,
    author_id INTEGER,
    course_id INTEGER,
    FOREIGN KEY (author_id) REFERENCES authors(id),
    FOREIGN KEY (course_id) REFERENCES courses(id)
);''')

conn.commit()
conn.close()
