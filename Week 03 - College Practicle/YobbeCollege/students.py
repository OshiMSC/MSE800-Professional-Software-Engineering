from database import create_connection
import sqlite3

def add_user(student_name, student_email,phone,address,department_ID,course_ID):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO students (student_name, student_email,phone,address,department_ID,course_ID) VALUES (?, ?,?,?,?,?)", (student_name, student_email,phone,address,department_ID,course_ID))
        conn.commit()
        print(" User added successfully.")
    except sqlite3.IntegrityError:
        print(" Email must be unique.")
    conn.close()

def view_users():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    conn.close()
    return rows

def search_user(student_name):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE student_name LIKE ?", ('%' + student_name + '%',))
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_user(student_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()
    conn.close()
    print("🗑️ User deleted.")
