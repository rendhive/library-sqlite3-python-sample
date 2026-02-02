import sqlite3

def transfer_product_price(connection, from_product, to_product):
    try:
        cursor = connection.cursor()
        cursor.execute("BEGIN")
        cursor.execute("SELECT price FROM products WHERE name = ?", (from_product,))
        price = cursor.fetchone()[0]
        cursor.execute("UPDATE products SET price = price - ? WHERE name = ?", (price, from_product))
        cursor.execute("UPDATE products SET price = price + ? WHERE name = ?", (price, to_product))
        connection.commit()
    except Exception as e:
        connection.rollback()
        print(f"Transaksi gagal: {e}")

# Panggil fungsi ini untuk mentransfer harga antar produk jika produk ada.
# Fungsi: Mengubah harga produk melalui transaksi yang aman.
# Kondisi: Ketika Anda memerlukan operasi atomik untuk menghindari inkonsistensi data.