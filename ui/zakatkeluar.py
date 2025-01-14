from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QMessageBox
from Koneksi.KoneksiDB_zakatkeluar import KoneksiDB
from Model.model_zakatkeluar import TableModel
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


class formZakatkeluar(QWidget):
    def __init__(self):
        super().__init__()

        # Memuat file .ui
        uic.loadUi("zakatkeluar.ui", self)

        # Instance KoneksiDB
        self.koneksiDB = KoneksiDB()

        # Memuat data awal
        self.load_data()

        # Menyambungkan fungsi ke tombol
        self.btnSimpan.clicked.connect(self.add_data)
        self.btnUbah.clicked.connect(self.update_data)
        self.btnHapus.clicked.connect(self.delete_data)
        self.tabel_Zakatkeluar.clicked.connect(self.on_table_click)
        self.btnCetak.clicked.connect(self.print_pdf)

    def load_data(self):
        """
        Memuat data dari database dan menampilkan di tabel.
        """
        try:
            data, headers = self.koneksiDB.fetch_all("zakatkeluar")
            self.model = TableModel(data, headers)
            self.tabel_Zakatkeluar.setModel(self.model)
        except Exception as e:
            QMessageBox.critical(self, "Kesalahan", f"Kesalahan saat memuat data: {e}")
            self.model = None

    def add_data(self):
        """
        Menambahkan data baru ke database.
        """
        no_keluar = self.edit_no_keluar.text()
        kd_zakat = self.edit_kd_zakat.text()
        kd_mustahik = self.edit_kd_mustahik.text()
        jmlh_keluar = self.edit_jmlh_keluar.text()
        bentuk = self.edit_bentuk.text()
        tgl_masuk = self.edit_tgl_masuk.text()
        ket = self.edit_ket.text()

        if all([no_keluar, kd_zakat, kd_mustahik, jmlh_keluar, bentuk, tgl_masuk, ket]):
            try:
                self.koneksiDB.tambah_Zakatkeluar(
                    no_keluar, kd_zakat, kd_mustahik, jmlh_keluar, bentuk, tgl_masuk, ket
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
        no_keluar = self.edit_no_keluar.text()
        kd_zakat = self.edit_kd_zakat.text()
        kd_mustahik = self.edit_kd_mustahik.text()
        jmlh_keluar = self.edit_jmlh_keluar.text()
        bentuk = self.edit_bentuk.text()
        tgl_masuk = self.edit_tgl_masuk.text()
        ket = self.edit_ket.text()

        if all([no_keluar, kd_zakat, kd_mustahik, jmlh_keluar, bentuk, tgl_masuk, ket]):
            try:
                self.koneksiDB.ubah_Zakatkeluar(
                    no_keluar, kd_zakat, kd_mustahik, jmlh_keluar, bentuk, tgl_masuk, ket
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
        no_keluar = self.edit_no_keluar.text()
        if no_keluar:
            try:
                self.koneksiDB.hapus_Zakatkeluar(no_keluar)
                QMessageBox.information(self, "Sukses", "Data berhasil dihapus.")
                self.clear_inputs()
                self.load_data()
            except Exception as e:
                QMessageBox.critical(self, "Kesalahan", f"Kesalahan saat menghapus data: {e}")
        else:
            QMessageBox.warning(self, "Peringatan", "Kode zakatkeluar harus diisi.")

    def clear_inputs(self):
        """
        Membersihkan semua input field.
        """
        self.edit_no_keluar.clear()
        self.edit_kd_zakat.clear()
        self.edit_kd_mustahik.clear()
        self.edit_jmlh_keluar.clear()
        self.edit_bentuk.clear()
        self.edit_tgl_masuk.clear()
        self.edit_ket.clear()

    def on_table_click(self, index):
        """
        Menangani event klik pada tabel untuk mengambil data baris tertentu.
        """
        try:
            row = index.row()
            if row < 0 or row >= len(self.model._data):
                raise ValueError("Indeks baris tidak valid.")

            record = self.model._data[row]
            if len(record) < 7:
                raise ValueError("Data baris tidak lengkap.")

            self.edit_no_keluar.setText(str(record[0]))
            self.edit_kd_zakat.setText(str(record[1]))
            self.edit_kd_mustahik.setText(str(record[2]))
            self.edit_jmlh_keluar.setText(str(record[3]))
            self.edit_bentuk.setText(str(record[4]))
            self.edit_tgl_masuk.setText(str(record[5]))
            self.edit_ket.setText(str(record[6]))
        except Exception as e:
            QMessageBox.warning(self, "Kesalahan", f"Kesalahan saat memilih data: {e}")

    def print_pdf(self):
        """
        Mencetak data ke PDF dari database.
        """
        try:
            data = self.koneksiDB.fetch_allPDF("zakatkeluar")
            if not data:
                QMessageBox.warning(self, "Data Kosong", "Tidak ada data untuk dicetak.")
                return

            pdf_file = "zakatkeluar_report.pdf"
            c = canvas.Canvas(pdf_file, pagesize=letter)
            width, height = letter

            # Header PDF
            c.setFont("Helvetica-Bold", 14)
            c.drawString(50, height - 40, "Laporan Data Zakatkeluar")

            # Header tabel
            col_widths = [60, 150, 100, 80, 80, 80]
            headers = ["no_keluar", "kd_zakat", "kd_mustahik", "jmlh_keluar", "bentuk", "tgl_masuk", "ket"]

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
