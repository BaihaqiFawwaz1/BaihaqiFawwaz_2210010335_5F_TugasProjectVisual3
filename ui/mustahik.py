from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QMessageBox
from Koneksi.KoneksiDB_mustahik import KoneksiDB
from Model.model_mustahik import TableModel
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


class formMustahik(QWidget):
    def __init__(self):
        super().__init__()

        # Memuat file .ui
        uic.loadUi("mustahik.ui", self)

        # Instance KoneksiDB
        self.koneksiDB = KoneksiDB()

        # Memuat data awal
        self.load_data()

        # Menyambungkan fungsi ke tombol
        self.btnSimpan.clicked.connect(self.add_data)
        self.btnUbah.clicked.connect(self.update_data)
        self.btnHapus.clicked.connect(self.delete_data)
        self.tabel_Mustahik.clicked.connect(self.on_table_click)
        self.btnCetak.clicked.connect(self.print_pdf)

    def load_data(self):
        """
        Memuat data dari database dan menampilkan di tabel.
        """
        try:
            data, headers = self.koneksiDB.fetch_all("mustahik")
            self.model = TableModel(data, headers)
            self.tabel_Mustahik.setModel(self.model)
        except Exception as e:
            QMessageBox.critical(self, "Kesalahan", f"Kesalahan saat memuat data: {e}")
            self.model = None

    def add_data(self):
        """
        Menambahkan data baru ke database.
        """
        kd_mustahik = self.edit_kd_mustahik.text()
        nama_mustahik = self.edit_nama_mustahik.text()
        nik = self.edit_nik.text()
        tempat = self.edit_tempat.text()
        tgl_lahir = self.edit_tgl_lahir.text()
        alamat = self.edit_alamat.text()
        jk = self.edit_jk.text()
        golongan = self.edit_golongan.text()

        if all([kd_mustahik, nama_mustahik, nik, tempat, tgl_lahir, alamat, jk, golongan]):
            try:
                self.koneksiDB.tambah_Mustahik(
                    kd_mustahik, nama_mustahik, nik, tempat, tgl_lahir, alamat, jk, golongan
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
        kd_mustahik = self.edit_kd_mustahik.text()
        nama_mustahik = self.edit_nama_mustahik.text()
        nik = self.edit_nik.text()
        tempat = self.edit_tempat.text()
        tgl_lahir = self.edit_tgl_lahir.text()
        alamat = self.edit_alamat.text()
        jk = self.edit_jk.text()
        golongan = self.edit_golongan.text()

        if all([kd_mustahik, nama_mustahik, nik, tempat, tgl_lahir, alamat, jk, golongan]):
            try:
                self.koneksiDB.ubah_Mustahik(
                    kd_mustahik, nama_mustahik, nik, tempat, tgl_lahir, alamat, jk, golongan
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
        kd_mustahik = self.edit_kd_mustahik.text()
        if kd_mustahik:
            try:
                self.koneksiDB.hapus_Mustahik(kd_mustahik)
                QMessageBox.information(self, "Sukses", "Data berhasil dihapus.")
                self.clear_inputs()
                self.load_data()
            except Exception as e:
                QMessageBox.critical(self, "Kesalahan", f"Kesalahan saat menghapus data: {e}")
        else:
            QMessageBox.warning(self, "Peringatan", "Kode mustahik harus diisi.")

    def clear_inputs(self):
        """
        Membersihkan semua input field.
        """
        self.edit_kd_mustahik.clear()
        self.edit_nama_mustahik.clear()
        self.edit_nik.clear()
        self.edit_tempat.clear()
        self.edit_tgl_lahir.clear()
        self.edit_alamat.clear()
        self.edit_jk.clear()
        self.edit_golongan.clear()

    def on_table_click(self, index):
        """
        Menangani event klik pada tabel untuk mengambil data baris tertentu.
        """
        try:
            row = index.row()
            if row < 0 or row >= len(self.model._data):
                raise ValueError("Indeks baris tidak valid.")

            record = self.model._data[row]
            if len(record) < 8:
                raise ValueError("Data baris tidak lengkap.")

            self.edit_kd_mustahik.setText(str(record[0]))
            self.edit_nama_mustahik.setText(str(record[1]))
            self.edit_nik.setText(str(record[2]))
            self.edit_tempat.setText(str(record[3]))
            self.edit_tgl_lahir.setText(str(record[4]))
            self.edit_alamat.setText(str(record[5]))
            self.edit_jk.setText(str(record[6]))
            self.edit_golongan.setText(str(record[7]))
        except Exception as e:
            QMessageBox.warning(self, "Kesalahan", f"Kesalahan saat memilih data: {e}")

    def print_pdf(self):
        """
        Mencetak data ke PDF dari database.
        """
        try:
            data = self.koneksiDB.fetch_allPDF("mustahik")
            if not data:
                QMessageBox.warning(self, "Data Kosong", "Tidak ada data untuk dicetak.")
                return

            pdf_file = "mustahik_report.pdf"
            c = canvas.Canvas(pdf_file, pagesize=letter)
            width, height = letter

            # Header PDF
            c.setFont("Helvetica-Bold", 14)
            c.drawString(50, height - 40, "Laporan Data Mustahik")

            # Header tabel
            col_widths = [60, 150, 100, 80, 80, 80]
            headers = ["kd_mustahik", "nama_mustahik", "nik", "tempat", "tgl_lahir", "alamat", "jk", "golongan"]

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
