import sqlite3

def create_connection(db_file):
    return sqlite3.connect(db_file)

connection = create_connection("example.db")
print("Koneksi ke database berhasil.")
# Fungsi: Membuat koneksi ke database SQLite baru atau yang sudah ada.
# Kondisi: Ketika Anda ingin mulai berinteraksi dengan database.