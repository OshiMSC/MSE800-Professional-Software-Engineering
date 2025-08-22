from database import create_connection
import sqlite3

def add_subjects(subject_Name,course_ID ):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO subjects (subject_Name,course_ID) VALUES (?,?)", (subject_Name,course_ID ))
        conn.commit()
        print(" User added successfully.")
    except sqlite3.IntegrityError:
        print(" Email must be unique.")
    conn.close()

def view_subjects():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM subjects")
    rows = cursor.fetchall()
    conn.close()
    return rows

def search_subjects(subject_Name):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM subjects WHERE subject_Name  LIKE ?", ('%' + subject_Name  + '%',))
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_subjects(subject_ID):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM subjects WHERE id = ?", (subject_ID,))
    conn.commit()
    conn.close()
    print("🗑️ User deleted.")
