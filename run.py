import sys
from PyQt6.QtWidgets import QApplication, QStyleFactory
from my_library import LibraryApp

x = QStyleFactory.keys()

print(x)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle(x[1])

    library = LibraryApp()

    sys.exit(app.exec())

