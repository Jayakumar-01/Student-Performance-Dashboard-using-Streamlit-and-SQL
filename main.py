import streamlit as st
import pandas as pd
from db_manager import DBManager

st.set_page_config(page_title="Student Dashboard", layout="wide")

# Connect to your SQLite database
db = DBManager("student_data.db")

# Tabs for Navigation
tab1, tab2 = st.tabs(["🎓 Eligible Students", "📊 Insights"])

# TAB 1: Eligibility Dashboard
with tab1:
    st.title("Student Eligibility Dashboard")

    st.sidebar.header("Filter Criteria")
    min_problems = st.sidebar.slider("Minimum Problems Solved", 0, 100, 50)
    min_softskills = st.sidebar.slider("Minimum Soft Skills Average", 50, 100, 75)

    # Get filtered students
    results = db.get_eligible_students(min_problems, min_softskills)

    df = pd.DataFrame(
    results,
    columns=["ID", "Name", "Problems_Solved", "Communication", "Teamwork", "Presentation", "Placement_Status"]
)


    st.subheader("Eligible Students")
    st.write(f"Showing {len(df)} students out of 100")
    st.dataframe(df)

# TAB 2: Insights
with tab2:
    st.title("📊 Insights from Data")

    # Insight 1: Average problems solved
    avg_query = "SELECT AVG(problems_solved) FROM programming"
    db.cursor.execute(avg_query)
    avg_problems = db.cursor.fetchone()[0]
    st.metric("📈 Average Problems Solved", f"{avg_problems:.2f}")

    # Insight 2: Top 5 Interview Performers
    top_query = """
    SELECT s.name, p.mock_interview_score
    FROM students s
    JOIN placements p ON s.student_id = p.student_id
    ORDER BY p.mock_interview_score DESC LIMIT 5
    """
    top_5 = db.cursor.execute(top_query).fetchall()
    top_df = pd.DataFrame(top_5, columns=["Student", "Mock Interview Score"])

    st.subheader("🏆 Top 5 Mock Interview Performers")
    st.table(top_df)
df = pd.DataFrame(
    results,
    columns=["ID", "Name", "Problems_Solved", "Communication", "Teamwork", "Presentation", "Placement_Status"]
)
