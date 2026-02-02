import sqlite3

def fetch_items_above_price(connection, min_price):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM products WHERE price > ?", (min_price,))
    return cursor.fetchall()

items = fetch_items_above_price(new_db_connection, 10.00)
print("Produk di atas harga 10.00:")
for item in items:
    print(item)
# Fungsi: Mengambil produk yang harga di atas nilai tertentu.
# Kondisi: Ketika Anda ingin mendapatkan daftar produk berdasarkan harga.