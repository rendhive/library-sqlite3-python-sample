import sqlite3

def update_product_price(connection, product_name, new_price):
    cursor = connection.cursor()
    cursor.execute("UPDATE products SET price = ? WHERE name = ?", (new_price, product_name))
    connection.commit()

update_product_price(new_db_connection, "Widget", 29.99)
print("Harga produk berhasil diperbarui.")
# Fungsi: Memperbarui harga produk dalam tabel.
# Kondisi: Ketika harga produk berubah dan perlu diperbarui di database.