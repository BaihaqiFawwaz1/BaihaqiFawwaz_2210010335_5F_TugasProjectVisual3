
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

    def fetch_all(self, zakat):
        self.cursor.execute("SELECT * FROM zakat")
        data = self.cursor.fetchall()
        headers = [desc[0] for desc in self.cursor.description]
        return data, headers

    def fetch_allPDF(self, zakat):
        try:
            self.cursor.execute("SELECT * FROM zakat")
            results = self.cursor.fetchall()
            print("Results fetched:", results)  # Tambahkan ini untuk debugging
            return results
        except pymysql.connector.Error as err:
            print(f"Kesalahan saat mengambil data: {err}")
            return []

    def tambah_Zakat(self, kd_zakat , nama_zakat, bentuk, saldo, keterangan):
        self.cursor.execute("INSERT INTO zakat (kd_zakat , nama_zakat, bentuk, saldo, keterangan) VALUES (%s, %s, %s, %s, %s)", (kd_zakat , nama_zakat, bentuk, saldo, keterangan))
        self.connection.commit()

    def ubah_Zakat(self, kd_zakat , nama_zakat, bentuk, saldo, keterangan):
        self.cursor.execute("UPDATE zakat SET nama_zakat = %s, bentuk = %s, saldo = %s, keterangan = %s WHERE kd_zakat = %s",(  nama_zakat, bentuk, saldo, keterangan, kd_zakat))
        self.connection.commit()

    def hapus_Zakat(self, kd_zakat ):
        self.cursor.execute("DELETE FROM zakat WHERE kd_zakat  = %s", (kd_zakat ))
        self.connection.commit()

    def close(self):
        self.connection.close()


