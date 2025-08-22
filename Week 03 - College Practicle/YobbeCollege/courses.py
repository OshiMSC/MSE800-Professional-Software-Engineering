from database import create_connection
import sqlite3

def add_course(course_Name,duration,department_ID ):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO course (course_Name,duration,department_ID ) VALUES (?, ?,?)", (course_Name,duration,department_ID ))
        conn.commit()
        print(" User added successfully.")
    except sqlite3.IntegrityError:
        print(" Email must be unique.")
    conn.close()

def view_course():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM course")
    rows = cursor.fetchall()
    conn.close()
    return rows

def search_course(course_Name):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM course WHERE course_Name LIKE ?", ('%' + course_Name + '%',))
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_course(course_ID):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM course WHERE id = ?", (course_ID,))
    conn.commit()
    conn.close()
    print("🗑️ User deleted.")
