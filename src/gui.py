from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from src import calc


class Gui(QMainWindow):
    def __init__(self):
        super(Gui, self).__init__()
        self.init_gui()

    def init_gui(self):
        self.setGeometry(500, 500, 600, 600)
        self.setWindowTitle("FIRE calculator")

        self.input_netto_inc = QtWidgets.QLineEdit(self)
        self.input_netto_inc.move(250, 100)
        self.label_netto_inc = QtWidgets.QLabel(self)
        self.label_netto_inc.setText("Dein Netto-Einkommen:")
        self.label_netto_inc.adjustSize()
        self.label_netto_inc.move(50, 100)


        self.input_yrly_spending = QtWidgets.QLineEdit(self)
        self.input_yrly_spending.move(250, 150)
        self.label_yrly_spending = QtWidgets.QLabel(self)
        self.label_yrly_spending.setText("Deine Ausgaben (im Jahr)")
        self.label_yrly_spending.adjustSize()
        self.label_yrly_spending.move(50, 150)

        self.input_yrly_savings = QtWidgets.QLineEdit(self)
        self.input_yrly_savings.move(250, 200)
        self.label_yrly_savings = QtWidgets.QLabel(self)
        self.label_yrly_savings.setText("Soviel sparst Du im Jahr:")
        self.label_yrly_savings.adjustSize()
        self.label_yrly_savings.move(50, 200)

        self.input_saving_rate = QtWidgets.QLineEdit(self)
        self.input_saving_rate.move(250, 250)
        self.label_saving_rate = QtWidgets.QLabel(self)
        self.label_saving_rate.setText("Deine Sparquote")
        self.label_saving_rate.adjustSize()
        self.label_saving_rate.move(50, 250)

        self.input_cur_net_worth = QtWidgets.QLineEdit(self)
        self.input_cur_net_worth.move(250, 300)
        self.label_cur_net_worth = QtWidgets.QLabel(self)
        self.label_cur_net_worth.setText("Aktuelles Vermögen")
        self.label_cur_net_worth.adjustSize()
        self.label_cur_net_worth.move(50, 300)

        self.input_interest_rate = QtWidgets.QLineEdit(self)
        self.input_interest_rate.move(250, 350)
        self.label_interest_rate = QtWidgets.QLabel(self)
        self.label_interest_rate.setText("Jährliche Rendite")
        self.label_interest_rate.adjustSize()
        self.label_interest_rate.move(50, 350)

        self.input_swr = QtWidgets.QLineEdit(self)
        self.input_swr.move(250, 400)
        self.label_swr = QtWidgets.QLabel(self)
        self.label_swr.setText("Entnahmerate (SWR)")
        self.label_swr.adjustSize()
        self.label_swr.move(50, 400)

        self.btn_calculate = QtWidgets.QPushButton(self)
        self.btn_calculate.setText("calculate!")
        self.btn_calculate.move(250, 450)
        self.btn_calculate.clicked.connect(self.button_clicked)

    def button_clicked(self):
        print("clicked")
        calc.calculate_remaining(self)


def window():
    app = QApplication(sys.argv)
    gui = Gui()
    gui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    window()

