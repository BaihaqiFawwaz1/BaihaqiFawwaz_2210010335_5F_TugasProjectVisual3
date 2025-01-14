
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

    def fetch_all(self, zakatmasuk):
        self.cursor.execute("SELECT * FROM zakatmasuk")
        data = self.cursor.fetchall()
        headers = [desc[0] for desc in self.cursor.description]
        return data, headers

    def fetch_allPDF(self, zakatmasuk):
        try:
            self.cursor.execute("SELECT * FROM zakatmasuk")
            results = self.cursor.fetchall()
            print("Results fetched:", results)  # Tambahkan ini untuk debugging
            return results
        except pymysql.connector.Error as err:
            print(f"Kesalahan saat mengambil data: {err}")
            return []

    def tambah_Zakatmasuk(self, no_masuk, kd_zakat, kd_muzaki, jmlh_masuk, bentuk, tgl_masuk, norek, ket, status):
        self.cursor.execute("INSERT INTO zakatmasuk (no_masuk, kd_zakat, kd_muzaki, jmlh_masuk, bentuk, tgl_masuk, norek, ket, status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (no_masuk, kd_zakat, kd_muzaki, jmlh_masuk, bentuk, tgl_masuk, norek, ket, status))
        self.connection.commit()

    def ubah_Zakatmasuk(self, no_masuk, kd_zakat, kd_muzaki, jmlh_masuk, bentuk, tgl_masuk, norek, ket, status):
        self.cursor.execute("UPDATE zakatmasuk SET kd_zakat = %s, kd_muzaki = %s, jmlh_masuk = %s, bentuk = %s, tgl_masuk = %s, norek = %s, ket = %s, status = %s WHERE no_masuk = %s",( kd_zakat, kd_muzaki, jmlh_masuk, bentuk, tgl_masuk, norek, ket, status, no_masuk))
        self.connection.commit()

    def hapus_Zakatmasuk(self, no_masuk ):
        self.cursor.execute("DELETE FROM zakatmasuk WHERE no_masuk  = %s", (no_masuk ))
        self.connection.commit()

    def close(self):
        self.connection.close()


