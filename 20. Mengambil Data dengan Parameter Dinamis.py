import sqlite3

def fetch_data_with_condition(connection, table_name, column, value):
    cursor = connection.cursor()
    query = f"SELECT * FROM {table_name} WHERE {column} = ?"
    cursor.execute(query, (value,))
    return cursor.fetchall()

fetched_data = fetch_data_with_condition(new_db_connection, "products", "name", "Widget")
print("Data yang diambil:")
for data in fetched_data:
    print(data)
# Fungsi: Mengambil data berdasarkan kondisi dinamis dari tabel.
# Kondisi: Ketika Anda ingin menggunakan query yang lebih fleksibel.