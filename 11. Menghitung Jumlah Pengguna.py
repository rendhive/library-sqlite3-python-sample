import sqlite3

def count_users(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM users")
    return cursor.fetchone()[0]

users_count = count_users(connection)
print(f"Jumlah pengguna: {users_count}")
# Fungsi: Menghitung jumlah total pengguna yang terdaftar.
# Kondisi: Ketika Anda ingin memantau jumlah pengguna dalam sistem.