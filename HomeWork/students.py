import sqlite3

conn = sqlite3.connect('students.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS student (
    id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    birth_year INTEGER,
    hobby TEXT,
    homework_score INTEGER
)
''')

students = [
    ('San', 'Li', 2000, 'Reading', 12),
    ('Wei', 'Chen', 1999, 'Gaming', 8),
    ('Hana', 'Kim', 2001, 'Music', 15),
    ('Taro', 'Yamamoto', 2002, 'Sports', 7),
    ('Mei', 'Zhang', 1998, 'Painting', 10),
    ('Jin', 'Park', 2003, 'Drawing', 11),
    ('Yuki', 'Tanaka', 1997, 'Cooking', 9),
    ('Sora', 'Watanabe', 2000, 'Dancing', 6),
    ('Liang', 'Wang', 2001, 'Traveling', 13),
    ('Aya', 'Matsumoto', 2002, 'Photography', 14)
]

cursor.executemany('''
INSERT INTO student (first_name, last_name, birth_year, hobby, homework_score)
VALUES (?, ?, ?, ?, ?)
''', students)

cursor.execute('''
SELECT * FROM student WHERE LENGTH(last_name) > 10
''')
students_with_long_last_name = cursor.fetchall()
print("Students with last name longer than 10 characters:")
for student in students_with_long_last_name:
    print(student)

cursor.execute('''
UPDATE student SET first_name = 'genius' WHERE homework_score > 10
''')

cursor.execute('''
SELECT * FROM student WHERE first_name = 'genius'
''')
genius_students = cursor.fetchall()
print("\nGenius students:")
for student in genius_students:
    print(student)

cursor.execute('''
DELETE FROM student WHERE id % 2 = 0
''')

cursor.execute('''
SELECT * FROM student
''')
remaining_students = cursor.fetchall()
print("\nRemaining students:")
for student in remaining_students:
    print(student)

conn.commit()
conn.close()

