import sqlite3

def create_connection():
    conn = sqlite3.connect("yoobee.db")
    return conn

def create_student_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students(
            student_id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_name TEXT NOT NULL,
            student_email TEXT NOT NULL UNIQUE,
            phone TEXT NOT NULL, 
            address TEXT NOT NULL,
            department_ID INT NOT NULL, 
            course_ID INT NOT NULL,
            FOREIGN KEY (department_ID) REFERENCES departments(department_ID),
            FOREIGN KEY (course_ID) REFERENCES course(course_ID)
        )
    ''')
    conn.commit()
    conn.close()

def create_course_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS course(
                course_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                course_Name TEXT NOT NULL,
                duration TEXT NOT NULL,  
                department_ID INT NOT NULL,
                FOREIGN KEY (department_ID) REFERENCES departments(department_ID)
                )
             ''')
    conn.commit()
    conn.close()

def create_lectures_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS lecturers(
                lecturer_Id INTEGER PRIMARY KEY AUTOINCREMENT,
                lecturer_Name TEXT NOT NULL,
                lecturer_Email TEXT NOT NULL UNIQUE,
                department_ID INT NOT NULL, 
                course_ID INT NOT NULL,
                FOREIGN KEY (department_ID) REFERENCES departments(department_ID),
                FOREIGN KEY (course_ID) REFERENCES course(course_ID)
                )
            ''')
    conn.commit()
    conn.close()

def create_departments_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS departments(
                department_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                department_Name TEXT NOT NULL
                       )''')
    conn.commit()
    conn.close()

def create_subjects_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
              CREATE TABLE IF NOT EXISTS subjects(
                subject_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                subject_Name TEXT NOT NULL,
                course_ID INT NOT NULL,
                FOREIGN KEY(course_ID) REFERENCES course(course_ID)       
                       
                 )''')
    conn.commit()
    conn.close()