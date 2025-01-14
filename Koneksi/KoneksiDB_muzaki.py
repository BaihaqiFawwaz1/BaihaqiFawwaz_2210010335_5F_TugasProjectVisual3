
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

    def fetch_all(self, muzaki):
        self.cursor.execute("SELECT * FROM muzaki")
        data = self.cursor.fetchall()
        headers = [desc[0] for desc in self.cursor.description]
        return data, headers

    def fetch_allPDF(self, muzaki):
        try:
            self.cursor.execute("SELECT * FROM muzaki")
            results = self.cursor.fetchall()
            print("Results fetched:", results)  # Tambahkan ini untuk debugging
            return results
        except pymysql.connector.Error as err:
            print(f"Kesalahan saat mengambil data: {err}")
            return []

    def tambah_Muzaki(self, kd_muzaki, nama_muzaki, tempat, tgl_lahir, alamatlengkap, jk, nik, pekerjaan, status, penghasilan, telp, email):
        self.cursor.execute("INSERT INTO muzaki (kd_muzaki, nama_muzaki, tempat, tgl_lahir, alamatlengkap, jk, nik, pekerjaan, status, penghasilan, telp, email) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (kd_muzaki, nama_muzaki, tempat, tgl_lahir, alamatlengkap, jk, nik, pekerjaan, status, penghasilan, telp, email))
        self.connection.commit()

    def ubah_Muzaki(self, kd_muzaki, nama_muzaki, tempat, tgl_lahir, alamatlengkap, jk, nik, pekerjaan, status, penghasilan, telp, email):
        self.cursor.execute("UPDATE muzaki SET nama_muzaki = %s, tempat = %s, tgl_lahir = %s, alamatlengkap = %s, jk = %s, nik = %s, pekerjaan = %s, status = %s, penghasilan = %s, telp = %s, email = %s WHERE kd_muzaki = %s",(  nama_muzaki, tempat, tgl_lahir, alamatlengkap, jk, nik, pekerjaan, status, penghasilan, telp, email, kd_muzaki))
        self.connection.commit()

    def hapus_Muzaki(self, kd_muzaki  ):
        self.cursor.execute("DELETE FROM muzaki WHERE kd_muzaki   = %s", (kd_muzaki  ))
        self.connection.commit()

    def close(self):
        self.connection.close()


