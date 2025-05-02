import sqlite3

def create_tables():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Festivals (
        festival_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        date DATE NOT NULL
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Customs (
        custom_id INTEGER PRIMARY KEY,
        festival_id INTEGER,
        description TEXT NOT NULL,
        FOREIGN KEY (festival_id) REFERENCES Festivals(festival_id)
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS UserPreferences (
        user_id INTEGER,
        festival_id INTEGER,
        custom_id INTEGER,
        FOREIGN KEY (festival_id) REFERENCES Festivals(festival_id),
        FOREIGN KEY (custom_id) REFERENCES Customs(custom_id)
    )
    ''')
    
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_tables()