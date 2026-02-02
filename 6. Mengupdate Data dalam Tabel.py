import sqlite3

def update_user_password(connection, username, new_password):
    cursor = connection.cursor()
    cursor.execute("UPDATE users SET password = ? WHERE username = ?", (new_password, username))
    connection.commit()

update_user_password(connection, "user1", "new_securepassword")
print("Password pengguna berhasil diperbarui.")
# Fungsi: Memperbarui password untuk pengguna tertentu.
# Kondisi: Ketika pengguna meminta untuk mengubah password mereka.