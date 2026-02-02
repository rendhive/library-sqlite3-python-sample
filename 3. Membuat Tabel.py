import sqlite3

def create_table(connection):
    cursor = connection.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    )
    """)
    connection.commit()

create_table(connection)
print("Tabel 'users' berhasil dibuat atau sudah ada.")
# Fungsi: Membuat tabel baru dalam database.
# Kondisi: Ketika Anda perlu mendefinisikan skema untuk menyimpan data.