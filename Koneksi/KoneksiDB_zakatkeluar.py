
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

    def fetch_all(self, zakatkeluar):
        self.cursor.execute("SELECT * FROM zakatkeluar")
        data = self.cursor.fetchall()
        headers = [desc[0] for desc in self.cursor.description]
        return data, headers

    def fetch_allPDF(self, zakatkeluar):
        try:
            self.cursor.execute("SELECT * FROM zakatkeluar")
            results = self.cursor.fetchall()
            print("Results fetched:", results)  # Tambahkan ini untuk debugging
            return results
        except pymysql.connector.Error as err:
            print(f"Kesalahan saat mengambil data: {err}")
            return []

    def tambah_Zakatkeluar(self, no_keluar, kd_zakat, kd_mustahik, jmlh_keluar, bentuk, tgl_masuk, ket):
        self.cursor.execute("INSERT INTO zakatkeluar (no_keluar, kd_zakat, kd_mustahik, jmlh_keluar, bentuk, tgl_masuk, ket) VALUES (%s, %s, %s, %s, %s, %s, %s)", (no_keluar, kd_zakat, kd_mustahik, jmlh_keluar, bentuk, tgl_masuk, ket))
        self.connection.commit()

    def ubah_Zakatkeluar(self, no_keluar, kd_zakat, kd_mustahik, jmlh_keluar, bentuk, tgl_masuk, ket):
        self.cursor.execute("UPDATE zakatkeluar SET kd_zakat = %s, kd_mustahik = %s, jmlh_keluar = %s, bentuk = %s, tgl_masuk = %s, ket = %s WHERE no_keluar = %s",( kd_zakat, kd_mustahik, jmlh_keluar, bentuk, tgl_masuk, ket, no_keluar))
        self.connection.commit()

    def hapus_Zakatkeluar(self, no_keluar  ):
        self.cursor.execute("DELETE FROM zakatkeluar WHERE no_keluar   = %s", (no_keluar  ))
        self.connection.commit()

    def close(self):
        self.connection.close()


