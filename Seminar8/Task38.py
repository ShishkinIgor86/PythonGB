from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QTextEdit)
from PyQt5.QtCore import pyqtSlot
import sys
import os.path


class MyApp(QWidget):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle('Телефонный справочник')
        self.setGeometry(600, 600, 300, 400)

        layout = QVBoxLayout()
        layout.addStretch(1)

        
        label1 = QLabel('Введите ФИО, номер телефона абонента:', self)
        layout.addWidget(label1)

        self.edit1= QLineEdit()
        layout.addWidget(self.edit1)


        self.button1 = QPushButton('Добавление контакта',self)
        self.button1.setFixedSize(150,25)
        self.button1.clicked.connect(self.on_button1_click)
        layout.addWidget(self.button1)

        label2 = QLabel('Вывести список всех контактов:', self)
        layout.addWidget(label2)

        self.button2 = QPushButton('Все контакты',self)
        self.button2.setFixedSize(150,25)
        self.button2.clicked.connect(self.on_button2_click)
        layout.addWidget(self.button2)

        self.text=QTextEdit()
        layout.addWidget(self.text)

        label3 = QLabel('Введите ФИО или номер телефона для поиска:', self)
        layout.addWidget(label3)

        self.edit2= QLineEdit()
        layout.addWidget(self.edit2)


        self.button3 = QPushButton('Поиск',self)
        self.button3.setFixedSize(150,25)
        self.button3.clicked.connect(self.on_button3_click)
        layout.addWidget(self.button3)

        label6 = QLabel('Результат поиска:', self)
        layout.addWidget(label6)

        self.text1=QTextEdit()
        layout.addWidget(self.text1)


        label4 = QLabel('Введите контакт для изменения:', self)
        layout.addWidget(label4)
        
        self.edit3= QLineEdit()
        layout.addWidget(self.edit3)
        self.edit3.textChanged.connect(self.edit3_on_change)

        label7 = QLabel('Введите изменение контакта:', self)
        layout.addWidget(label7)
        
        self.text2=QTextEdit()
        layout.addWidget(self.text2)
                
                
        self.button4 = QPushButton('Изменить',self)
        self.button4.setFixedSize(150,25)
        self.button4.clicked.connect(self.on_button4_click)
        layout.addWidget(self.button4)


        label6 = QLabel('Для удаления контакта загрузите книгу:', self)
        layout.addWidget(label6)

        self.button7 = QPushButton('Загрузить',self)
        self.button7.setFixedSize(150,25)
        self.button7.clicked.connect(self.on_button7_click)
        layout.addWidget(self.button7)


        label7 = QLabel('Удалите строку контакта целиком в поле ниже и нажмите кнопку Удалить:', self)
        layout.addWidget(label7)

        self.text4=QTextEdit()
        layout.addWidget(self.text4)
             
 
        self.button5 = QPushButton('Удалить',self)
        self.button5.setFixedSize(150,25)
        self.button5.clicked.connect(self.on_button5_click)
        layout.addWidget(self.button5)
       

        self.button6 = QPushButton('Закрыть',self)
        layout.addWidget(self.button6)
        self.button6.setFixedSize(150,25)
        self.button6.clicked.connect(self.on_button6_click)
                        

        self.setLayout(layout)

    def on_button1_click(self):
        if self.edit1.text()=='':
            QMessageBox.information(self,'Сообщение','Введите ФИО и номер телефона')
        else:
            with open('td.txt','a', encoding='utf8') as f:
                f.writelines(self.edit1.text()+'\n')
            QMessageBox.information(self,'Сообщение','Данные успешно внесены')
            self.edit1.setText('')

    def on_button2_click(self):
        s=''
        with open('td.txt','r', encoding='utf8') as f:
            for line in f:
                s+=line
        self.text.setPlainText(s)
     

    def on_button3_click(self):
        if self.edit2.text()=='':
            QMessageBox.information(self,'Сообщение','Введите строку для поиска')
        else:
            s=self.edit2.text()
            s_1=''
            with open('td.txt','r', encoding='utf8') as f:
                for line in f:
                    if s in line:
                        s_1+=line
        self.text1.setPlainText(s_1)

    
    @pyqtSlot(str)
    def edit3_on_change(self,text):
        s=self.edit3.text()
        s_1=''
        with open('td.txt','r', encoding='utf8') as f:
            for pr, line in enumerate(f):
                if s in line:
                    s_1+=str(pr)+') '+line
        self.text2.setPlainText(s_1)
        if s_1=='':
            QMessageBox.information(self,'Сообщение','Ничего не найдено')


    def on_button4_click(self):
        s=self.edit3.text()
        s1=''
        with open('td.txt','r', encoding='utf8') as f:
            for pr, line in enumerate(f):
                s1+=str(pr)+') '+line
        l_lines=s1.split('\n')
                   
        text=self.text2.toPlainText()
        l_text=text.split('\n')      


        if l_text==l_lines:
            QMessageBox.information(self,'Сообщение','Изменений не было')
        else:       
            buf1=''
            buf2=''     
            for i in range(len(l_lines)):
                buf1=l_lines[i].split(') ')
                for j in range(len(l_text)):
                    buf2=l_text[j].split(') ')                    
                    if buf1[0]==buf2[0]:
                        l_lines[i]=l_text[j]
        with open('td.txt','w', encoding='utf8') as f:
            for i in range(len(l_lines)):
                s=l_lines[i][l_lines[i].index(') ')+1:len(l_lines[i]):]+'\n'
                f.write(s.lstrip())
           
           
    def on_button7_click(self):
        s_1=''
        with open('td.txt','r', encoding='utf8') as f:
            for line in f:
                s_1+=line
        self.text4.setPlainText(s_1)
    
    
    def on_button5_click(self):
        text=self.text4.toPlainText()
        with open('td.txt','w', encoding='utf8') as f:
            f.writelines(text)
        QMessageBox.information(self,'Сообщение','Удаление контакта(ов) успешно завершено')

      
    @staticmethod
    def on_button6_click():
        QApplication.quit()
        print('OK')
   
def start():
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    my_app = MyApp()
    my_app.show()
    sys.exit(app.exec_())


if os.path.isfile('td.txt'):
    start()
else:
    f=open('td.txt','w')
    f.close()
    start()