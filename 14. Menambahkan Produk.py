import sqlite3

def add_product(connection, name, price):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO products (name, price) VALUES (?, ?)", (name, price))
    connection.commit()

add_product(new_db_connection, "Widget", 19.99)
print("Produk berhasil ditambahkan.")
# Fungsi: Menambahkan entri produk ke dalam tabel produk.
# Kondisi: Ketika Anda ingin mencatat informasi produk ke database.