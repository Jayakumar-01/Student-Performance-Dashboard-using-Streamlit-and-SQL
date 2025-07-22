import sqlite3
import random

# Connect to SQLite
conn = sqlite3.connect("student_data.db")
cursor = conn.cursor()

# Drop tables if they exist
cursor.execute("DROP TABLE IF EXISTS students")
cursor.execute("DROP TABLE IF EXISTS programming")
cursor.execute("DROP TABLE IF EXISTS soft_skills")
cursor.execute("DROP TABLE IF EXISTS placements")

# Create students table
cursor.execute("""
    CREATE TABLE students (
        student_id INTEGER PRIMARY KEY,
        name TEXT
    )
""")

# Create programming table
cursor.execute("""
    CREATE TABLE programming (
        student_id INTEGER,
        problems_solved INTEGER,
        FOREIGN KEY(student_id) REFERENCES students(student_id)
    )
""")

# Create soft_skills table
cursor.execute("""
    CREATE TABLE soft_skills (
        student_id INTEGER,
        communication INTEGER,
        teamwork INTEGER,
        presentation INTEGER,
        FOREIGN KEY(student_id) REFERENCES students(student_id)
    )
""")

# Create placements table
cursor.execute("""
    CREATE TABLE placements (
        student_id INTEGER,
        mock_interview_score INTEGER,
        placement_status TEXT,
        FOREIGN KEY(student_id) REFERENCES students(student_id)
    )
""")

# Insert fake data
for i in range(1, 101):
    name = f"Student {i}"
    problems_solved = random.randint(20, 100)
    communication = random.randint(50, 100)
    teamwork = random.randint(50, 100)
    presentation = random.randint(50, 100)
    mock_score = random.randint(40, 100)
    status = random.choice(["Placed", "Not Placed"])

    cursor.execute("INSERT INTO students (student_id, name) VALUES (?, ?)", (i, name))
    cursor.execute("INSERT INTO programming (student_id, problems_solved) VALUES (?, ?)", (i, problems_solved))
    cursor.execute("INSERT INTO soft_skills (student_id, communication, teamwork, presentation) VALUES (?, ?, ?, ?)",
                   (i, communication, teamwork, presentation))
    cursor.execute("INSERT INTO placements (student_id, mock_interview_score, placement_status) VALUES (?, ?, ?)",
                   (i, mock_score, status))

conn.commit()
conn.close()
print("✅ Database setup complete with dummy data.")
