from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QMessageBox
from Koneksi.KoneksiDB_zakat import KoneksiDB
from Model.model_zakat import TableModel
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


class formZakat(QWidget):
    def __init__(self):
        super().__init__()

        # Memuat file .ui
        uic.loadUi("zakat.ui", self)

        # Instance KoneksiDB
        self.koneksiDB = KoneksiDB()

        # Memuat data awal
        self.load_data()

        # Menyambungkan fungsi ke tombol
        self.btnSimpan.clicked.connect(self.add_data)
        self.btnUbah.clicked.connect(self.update_data)
        self.btnHapus.clicked.connect(self.delete_data)
        self.tabel_Zakat.clicked.connect(self.on_table_click)
        self.btnCetak.clicked.connect(self.print_pdf)

    def load_data(self):
        """
        Memuat data dari database dan menampilkan di tabel.
        """
        try:
            data, headers = self.koneksiDB.fetch_all("zakat")
            self.model = TableModel(data, headers)
            self.tabel_Zakat.setModel(self.model)
        except Exception as e:
            QMessageBox.critical(self, "Kesalahan", f"Kesalahan saat memuat data: {e}")
            self.model = None

    def add_data(self):
        """
        Menambahkan data baru ke database.
        """
        kd_zakat  = self.edit_kd_zakat.text()
        nama_zakat = self.edit_nama_zakat.text()
        bentuk = self.edit_bentuk.text()
        saldo = self.edit_saldo.text()
        keterangan = self.edit_keterangan.text()

        if all([kd_zakat , nama_zakat, bentuk, saldo, keterangan]):
            try:
                self.koneksiDB.tambah_Zakat(
                    kd_zakat , nama_zakat, bentuk, saldo, keterangan
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
        kd_zakat = self.edit_kd_zakat.text()
        nama_zakat = self.edit_nama_zakat.text()
        bentuk = self.edit_bentuk.text()
        saldo = self.edit_saldo.text()
        keterangan = self.edit_keterangan.text()

        if all([kd_zakat , nama_zakat, bentuk, saldo, keterangan]):
            try:
                self.koneksiDB.ubah_Zakat(
                    kd_zakat , nama_zakat, bentuk, saldo, keterangan
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
        kd_zakat = self.edit_kd_zakat.text()
        if kd_zakat:
            try:
                self.koneksiDB.hapus_Zakat(kd_zakat)
                QMessageBox.information(self, "Sukses", "Data berhasil dihapus.")
                self.clear_inputs()
                self.load_data()
            except Exception as e:
                QMessageBox.critical(self, "Kesalahan", f"Kesalahan saat menghapus data: {e}")
        else:
            QMessageBox.warning(self, "Peringatan", "Kode zakat harus diisi.")

    def clear_inputs(self):
        """
        Membersihkan semua input field.
        """
        self.edit_kd_zakat.clear()
        self.edit_nama_zakat.clear()
        self.edit_bentuk.clear()
        self.edit_saldo.clear()
        self.edit_keterangan.clear()

    def on_table_click(self, index):
        """
        Menangani event klik pada tabel untuk mengambil data baris tertentu.
        """
        try:
            row = index.row()
            if row < 0 or row >= len(self.model._data):
                raise ValueError("Indeks baris tidak valid.")

            record = self.model._data[row]
            if len(record) < 5:
                raise ValueError("Data baris tidak lengkap.")

            self.edit_kd_zakat.setText(str(record[0]))
            self.edit_nama_zakat.setText(str(record[1]))
            self.edit_bentuk.setText(str(record[2]))
            self.edit_saldo.setText(str(record[3]))
            self.edit_keterangan.setText(str(record[4]))
        except Exception as e:
            QMessageBox.warning(self, "Kesalahan", f"Kesalahan saat memilih data: {e}")

    def print_pdf(self):
        """
        Mencetak data ke PDF dari database.
        """
        try:
            data = self.koneksiDB.fetch_allPDF("zakat")
            if not data:
                QMessageBox.warning(self, "Data Kosong", "Tidak ada data untuk dicetak.")
                return

            pdf_file = "zakat_report.pdf"
            c = canvas.Canvas(pdf_file, pagesize=letter)
            width, height = letter

            # Header PDF
            c.setFont("Helvetica-Bold", 14)
            c.drawString(50, height - 40, "Laporan Data Zakat")

            # Header tabel
            col_widths = [60, 150, 100, 80, 80, 80]
            headers = ["kd_zakat", "nama_zakat", "bentuk", "saldo", "keterangan"]

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
