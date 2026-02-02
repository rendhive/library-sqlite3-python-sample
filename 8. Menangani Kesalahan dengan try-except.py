import sqlite3

def safe_add_user(connection, username, password):
    try:
        add_user(connection, username, password)
    except sqlite3.IntegrityError:
        print("Pengguna sudah ada.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

safe_add_user(connection, "user1", "password123")
# Fungsi: Menggunakan `try-except` untuk menangani potensi kesalahan saat menambahkan pengguna.
# Kondisi: Ketika Anda ingin mencegah kesalahan saat memasukkan data.