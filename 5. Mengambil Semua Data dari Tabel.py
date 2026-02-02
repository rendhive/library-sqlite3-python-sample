import sqlite3

def fetch_all_users(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()

users = fetch_all_users(connection)
print("Data Pengguna:")
for user in users:
    print(user)
# Fungsi: Mengambil semua entri pengguna dari tabel.
# Kondisi: Ketika Anda ingin menampilkan atau memproses data pengguna.