from Source.Graphics import GUI
from PyQt5.QtWidgets import QApplication





# Show the UI and execute
app = QApplication([])
ui = GUI(25,2)
ui.show()
app.exec()