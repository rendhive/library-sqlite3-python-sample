import sqlite3

def delete_product(connection, product_name):
    cursor = connection.cursor()
    cursor.execute("DELETE FROM products WHERE name = ?", (product_name,))
    connection.commit()

delete_product(new_db_connection, "Widget")
print("Produk berhasil dihapus.")
# Fungsi: Menghapus entri produk dari tabel produk berdasarkan nama.
# Kondisi: Ketika produk tidak lagi dijual atau diperlukan.