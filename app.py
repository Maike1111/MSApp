"""
My first application
"""

import pathlib
from PyQt6 import uic, QtWidgets
import sys

from PyQt6.QtWidgets import QDialog



# import toga
# from toga.style import Pack
# from toga.style.pack import COLUMN, ROW
#
#
#  class MSApplication(toga.App):
#      def startup(self):
#          """Construct and show the Toga application.
#
#          Usually, you would add your application to a main content box.
#          We then create a main window (with a name matching the app), and
#         show the main window.
#         """
#          main_box = toga.Box()
#
#          self.main_window = toga.MainWindow(title=self.formal_name)
#          self.main_window.content = main_box
#          self.main_window.show()

class Login(QDialog):#
    def __innit__(self):
        print("in QDialog")



class MSApplikation(QtWidgets.QMainWindow):

    def __init__(self):
        super(MSApplikation, self).__init__()

        working_dir = str(pathlib.Path(__file__).parent.resolve())
        self.main_Window = uic.loadUi(working_dir + '\\resources\\main_window.ui', self)

        self.show()


def main():
    print("Test")
    app = QtWidgets.QApplication(sys.argv)

    main_window = MSApplikation()
    main_window.setWindowTitle('App Tutorial')

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
