import sqlite3

def add_user(connection, username, password):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    connection.commit()

add_user(connection, "user1", "securepassword")
print("Pengguna berhasil ditambahkan.")
# Fungsi: Menambahkan entri pengguna baru ke dalam tabel.
# Kondisi: Ketika Anda ingin menyimpan informasi pengguna baru.