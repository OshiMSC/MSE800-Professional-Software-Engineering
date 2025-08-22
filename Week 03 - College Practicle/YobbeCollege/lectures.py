from database import create_connection
import sqlite3

def add_lectures(lecturer_Name,lecturer_Email,department_ID,course_ID):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO lecturers (lecturer_Name,lecturer_Email,department_ID,course_ID) VALUES (?, ?,?,?)", (lecturer_Name,lecturer_Email,department_ID,course_ID))
        conn.commit()
        print(" User added successfully.")
    except sqlite3.IntegrityError:
        print(" Email must be unique.")
    conn.close()

def view_lectures():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM lecturers")
    rows = cursor.fetchall()
    conn.close()
    return rows

def search_lectures(lecturer_Name):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM lecturers WHERE lecturer_Name LIKE ?", ('%' + lecturer_Name + '%',))
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_lectures(lecturer_Id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM lecturers WHERE id = ?", (lecturer_Id,))
    conn.commit()
    conn.close()
    print("🗑️ User deleted.")
