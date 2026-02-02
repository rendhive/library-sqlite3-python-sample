import sqlite3

def delete_user(connection, username):
    cursor = connection.cursor()
    cursor.execute("DELETE FROM users WHERE username = ?", (username,))
    connection.commit()

delete_user(connection, "user1")
print("Pengguna berhasil dihapus.")
# Fungsi: Menghapus entri pengguna dari tabel berdasarkan username.
# Kondisi: Ketika Anda perlu menghapus akun pengguna dari database.