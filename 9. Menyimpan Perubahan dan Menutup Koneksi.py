import sqlite3

def close_connection(connection):
    connection.close()
    print("Koneksi ke database ditutup.")

close_connection(connection)
# Fungsi: Menutup koneksi ke database setelah selesai.
# Kondisi: Ketika Anda telah menyelesaikan semua operasi database.