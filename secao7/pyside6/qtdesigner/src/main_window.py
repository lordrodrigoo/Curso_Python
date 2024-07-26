from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtCore import QEvent, QObject
from window import Ui_MainWindow  # Certifique-se de que o caminho está correto e que a classe Ui_MainWindow é importada
import sys

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # Conecte o sinal de clique do botão ao método
        self.pushSend.clicked.connect(self.changeLabelResult)
        

    def changeLabelResult(self):
        # Atualize o texto do label com o texto da linha de entrada
        text = self.lineName.text()
        self.labelResult.setText(text)

    def event(self, watched: QObject, event: QEvent) -> bool:
        return super().event(watched, event)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())
