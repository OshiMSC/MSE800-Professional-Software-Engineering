from database import create_connection
import sqlite3

def add_departments(department_Name ):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO departments (department_Name) VALUES (?)", (department_Name ))
        conn.commit()
        print(" User added successfully.")
    except sqlite3.IntegrityError:
        print(" Email must be unique.")
    conn.close()

def view_departments():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM departments")
    rows = cursor.fetchall()
    conn.close()
    return rows

def search_departments(department_Name):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM departments WHERE department_Name  LIKE ?", ('%' + department_Name  + '%',))
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_departments(course_ID):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM departments WHERE id = ?", (course_ID,))
    conn.commit()
    conn.close()
    print("🗑️ User deleted.")
