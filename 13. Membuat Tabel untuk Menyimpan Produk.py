import sqlite3

def create_products_table(connection):
    cursor = connection.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        price REAL NOT NULL
    )
    """)
    connection.commit()

create_products_table(new_db_connection)
print("Tabel 'products' berhasil dibuat.")
# Fungsi: Membuat tabel produk dalam database.
# Kondisi: Ketika Anda perlu menyimpan informasi produk untuk aplikasi.