from PyQt5.QtWidgets import *
from arayuz_1 import Ui_MainWindow
import requests


url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,cardano,solana,chainlink,uniswap,dogecoin,polkadot,litecoin,stellar&vs_currencies=usd'

response = requests.get(url)
data = response.json()


btc = str(data['bitcoin']['usd'])
eth = str(data['ethereum']['usd'])
ada = str(data['cardano']['usd'])
sol = str(data['solana']['usd'])
link = str(data['chainlink']['usd'])
uni = str(data['uniswap']['usd'])
doge = str(data['dogecoin']['usd'])
dot = str(data['polkadot']['usd'])
ltc = str(data['litecoin']['usd'])
xlm = str(data['stellar']['usd'])

class ProcessPage(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.processform = Ui_MainWindow()
        self.processform.setupUi(self)
        self.processform.BTC.setText(btc)
        self.processform.ETH.setText(eth)
        self.processform.ADA.setText(ada)
        self.processform.SOL.setText(sol)
        self.processform.LINK.setText(link)
        self.processform.UNI.setText(uni)
        self.processform.DOGE.setText(doge)
        self.processform.DOT.setText(dot)
        self.processform.LTC.setText(ltc)
        self.processform.XLM.setText(xlm)
        self.processform.pushButton_Hesapla.clicked.connect(self.hesapla)
        self.sonuc=0
        
    def hesapla(self):
        adet=float(self.processform.doubleSpinBox_Adet.text().replace(',', '.'))
        alis=float(self.processform.lineEdit_Alis.text().replace(',', '.'))
        alim_tutari=adet*alis
        if self.processform.comboBox_Coin.currentIndex()==0:
            suan=float(btc)
            total=suan*adet
        elif self.processform.comboBox_Coin.currentIndex()==1:
            suan=float(eth)
            total=suan*adet
        elif self.processform.comboBox_Coin.currentIndex()==2:
            suan=float(ada)
            total=suan*adet
        elif self.processform.comboBox_Coin.currentIndex()==3:
            suan=float(sol)
            total=suan*adet
        elif self.processform.comboBox_Coin.currentIndex()==4:
            suan=float(link)
            total=suan*adet
        elif self.processform.comboBox_Coin.currentIndex()==5:
            suan=float(uni)
            total=suan*adet
        elif self.processform.comboBox_Coin.currentIndex()==6:
            suan=float(doge)
            total=suan*adet
        elif self.processform.comboBox_Coin.currentIndex()==7:
            suan=float(dot)
            total=suan*adet
        elif self.processform.comboBox_Coin.currentIndex()==8:
            suan=float(ltc)
            total=suan*adet
        elif self.processform.comboBox_Coin.currentIndex()==9:
            suan=float(xlm)
            total=suan*adet  
        else:
            total=0 
        self.sonuc=total-alim_tutari
        self.processform.Label_KarZarar.setText(str(self.sonuc)+' $')