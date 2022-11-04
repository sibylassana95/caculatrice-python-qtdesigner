from PyQt5 import QtCore, QtGui, QtWidgets
from calculatrice import Ui_MainWindow
ok = True


# affichages des numerique
def affiche1():
    global ok
    if(ok == True):
        ui.resultat.setText(ui.resultat.text()+"1")
    else:
        ui.resultat.setText("1")
        ok = True


def affiche2():
    global ok
    if(ok == True):
        ui.resultat.setText(ui.resultat.text()+"2")
    else:
        ui.resultat.setText("2")
        ok = True


def affiche3():
    global ok
    if(ok == True):
        ui.resultat.setText(ui.resultat.text()+"3")
    else:
        ui.resultat.setText("3")
        ok = True


def affiche4():
    global ok
    if(ok == True):
        ui.resultat.setText(ui.resultat.text()+"4")
    else:
        ui.resultat.setText("4")
        ok = True


def affiche5():
    global ok
    if(ok == True):
        ui.resultat.setText(ui.resultat.text()+"5")
    else:
        ui.resultat.setText("5")
        ok = True


def affiche6():
    global ok
    if(ok == True):
        ui.resultat.setText(ui.resultat.text()+"6")
    else:
        ui.resultat.setText("6")
        ok = True


def affiche7():
    global ok
    if(ok == True):
        ui.resultat.setText(ui.resultat.text()+"7")
    else:
        ui.resultat.setText("7")
        ok = True


def affiche8():
    global ok
    if(ok == True):
        ui.resultat.setText(ui.resultat.text()+"8")
    else:
        ui.resultat.setText("8")
        ok = True


def affiche9():
    global ok
    if(ok == True):
        ui.resultat.setText(ui.resultat.text()+"9")
    else:
        ui.resultat.setText("9")
        ok = True


def affiche0():
    global ok
    if(ok == True):
        ui.resultat.setText(ui.resultat.text()+"0")
    else:
        ui.resultat.setText("0")
        ok = True


def affichePoint():
    ui.resultat.setText(ui.resultat.text()+".")


def afficheDivise():
    ui.resultat.setText(ui.resultat.text()+"/")


def afficheMult():
    ui.resultat.setText(ui.resultat.text()+"*")


def afficheMoins():
    ui.resultat.setText(ui.resultat.text()+"-")


def affichePlus():
    ui.resultat.setText(ui.resultat.text()+"+")


def afficheDiv():
    ui.resultat.setText(ui.resultat.text()+"//")


def afficheMod():
    ui.resultat.setText(ui.resultat.text()+"%")


def affichePo():
    ui.resultat.setText(ui.resultat.text()+"(")


def affichePf():
    ui.resultat.setText(ui.resultat.text()+")")

# fonnction pour les operateur:
       
def afficheAc():
    ui.resultat.setText("")

def afficheDel():
    ui.resultat.setText(ui.resultat.text()[:-1])

def afficheEgal():
    ui.resultat.setText(str(eval(ui.resultat.text())))

import sys
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()


ui.b_1.clicked.connect(affiche1)
ui.b_2.clicked.connect(affiche2)
ui.b_3.clicked.connect(affiche3)
ui.b_4.clicked.connect(affiche4)
ui.b_5.clicked.connect(affiche5)
ui.b_6.clicked.connect(affiche6)
ui.b_7.clicked.connect(affiche7)
ui.b_8.clicked.connect(affiche8)
ui.b_9.clicked.connect(affiche9)
ui.b_0.clicked.connect(affiche0)
ui.b_plus.clicked.connect(affichePlus)
ui.b_moins.clicked.connect(afficheMoins)
ui.b_mult.clicked.connect(afficheMult)
ui.b_divise.clicked.connect(afficheDivise)
ui.b_div.clicked.connect(afficheDiv)
ui.b_mod.clicked.connect(afficheMod)
ui.b_point.clicked.connect(affichePoint)
ui.b_po.clicked.connect(affichePo)
ui.b_pf.clicked.connect(affichePf)

ui.b_ac.clicked.connect(afficheAc)
ui.b_del.clicked.connect(afficheDel)
ui.b_egale.clicked.connect(afficheEgal)


sys.exit(app.exec_())
