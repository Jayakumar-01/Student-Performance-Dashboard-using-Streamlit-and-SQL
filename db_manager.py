import sqlite3

class DBManager:
    def __init__(self, db_name="student_data.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def get_eligible_students(self, min_problems, min_softskills):
        query = f"""
        SELECT s.student_id, s.name, p.problems_solved, sk.communication, sk.teamwork, sk.presentation, pl.placement_status
        FROM students s
        JOIN programming p ON s.student_id = p.student_id
        JOIN soft_skills sk ON s.student_id = sk.student_id
        JOIN placements pl ON s.student_id = pl.student_id
        WHERE p.problems_solved >= {min_problems}
        AND (sk.communication + sk.teamwork + sk.presentation) / 3 >= {min_softskills}
        """
        return self.cursor.execute(query).fetchall()
