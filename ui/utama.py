from PyQt6.QtWidgets import QWidget, QPushButton, QApplication
import sys

from PyQt6 import uic
from mustahik import formMustahik
from muzaki import formMuzaki
from zakat import formZakat
from zakatkeluar import formZakatkeluar
from zakatmasuk import formZakatmasuk


class formUtama(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('utama.ui',self)
        self.button_tampil_mustahik=self.findChild(QPushButton,"button_tampil_mustahik")
        self.button_tampil_mustahik.clicked.connect(self.tampil_mustahik)
        self.button_tampil_muzaki = self.findChild(QPushButton, "button_tampil_muzaki")
        self.button_tampil_muzaki.clicked.connect(self.tampil_muzaki)
        self.button_tampil_zakat = self.findChild(QPushButton, "button_tampil_zakat")
        self.button_tampil_zakat.clicked.connect(self.tampil_zakat)
        self.button_tampil_zakatkeluar = self.findChild(QPushButton, "button_tampil_zakatkeluar")
        self.button_tampil_zakatkeluar.clicked.connect(self.tampil_zakatkeluar)
        self.button_tampil_zakatmasuk = self.findChild(QPushButton, "button_tampil_zakatmasuk")
        self.button_tampil_zakatmasuk.clicked.connect(self.tampil_zakatmasuk)

    def tampil_mustahik(self):
        self.mustahik = formMustahik()
        self.mustahik.show()
        self.close()

    def tampil_muzaki(self):
        self.muzaki = formMuzaki()
        self.muzaki.show()
        self.close()

    def tampil_zakat(self):
        self.zakat = formZakat()
        self.zakat.show()
        self.close()

    def tampil_zakatkeluar(self):
        self.zakatkeluar = formZakatkeluar()
        self.zakatkeluar.show()
        self.close()

    def tampil_zakatmasuk(self):
        self.zakatmasuk = formZakatmasuk()
        self.zakatmasuk.show()
        self.close()

app = QApplication(sys.argv)
window = formUtama()
window.show()
sys.exit(app.exec())