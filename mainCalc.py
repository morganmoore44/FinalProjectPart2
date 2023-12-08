from guiCalc import *
from logicCalc import *

def main():
    application = QApplication([])
    window = LogicCalc()
    window.show()
    application.exec()

if __name__ == "__main__":
    main()