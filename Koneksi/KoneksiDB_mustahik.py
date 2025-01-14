
import pymysql
from mysql.connector import Error

class KoneksiDB:
    def __init__(self):
        try:
            self.connection = pymysql.connect(
                host='localhost',
                user='root',  # Ganti dengan username MySQL Anda
                password='',  # Ganti dengan password MySQL Anda
                database='_2210010335_agama'  # Ganti dengan nama database Anda
            )

            # Memastikan koneksi berhasil
            if self.connection.open:
                print("Koneksi berhasil")
                self.cursor = self.connection.cursor()
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")

    def fetch_all(self, mustahik):
        self.cursor.execute("SELECT * FROM mustahik")
        data = self.cursor.fetchall()
        headers = [desc[0] for desc in self.cursor.description]
        return data, headers

    def fetch_allPDF(self, mustahik):
        try:
            self.cursor.execute("SELECT * FROM mustahik")
            results = self.cursor.fetchall()
            print("Results fetched:", results)  # Tambahkan ini untuk debugging
            return results
        except pymysql.connector.Error as err:
            print(f"Kesalahan saat mengambil data: {err}")
            return []

    def tambah_Mustahik(self, kd_mustahik, nama_mustahik, nik, tempat, tgl_lahir, alamat, jk, golongan):
        self.cursor.execute("INSERT INTO mustahik (kd_mustahik, nama_mustahik, nik, tempat, tgl_lahir, alamat, jk, golongan) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (kd_mustahik, nama_mustahik, nik, tempat, tgl_lahir, alamat, jk, golongan))
        self.connection.commit()

    def ubah_Mustahik(self, kd_mustahik, nama_mustahik, nik, tempat, tgl_lahir, alamat, jk, golongan):
        self.cursor.execute("UPDATE mustahik SET nama_mustahik = %s, nik = %s, tempat = %s, tgl_lahir = %s, alamat = %s, jk = %s, golongan = %s WHERE kd_mustahik = %s",( nama_mustahik, nik, tempat, tgl_lahir, alamat, jk, golongan, kd_mustahik))
        self.connection.commit()

    def hapus_Mustahik(self, kd_mustahik ):
        self.cursor.execute("DELETE FROM mustahik WHERE kd_mustahik  = %s", (kd_mustahik ))
        self.connection.commit()

    def close(self):
        self.connection.close()


