from PyQt5.QtWidgets import *
from loginn_1 import Ui_Form
from anapencere import ProcessPage
import sqlite3

conn=sqlite3.connect("database.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS users(kullanici_adi TEXT, parola TEXT) ")
class LoginPage(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.loginform = Ui_Form()
        self.loginform.setupUi(self)
        self.anapencereac = ProcessPage()
        self.loginform.pushButton.clicked.connect(self.giris_yap)
        self.loginform.pushButton_2.clicked.connect(self.kayit_ol)

    def giris_yap(self):
        kadi = self.loginform.lineEdit.text()
        sifre = self.loginform.lineEdit_2.text()
        cursor.execute("SELECT * FROM users WHERE kullanici_adi = ? and parola = ?",(kadi,sifre))
        data = cursor.fetchall()
        if len(data) == 0:
            self.loginform.lineEdit.setPlaceholderText("Giris Yapilamadi")
        else:
            self.hide()
            self.anapencereac.show()
    def kayit_ol(self):
        kadi = self.loginform.lineEdit.text()
        sifre = self.loginform.lineEdit_2.text()
        cursor.execute("INSERT INTO users VALUES (?,?)",(kadi,sifre))
        conn.commit()
        
        


        
        
