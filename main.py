import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication


class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("custom.ui",self)

        #Down below are all the events of the app (clicking on a button, changing a value in a label or checkbox...)

        # Button
        self.button.clicked.connect(self.buttonclicked)

        # Check Box
        self.checkBox.stateChanged.connect(self.checked)

        # Combo Box
        self.comboBox.setVisible(False)
        listocc=["/","HR depart.", "Manager", "Customers support", "Python developer", "PHP developer","SQL developer","Web developer"]
        for job in listocc:
            self.comboBox.addItem(job)
        self.comboBox.currentIndexChanged.connect(self.combochanged)

        # Spin Box
        self.spinBox.setMinimum(0)
        self.spinBox.setMaximum(100)
        self.spinBox.valueChanged.connect(self.spinchanged)

    # function triggered when the button is pressed
    # the function is taking the value of both label/input as well as the status 
        # of the checkbox and printing those values into the console
    def buttonclicked(self):
        outputstr = self.fname.toPlainText()+ " " + self.lname.toPlainText()
        self.fname.setReadOnly(True)
        self.lname.setReadOnly(True)
        self.fname.setDisabled(True)
        self.lname.setDisabled(True)
        if self.checkBox.isChecked():
            outputstr=outputstr+" is employed"
        else:
            outputstr = outputstr + " is not employed"
        print(outputstr)

    # function triggered by a change of value on the combobox
    # the function is printing this combobox value INSIDE a label/input
        # it means this function is printing ON the GUI and not in the console!    
    def combochanged(self):
        self.outputlabel.setText(self.comboBox.currentText()+" is selected")

    # function triggered by a change of value on the component spinbox,
    # the function is printing in the console the value current value of the spinbox
    def spinchanged(self):
        print("current value" + str(self.spinBox.value()))

    # function triggered by a change of state of the checkbox
    # the fucntion is showing or not showing the compotent combobox depending on the state of the checkbox    
    def checked(self):
        if self.checkBox.isChecked():
            self.comboBox.setVisible(True)
        else:
            self.comboBox.setVisible(False)




# main
app = QApplication(sys.argv)
mainwindow = MainWindow()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedHeight(1050)
widget.setFixedWidth(1550)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Demo is closed")