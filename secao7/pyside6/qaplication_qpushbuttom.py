# QApplication e QPushButton de PySide6.QtWidgets
# QApplication -> O Widget principal da aplicação
# QPushButton -> Um botão
# PySide6.QtWidgets -> Onde estão os widgets do PySide6

import sys
from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QGridLayout

app = QApplication(sys.argv)

botao = QPushButton('botão 1')
botao.setStyleSheet('font-size: 60px; color: blue')

botao2 = QPushButton('botão 2')
botao2.setStyleSheet('font-size: 60px; color: blue')

botao3 = QPushButton('botão 3')
botao3.setStyleSheet('font-size: 60px; color: blue')


central_widget = QWidget()

layout = QGridLayout()
central_widget.setLayout(layout)

layout.addWidget(botao, 1, 1)  # linha e coluna
layout.addWidget(botao2, 1, 2)
layout.addWidget(botao3, 3, 1, 1, 2)



central_widget.show()  # Central widget entre na hierarquia e mostre sua janela

app.exec() # O loop da aplicação

