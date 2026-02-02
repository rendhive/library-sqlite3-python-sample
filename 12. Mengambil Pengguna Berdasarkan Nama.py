import sqlite3

def fetch_user_by_username(connection, username):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    return cursor.fetchone()

user = fetch_user_by_username(connection, "user1")
if user:
    print(f"Data Pengguna: {user}")
else:
    print("Pengguna tidak ditemukan.")
# Fungsi: Mengambil entri pengguna berdasarkan nama pengguna.
# Kondisi: Ketika Anda perlu mengambil informasi spesifik tentang seorang pengguna.