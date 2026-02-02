import sqlite3

def create_new_database(db_file):
    connection = sqlite3.connect(db_file)
    print(f"Database '{db_file}' berhasil dibuat.")
    return connection

new_db_connection = create_new_database("new_database.db")
close_connection(new_db_connection)
# Fungsi: Membuat database baru di sistem file.
# Kondisi: Ketika Anda ingin mulai dari awal dengan database baru.