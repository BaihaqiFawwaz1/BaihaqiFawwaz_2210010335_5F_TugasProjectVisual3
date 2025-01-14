from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QMessageBox
from Koneksi.KoneksiDB_muzaki import KoneksiDB
from Model.model_muzaki import TableModel
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


class formMuzaki(QWidget):
    def __init__(self):
        super().__init__()

        # Memuat file .ui
        uic.loadUi("muzaki.ui", self)

        # Instance KoneksiDB
        self.koneksiDB = KoneksiDB()

        # Memuat data awal
        self.load_data()

        # Menyambungkan fungsi ke tombol
        self.btnSimpan.clicked.connect(self.add_data)
        self.btnUbah.clicked.connect(self.update_data)
        self.btnHapus.clicked.connect(self.delete_data)
        self.tabel_Muzaki.clicked.connect(self.on_table_click)
        self.btnCetak.clicked.connect(self.print_pdf)

    def load_data(self):
        """
        Memuat data dari database dan menampilkan di tabel.
        """
        try:
            data, headers = self.koneksiDB.fetch_all("muzaki")
            self.model = TableModel(data, headers)
            self.tabel_Muzaki.setModel(self.model)
        except Exception as e:
            QMessageBox.critical(self, "Kesalahan", f"Kesalahan saat memuat data: {e}")
            self.model = None

    def add_data(self):
        """
        Menambahkan data baru ke database.
        """
        kd_muzaki  = self.edit_kd_muzaki.text()
        nama_muzaki = self.edit_nama_muzaki.text()
        tempat = self.edit_tempat.text()
        tgl_lahir = self.edit_tgl_lahir.text()
        alamatlengkap = self.edit_alamatlengkap.text()
        jk = self.edit_jk.text()
        nik = self.edit_nik.text()
        pekerjaan = self.edit_pekerjaan.text()
        status = self.edit_status.text()
        penghasilan = self.edit_penghasilan.text()
        telp = self.edit_telp.text()
        email = self.edit_email.text()

        if all([kd_muzaki, nama_muzaki, tempat, tgl_lahir, alamatlengkap, jk, nik, pekerjaan, status, penghasilan, telp, email]):
            try:
                self.koneksiDB.tambah_Muzaki(
                    kd_muzaki, nama_muzaki, tempat, tgl_lahir, alamatlengkap, jk, nik, pekerjaan, status, penghasilan, telp, email
                )
                QMessageBox.information(self, "Sukses", "Data berhasil ditambahkan.")
                self.clear_inputs()
                self.load_data()
            except Exception as e:
                QMessageBox.critical(self, "Kesalahan", f"Kesalahan saat menambahkan data: {e}")
        else:
            QMessageBox.warning(self, "Peringatan", "Semua input harus diisi.")

    def update_data(self):
        """
        Mengupdate data yang dipilih di database.
        """
        kd_muzaki = self.edit_kd_muzaki.text()
        nama_muzaki = self.edit_nama_muzaki.text()
        tempat = self.edit_tempat.text()
        tgl_lahir = self.edit_tgl_lahir.text()
        alamatlengkap = self.edit_alamatlengkap.text()
        jk = self.edit_jk.text()
        nik = self.edit_nik.text()
        pekerjaan = self.edit_pekerjaan.text()
        status = self.edit_status.text()
        penghasilan = self.edit_penghasilan.text()
        telp = self.edit_telp.text()
        email = self.edit_email.text()

        if all([kd_muzaki, nama_muzaki, tempat, tgl_lahir, alamatlengkap, jk, nik, pekerjaan, status, penghasilan, telp, email]):
            try:
                self.koneksiDB.ubah_Muzaki(
                    kd_muzaki, nama_muzaki, tempat, tgl_lahir, alamatlengkap, jk, nik, pekerjaan, status, penghasilan, telp, email
                )
                QMessageBox.information(self, "Sukses", "Data berhasil diubah.")
                self.clear_inputs()
                self.load_data()
            except Exception as e:
                QMessageBox.critical(self, "Kesalahan", f"Kesalahan saat mengubah data: {e}")
        else:
            QMessageBox.warning(self, "Peringatan", "Semua input harus diisi.")

    def delete_data(self):
        """
        Menghapus data yang dipilih di database.
        """
        kd_muzaki = self.edit_kd_muzaki.text()
        if kd_muzaki:
            try:
                self.koneksiDB.hapus_Muzaki(kd_muzaki)
                QMessageBox.information(self, "Sukses", "Data berhasil dihapus.")
                self.clear_inputs()
                self.load_data()
            except Exception as e:
                QMessageBox.critical(self, "Kesalahan", f"Kesalahan saat menghapus data: {e}")
        else:
            QMessageBox.warning(self, "Peringatan", "Kode muzaki harus diisi.")

    def clear_inputs(self):
        """
        Membersihkan semua input field.
        """
        self.edit_kd_muzaki.clear()
        self.edit_nama_muzaki.clear()
        self.edit_tempat.clear()
        self.edit_tgl_lahir.clear()
        self.edit_alamatlengkap.clear()
        self.edit_jk.clear()
        self.edit_nik.clear()
        self.edit_pekerjaan.clear()
        self.edit_status.clear()
        self.edit_penghasilan.clear()
        self.edit_telp.clear()
        self.edit_email.clear()

    def on_table_click(self, index):
        """
        Menangani event klik pada tabel untuk mengambil data baris tertentu.
        """
        try:
            row = index.row()
            if row < 0 or row >= len(self.model._data):
                raise ValueError("Indeks baris tidak valid.")

            record = self.model._data[row]
            if len(record) < 12:
                raise ValueError("Data baris tidak lengkap.")

            self.edit_kd_muzaki.setText(str(record[0]))
            self.edit_nama_muzaki.setText(str(record[1]))
            self.edit_tempat.setText(str(record[2]))
            self.edit_tgl_lahir.setText(str(record[3]))
            self.edit_alamatlengkap.setText(str(record[4]))
            self.edit_jk.setText(str(record[5]))
            self.edit_nik.setText(str(record[6]))
            self.edit_pekerjaan.setText(str(record[7]))
            self.edit_status.setText(str(record[8]))
            self.edit_penghasilan.setText(str(record[9]))
            self.edit_telp.setText(str(record[10]))
            self.edit_email.setText(str(record[11]))
        except Exception as e:
            QMessageBox.warning(self, "Kesalahan", f"Kesalahan saat memilih data: {e}")

    def print_pdf(self):
        """
        Mencetak data ke PDF dari database.
        """
        try:
            data = self.koneksiDB.fetch_allPDF("muzaki")
            if not data:
                QMessageBox.warning(self, "Data Kosong", "Tidak ada data untuk dicetak.")
                return

            pdf_file = "muzaki_report.pdf"
            c = canvas.Canvas(pdf_file, pagesize=letter)
            width, height = letter

            # Header PDF
            c.setFont("Helvetica-Bold", 14)
            c.drawString(50, height - 40, "Laporan Data Mustahik")

            # Header tabel
            col_widths = [60, 150, 100, 80, 80, 80]
            headers = ["kd_muzaki, nama_muzaki, tempat, tgl_lahir, alamatlengkap, jk, nik, pekerjaan, status, penghasilan, telp, email"]

            y_position = height - 60
            for header, col_width in zip(headers, col_widths):
                c.drawString(50, y_position, header)
                y_position -= 20

            # Isi tabel
            for row in data:
                x_position = 50
                for cell, col_width in zip(row, col_widths):
                    c.drawString(x_position, y_position, str(cell))
                    x_position += col_width
                y_position -= 20

            c.save()
            QMessageBox.information(self, "Sukses", f"PDF berhasil disimpan: {pdf_file}")
        except Exception as e:
            QMessageBox.critical(self, "Kesalahan", f"Kesalahan saat mencetak PDF: {e}")

    def closeEvent(self, event):
        """
        Menutup koneksi database saat aplikasi ditutup.
        """
        self.koneksiDB.close()
        event.accept()
