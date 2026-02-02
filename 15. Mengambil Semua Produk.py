import sqlite3

def fetch_all_products(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM products")
    return cursor.fetchall()

products = fetch_all_products(new_db_connection)
print("Data Produk:")
for product in products:
    print(product)
# Fungsi: Mengambil semua entri produk dari tabel.
# Kondisi: Ketika Anda ingin menampilkan atau mengelola data produk.